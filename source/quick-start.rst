Quick Start
===========

При возникновении вопросов во время работы с облаком, поищите ответы
в :doc:`faq`.

Настройка DNS
-------------

Прежде чем начать работу с облаком, нужно настроить DNS. Mekstack использует
свой приватный :ref:`DNSaaS` сервис. С его помощью можно подключаться
к инстансам по домену, а не по IP-адресу: ``ssh arch@web1.myservice.miem``
вместо ``ssh arch@172.18.220.68``.

Для того, чтобы адрес используемого DNS-сервера автоматически менялся при
подключении к VPN облака, необходимо отредактировать конфигурацию подключения.
Добавьте это в начало файла ovpn конфигурации.

.. code-block::

    pull-filter accept "dhcp-option DNS"
    dhcp-option DNS 172.18.221.21
    dhcp-option DNS 8.8.8.8

.. note::

    На Linux DNS конфигурация не изменится при подключении к VPN командой
    `openvpn`. Используйте такой systemd, OpenRC или s6 сервис OpenVPN, который
    будет автоматически редактировать `/etc/resolv.conf`.

    На systemd хорошо работает скрипт `update-resolv-conf
    <https://github.com/alfredopalhares/openvpn-update-resolv-conf>`_.

При правильной конфигурации после подключения к VPN в `/etc/resolv.conf`
появится строчка ``nameserver 172.18.221.21``, а после отключения исчезнет. Подробнее --
`<https://wiki.archlinux.org/title/OpenVPN#DNS>`_, `man
5 resolv.conf` и `man 5 nsswitch.conf`.

Вход в Mekstack
---------------

Для входа в веб интерфейс нажмите кнопку **Log In** на `mekstack.ru
<https://mekstack.ru>`_. 

При первом входе автоматически создадутся проекты, в которых вы состоите.
Переключаться между ними можно через меню в левом верхнем углу.

Запуск своего образа
--------------------

.. note::

   You can skip all these steps and use a `Project template with Terraform and
   Ansible <https://github.com/mmskv/openstack-project-template>`_ instead.

#. Create :ref:`overlay-network`:

   #. Project -> Networks -> Create Network. Set any name.

   #. Create subnet with any CIDR. In allocation pools specify IPs that you
      want to be allocated.

   #. Don't specify DNS Name Servers and Host Routes.

   #. Now you have your subnet but it is not connected to the :ref:`provider` network.
      Go to Project -> Network -> Routers and create a new Router. Select **provider** 
      network to be external.

   #. **Connect your subnet to the Router.**
      Click on your new Router -> Interfaces -> Add Interface. Select the
      subnet you have created earlier and click Submit. Now the subnet is
      reachable from the provider network and the other way.

#. Edit **default** :ref:`security-group` to allow ingress ICMP (ping) and SSH
   traffic. By default Security Groups block all external ingress traffic.

   #. Project -> Network -> Security Groups -> Manage Rules

   #. Add Rule -> Rule -> All ICMP -> ADD

   #. Add Rule -> Rule -> SSH -> ADD

#. Launch :ref:`instance`

   #. Compute -> Instances -> Launch Instance

   #. In instance description write what is this instance is used for. For
      example: "Django server that serves static cat images"

   #. Select a base OS. Arch Linux is generally two times faster than Ubuntu as
      it has btrfs filesystem compression.

   #. Select suitable :ref:`flavor`

   #. Network. Select network that you created in the first step. Don't select
      **provider** network.

   #. In Key Pair menu import your SSH public key.

   #. Launch Instance

   #. Attach floating IP: Go to Project -> Compute -> Instances -> Click the
      rightmost arrow in the *Actions* column -> Associate Floating IP.

   #. Connect to instance via ssh. ``ssh user@172.18.130.xxx``. User for Ubuntu
      is **ubuntu**, user for Arch Linux is **arch**.

.. note:: 
   
    First start of Arch Linux instance can take a minute

DNS
---

Для того, чтобы использовать хостнеймы вместо IP адресов, можно создать 
DNS-записи в своей зоне.

Каждый проект может создавать собственные DNS зоны в формате **<name>.corp.**,
где **<name>** -- произвольная строка. В этих зонах можно создавать DNS записи. Все
зоны резолвятся на центральном DNS сервере **172.18.221.21**.

Ручное управление DNS записями всех своих инстансов плохо масштабируется,
поэтому рекомендуем использовать :ref:`terraform` для управления DNS.

Publish your app
----------------

Перед публикацией приложения в интернет необходимо провести его аудит. Для
этого вашему руководителю необходимо отправить заявку в отдел ИБ ВШЭ по
инструкции :doc:`audit`. 
