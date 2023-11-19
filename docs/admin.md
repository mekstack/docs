# Admin Guides

В этой секции находится информация для администраторов облака.

- [Репозиторий с конфигурацией Kolla, Kayobe и IaC инфраструктуры](https://github.com/mekstack/mekstack)

## Архитектура

![Архитектура](images/l2.jpg)

*TODO: описание архитектуры*

## Bootstrapping kayobe host

> Почему отдельный сервер для kayobe?
> Тогда не произойдет ситуации, когда два разных человека с двумя разными
> конфигурациями одновременно деплоят одно облако.

## Enroll bifrost inventory

```bash
export OS_CLOUD=bifrost
export BIFROST_INVENTORY_SOURCE=/etc/bifrost/servers.yml
cd playbooks
ansible-playbook -vvvv -i inventory/bifrost_inventory.py enroll-dynamic.yaml
```

## Post deploy

Что надо делать после первого деплоя

### Configure db for mappings to fit

Для костылей интеграции с cabinet.miem.hse.ru нужно увеличить размер колонки
с маппингами, потому что они не помещаются в стандартный.

```bash
    docker exec -it mariadb bash
    mysql -u keystone -p

    use keystone;
    alter table mapping change rules rules longtext;
```

## Keystone

### Проблема

В режиме простоя (промежутки времени, когда не авторизуются пользователи и не создаются новые виртуальные машины) контейнер keystone в среднем потребляет 10% CPU. В log-файлах при режиме debug этом наблюдаются периодически появляющиеся сообщения (кроме прочих):

```bash
  2023-11-07 16:32:16.397 22 DEBUG keystone.server.flask.request_processing.req_logging [None req-48e1f6ba-137d-4d86-99b7-31290ca52631 - - - - - -] REQUEST_METHOD: `GET` log_request_info /var/lib/kolla/venv/lib/python3.10/site-packages/keystone/server/flask/request_processing/req_logging.py:27
  2023-11-07 16:32:16.397 22 DEBUG keystone.server.flask.request_processing.req_logging [None req-48e1f6ba-137d-4d86-99b7-31290ca52631 - - - - - -] SCRIPT_NAME: `` log_request_info /var/lib/kolla/venv/lib/python3.10/site-packages/keystone/server/flask/request_processing/req_logging.py:28
  2023-11-07 16:32:16.398 22 DEBUG keystone.server.flask.request_processing.req_logging [None req-48e1f6ba-137d-4d86-99b7-31290ca52631 - - - - - -] PATH_INFO: `/` log_request_info /var/lib/kolla/venv/lib/python3.10/site-packages/keystone/server/flask/request_processing/req_logging.py:29
  2023-11-07 16:32:16.401 24 DEBUG keystone.server.flask.request_processing.req_logging [None req-123200f8-a21d-4ab0-a9b6-8e04c5fe676e - - - - - -] REQUEST_METHOD: `POST` log_request_info /var/lib/kolla/venv/lib/python3.10/site-packages/keystone/server/flask/request_processing/req_logging.py:27
  2023-11-07 16:32:16.401 24 DEBUG keystone.server.flask.request_processing.req_logging [None req-123200f8-a21d-4ab0-a9b6-8e04c5fe676e - - - - - -] SCRIPT_NAME: `` log_request_info /var/lib/kolla/venv/lib/python3.10/site-packages/keystone/server/flask/request_processing/req_logging.py:28
  2023-11-07 16:32:16.402 24 DEBUG keystone.server.flask.request_processing.req_logging [None req-123200f8-a21d-4ab0-a9b6-8e04c5fe676e - - - - - -] PATH_INFO: `/v3/auth/tokens` log_request_info /var/lib/kolla/venv/lib/python3.10/site-packages/keystone/server/flask/request_processing/req_logging.py:29
  2023-11-07 16:32:16.424 24 WARNING keystone.common.password_hashing [None req-123200f8-a21d-4ab0-a9b6-8e04c5fe676e - - - - - -] Truncating password to algorithm specific maximum length 72 characters.
  2023-11-07 16:32:16.735 24 DEBUG keystone.auth.core [None req-123200f8-a21d-4ab0-a9b6-8e04c5fe676e - - - - - -] MFA Rules not processed for user `dc11a79816904e1dbfb5e719068f5820`. Rule list: `[]` (Enabled: `True`). check_auth_methods_against_rules /var/lib/kolla/venv/lib/python3.10/site-packages/keystone/auth/core.py:438
```

Причем появляются они с определенной периодичностью (xxxx.xx.xx-xx:xx:14-19, 56, 57. При этом существует корреляция между этими событиями и потреблением CPU: примерно в эти интервалы нагрузка на процессор достигает 100%, в остальное же время потребление составляет примерно 0%, с редкими выбросами в 8%. Режим debug также не дает дополнительной информации: keystone активизируется в вышеупомянутые интервалы и штатно производит аутентификацию поступающих запросов.
Важно также отметить, что, так как в своей работе keystone постоянно обращается к БД, то логичным было бы, что потребление CPU у БД тоже должно быть повышенным, но этого не происходит. Исходя из этого складывается впечатление, что высокое потребление CPU обосновано не слишком частыми запросами к keystone со стороны служб, а собственной неэффективной работой keystone.

### Возможные причины

1) Используются слишком длинные пароли и keystone постоянно тратит ресурсы на их обрезание;
2) Токены имеют слишком маленький срок жизни и из-за этого keystone приходится генерировать токены чаще. Возможно, стоит увеличить срок их жизни, но непонятно как это отразится на ИБ;
3) Описанная [здесь](https://bugs.launchpad.net/keystone/+bug/1182481) проблема о том, что БД со забита старыми токенами.

### Что можно сделать

1) Проверить корректность описанных в [документации](https://docs.openstack.org/keystone/pike/admin/identity-performance.html) параметров, влияющих на производительность;
2) Использовать профилировщики (например, cProfile) чтобы выяснить, какие именно операции занимают наибольшее время выполнения. Недостаток данного способа в том, что необходимо лезть в исходники Openstack и оборачивать каждую функцию в профилировщик. Но профилирование keystone можно включить и в самом keystone.conf файле . [Тут](https://docs.openstack.org/keystone/queens/configuration/samples/keystone-conf.html) нет полноценного гайда и нужно разбираться как потом доставать результаты профилирования из БД и интерпретировать их.
