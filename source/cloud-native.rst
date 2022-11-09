Cloud Native
============

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
ODO
