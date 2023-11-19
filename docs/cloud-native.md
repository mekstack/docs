# Cloud Native


## OpenStack CLI

У OpenStack есть свое консольное приложение, через которое можно работать со
всеми доступными сервисами (в гуях mekstack.ru, например, доступны не все API
эндпоинты).

Устанавливается так:

``` bash
   pip install python-openstackclient # Для основных сервисов OpenStack
   # остальные клиенты выполнены модулями и их можно устанавливать отдельно
   pip install python-octaviaclient # Для Octavia
   pip install python-magnumclient # Для Magnum k8s
   pip install python-{{ servicename }}client # В общем
```

После этого станет доступна команда ``openstack``.

Чтобы подключиться к API не через браузер нужно как-то передать информацию для
авторизации. Это можно сделать через env переменные ``OS_*`` или через файл
``clouds.yaml``.


### Доступ в API по clouds.yaml

Клауды надо настраивать для всех приложений, которые ходят в апи опенстака.
Ansible, Terraform, openstacksdk, Gophercloud и остальные.

Скачать свой **clouds.yaml** можно из гуев. Для этого в ``Identity / Application Credentials`` создай **Application Credential** и скачай клаудс в директорию ``~/.config/openstack/clouds.yaml``.

> При создании **Application Credentials** нельзя выбирать только роль ``member``.
> Поэтому или не выбирай роли или выбери все сразу.

**openstack-cli** ищет ``clouds.yaml`` сначала в ``$PWD``, а затем в ``~/.config/openstack/``.
В clouds.yaml можно хранить креды от нескольких проектов. Консольные проги
выбирают какой клауд юзать для авторизации по переменной енва ``OS_CLOUD``.
Например, для такого клаудса выбрать проект можно через ``export
OS_CLOUD=19106`` или ``export OS_CLOUD=370``.

``` yaml
   clouds:
     19106:
       auth:
         auth_url: https://keystone.api.mekstack.ru/v3
         application_credential_id: "10efec9b264846a19a091b7a6aeed2af"
         application_credential_secret: "Hlf2--a6axPUjlSAMp3iJ8Qp0xaM"
       region_name: "MIEM"
       interface: "public"
       identity_api_version: 3
     370:
       auth:
         auth_url: https://keystone.api.mekstack.ru/v3
         application_credential_id: "usf9KLjhYPfMf2erlSYx8WkK9BIGSGz8"
         application_credential_secret: "8OBauPKX29P3UPXvvvRyROp0xaM"
       region_name: "MIEM"
       interface: "public"
       identity_api_version: 3
```

Затестить можно командой ``openstack token issue`` например. Вывод должен выглядеть так:

``` none
   $ OS_CLOUD=mekstack openstack token issue
   +------------+-------------------------------------------+
   | Field      | Value                                     |
   +------------+-------------------------------------------+
   | expires    | 2022-11-23T13:06:49+0000                  |
   | id         | gAAAAABjfMlpYPfn2D2GxoSRIdRhpztxRCNkppIq0 |
   | project_id | 01b8eb750e504914ad478e2451043f43          |
   | user_id    | ec63c92a5b324c9faf43cd1d0a44b428          |
   +------------+-------------------------------------------+
```


## Pets vs Cattle

В предыдущем IaaS виртуальные машины были как *домашние животные* -- с ними
нужно было действовать аккуратно, в случае поломки -- обращаться за помощью и
вручную восстанавливать.

Промышленный подход к инфраструктуре называется [Cloud Native](https://learn.microsoft.com/en-us/dotnet/architecture/cloud-native/definition)
и рассматривает виртуальные машины как *скот* -- архитектура приложения
рассчитывает на то, что рано или поздно виртуальные машины упадут. Поэтому
архитектура поддерживает редеплой сломанной инфраструктуры при помощи таких
инструментов, как Ansible, Terraform, cloud-config.

Servers or server pairs that are treated as indispensable or unique systems that
can never be down. Typically they are manually built, managed, and “hand fed”.
Examples include mainframes, solitary servers, HA loadbalancers/firewalls
(active/active or active/passive), database systems designed as master/slave
(active/passive), and so on.

Arrays of more than two servers, that are built using automated tools, and are
designed for failure, where no one, two, or even three servers are
irreplaceable. Typically, during failure events no human intervention is
required as the array exhibits attributes of “routing around failures” by
restarting failed servers or replicating data through strategies like triple
replication or erasure coding. Examples include web server arrays, multi-master
datastores such as Cassandra clusters, multiple racks of gear put together in
clusters, and just about anything that is load-balanced and multi-master.

The key here is that in the old world redundancy through having two of
everything, the ubiquitous HA pair in the enterprise datacenter, is not enough.
What is required is assuming that failures can and will happen. That every
server, every component is able to fail without impacting the system.

https://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle/


## Terraform

Terraform -- инструмент для управления инфраструктурой по технологии [IaC](https://en.wikipedia.org/wiki/Infrastructure_as_code) с открытым исходным
кодом, позволяющий безопасно и нативно создавать и изменять инфраструктуру.

Терраформ нас не любит поэтому запретил доступ к своим серверам. Но у нас
есть зеркала!

Для того чтобы ими воспользоваться нужно создать файл ``~/.terraformrc`` с таким содержимым

``` terraform

    provider_installation {
      network_mirror {
        url = "https://registry.comcloud.xyz/"
        include = ["registry.terraform.io/*/*"]
      }
      direct {
        exclude = ["registry.terraform.io/*/*"]
      }
    }
```

После этого ``terraform init`` будет работать

Документация terraform тоже заблочена, но и на неё нашлось зеркало:

https://docs.comcloud.xyz/providers/terraform-provider-openstack/openstack


## Ansible

Ansible -- YAML фронтенд к питону, чтобы выполнять почти идемпотентные команды
на серверах по ссш.


## Miroservices

TODO
