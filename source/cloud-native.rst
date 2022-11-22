Cloud Native
============

OpenStack CLI
-------------

У OpenStack есть свое консольное приложение, через которое можно
взаимодействовать со всеми доступными API (в web--интерфейсе Horizon, например,
доступны не все API эндпоинты). 

Устанавливается так:

.. code-block::

   pip install python-openstackclient # Для основных сервисов OpenStack
   pip install python-octaviaclient # Для Octavia

После этого станет доступна команда ``openstack``.

Чтобы получить доступ к API через openstack--cli, нужно передать информацию для
авторизации. Это можно сделать через env переменные ``OS_*`` или через файл
``clouds.yaml``.

Скачать ваш clouds.yaml можно из web--интерфейса. Для этого
в ``Identity / Application Credentials`` создайте Application
Credential и сохраните сгенерированный файл clouds.yaml в директорию
``~/.config/openstack/clouds.yaml``. 

.. note::

    openstack--cli сначала ищет ``clouds.yaml`` в ``$PWD``, а затем
    в ``~/.config/openstack/``.

В clouds.yaml можно хранить несколько credentials. Выбор credential из файла
производится переменной ``OS_CLOUD``. Например, для такого clouds.yaml, выбор
осуществляется через ``export OS_CLOUD=19106`` или ``export OS_CLOUD=370``. 

.. code-block:: yaml

   clouds:
     19106:
       auth:
         auth_url: https://mekstack.ru:5000
         application_credential_id: "10efec9b264846a19a091b7a6aeed2af"
         application_credential_secret: "Hlf2--a6axPUjlSAMp3iJ8Qp0xaM"
       region_name: "MIEM"
       interface: "public"
       identity_api_version: 3
     370:
       auth:
         auth_url: https://mekstack.ru:5000
         application_credential_id: "usf9KLjhYPfMf2erlSYx8WkK9BIGSGz8"
         application_credential_secret: "8OBauPKX29P3UPXvvvRyROp0xaM"
       region_name: "MIEM"
       interface: "public"
       identity_api_version: 3

Проверить работу можно командой ``openstack token issue``. Вывод должен выглядеть так:

.. code-block:: none
   
   $ export OS_CLOUD=mekstack
   $ openstack token issue
   +------------+-------------------------------------------+
   | Field      | Value                                     |
   +------------+-------------------------------------------+
   | expires    | 2022-11-23T13:06:49+0000                  |
   | id         | gAAAAABjfMlpYPfn2D2GxoSRIdRhpztxRCNkppIq0 |
   | project_id | 01b8eb750e504914ad478e2451043f43          |
   | user_id    | ec63c92a5b324c9faf43cd1d0a44b428          |
   +------------+-------------------------------------------+

Pets vs Cattle
--------------

В предыдущем IaaS виртуальные машины были как *домашние животные* -- с ними
нужно было действовать аккуратно, в случае поломки -- обращаться за помощью и
вручную восстанавливать.  

Промышленный подход к инфраструктуре называется `Cloud Native
<https://learn.microsoft.com/en-us/dotnet/architecture/cloud-native/definition>`_
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

`<https://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle/>`_

.. _terraform:

Terraform
---------

Terraform -- инструмент для управления инфраструктурой по технологии `IaC <https://en.wikipedia.org/wiki/Infrastructure_as_code>`_ с
открытым исходным кодом, позволяющий безопасно и нативно создавать и изменять
инфраструктуру.

Сейчас Terraform не доступен из РФ, однако им все еще можно пользоваться,
используя зеркала.

Для этого нужно создать файл ``~/.terraformrc`` с таким содержимым

.. code-block::

        provider_installation {
          network_mirror {
            url     = "https://nm.tf.org.ru/"
            include = ["registry.terraform.io/*/*"]
          }
          direct {
            exclude = ["registry.terraform.io/*/*"]
          }
        }

После этого команда ``terraform init`` будет работать

Документация terraform тоже не открывается из РФ, но у неё тоже есть зеркало:
`<https://registry.tfpla.net/providers/terraform-provider-openstack/openstack/latest/docs>`_

Ansible
-------

Ansible — система управления конфигурациями, написанная на языке программирования Python, с использованием декларативного языка разметки для описания конфигураций. Применяется для автоматизации настройки и развёртывания программного обеспечения.

Ansible имеет большое количество пользователей и нативные модули для решения большинства задач деплоя и конфигурации

`Сайт Ansible <https://www.ansible.com/>`_

Miroservices
-------------
TODO
