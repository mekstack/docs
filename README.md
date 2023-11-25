# Diplodoc

Все исходные файлы документации, подлежащие изменению лежат в [*docs*](./docs/)

Структура проекта имеет следующий вид:
```
mekstack/docs/docs
|-- .yfm                      (Файл конфигурации проекта)
|-- toc.yaml                  (Файл конфигурация боковой навигационной панели с оглавлением)
|-- index.yaml                (Скелет разводящей страницы)
|-- quick-start.md            (Контент для страницы Quick Start +Lore)
|-- heat-quick-start.md       (Контент для страницы Quick Start -Lore)
|-- cloud-native.md           (Контент для страницы Cloud Native)
|-- images.md                 (Контент для страницы Linux Autobuilds)
|-- admin.md                  (Контент для страницы Admin Guides)
|-- glossary.md               (Контент для страницы Glossary)
|-- services.md               (Контент для страницы Services)
|-- index.md                  (Контент для главной страницы)
|-- faq.md                    (Контент для страницы FAQ)
|-- images                    (Каталог с изображениями для страниц)
    |-- l2.jpg
    |-- l3-lore.png
    |-- sneedaas.png
|-- files                     (Прочее)
    |-- heat-quick-start.yaml (Манифест для разворачивания виртуалок)
```

Если нужно что-то добавить, то открываем нужный .md файл, редактируем его в синтаксисе MarkDown и создаем Pull Request. После, в комментарии к вашему Pull Request'у появится ссылка на получившуюся документацию вида `pr-#.docs.mekstack.ru` где #-номер вашего Pull Request'a. После ревизии и merg'a владельцем изменения появятся на `docs.mekstack.ru`.


# Настройка S3

1. Переходим на сайт [Yandex Cloud](https://cloud.yandex.ru/services/storage)  
2. Регистрируемся при необходимости и переходим в [консоль](https://console.cloud.yandex.ru/)  
3. Жмем в верхнем правом углу **Создать ресурс**, там выбираем **Бакет**, вводим желаемое имя бакета и его размер, выбираем **Доступ на чтение объектов: публичный**, чтобы Nginx имел доступ к документации.  
4. Далее нужно создать своего рода токен, по которому через API мы сможем управлять бакетом. Переходим на главную страницу [консоли](https://console.cloud.yandex.ru/) и жмем на **Сервисные аккаунты**, в верхнем правом углу выбираем **Создать сервисный аккаунт**, вводит желаемое имя и описание, выбираем **Роль: admin**, жмем создать и записываем куда-нибудь **acces_key** и **secret_key**.
5. Переходим на главной странице [консоли](https://console.cloud.yandex.ru/) в свои бакеты и выбираем созданный. В боковом меню выбираем **Веб-сайт**. Далее жмем **Хостинг**, в качестве главной страницы выбираем **index.html** и жмем сохранить. Это нужно для того чтобы S3 сам хостил наши статические файлы, а мы через Nginx просто проксировали все запросы с *.docs.mekstack.ru на этот веб-сайт.
6. Переходим в Репозиторий -> Settings -> Secrets and variables -> Actions.
    - Во вкладке Secrets с помощью кнопки **New repository** secret создаем два секрета, куда вписываем соответственно полученные ранее **acces_key** и **secret_key**:
        - **DIPLODOC_ACCESS_KEY_ID**
        - **DIPLODOC_SECRET_ACCESS_KEY**
    - Во вкладке Variables с помощью кнопки **New repository variable** создаем три переменые:
        - **DIPLODOC_STORAGE_BUCKET** со значением имени бакета, которое вы указали на этапе создания бакета
        - DIPLODOC_STORAGE_ENDPOINT со значением `https://storage.yandexcloud.net`
        - DIPLODOC_STORAGE_REGION со значением `ru-central1`
