Services
========

TODO Custom Linux Images
------------------------

Custom images are provided by the **mekstack** project.
They are built and auto tested daily.

Our images contain the following modifications:

* Use local pacman, apt, pip and docker mirrors

* Use :ref:`zram` to optimize RAM utilization

* Filesystem modifications: Btrfs with ``compress-force=zstd:6,autodefrag,noatime``

* Pre-installed packages: ``vim nano ncdu git htop bind net-tools rsync
  wgetpaste bash-completion fzf``

  * Images with Docker have ``docker`` and ``docker-compose`` installed and enabled

* Timezone set to Europe/Moscow

* Custom bashrc with `fzf <https://wiki.archlinux.org/title/Fzf>`_ keybinds

  * ``Ctrl+t`` list files+folders in current directory (e.g., type ``git
    add``, press ``Ctrl+t``, select a few files using ``Tab``, finally
    ``Enter``)

  * ``Ctrl+r`` search history of shell commands

  * ``Alt+c`` fuzzy change directory

* Cloud-specific customizations:

  * DHCP Client listens on **all** interfaces to support dynamic interface
    attachment

Thanks to these modifications our images are faster and more efficient than
default cloud images, so use your own images only in special circumstances.

.. note::

   If your application depends on ``atime``, you should disable ``noatime``

   If your workflow depends on not having DHCP on new interfaces, remove
   ``/etc/udev/rules.d/10-dhlient.rules`` and
   ``/etc/netplan/90-dhcp-on-all-interfaces.yaml``

Monitoring
----------

Мы предоставляем информацию о доступности и загруженности сервисов облака
в `Cloud Health Dashboard <http://status.corp>`_.

Метрики утилизации инстансов своего и чужих проектов можно посмотреть в
`Instances Dashboard <http://status.corp/d/ysqRegynk/projects>`_.

По предложениям улучшения дашбордов пишите нам в Zulip.

Local Mirrors
-------------

We provide mirrors for selected services

Python package mirror
^^^^^^^^^^^^^^^^^^^^^

TODO

Arch repos mirror
^^^^^^^^^^^^^^^^^

TODO

Ubuntu repos mirror
^^^^^^^^^^^^^^^^^^^

TODO

Docker mirror and registry
^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO

LBaaS
-----

SaaS
----

.. _paas:

PaaS
----

.. _glance:

Glance
------

.. _ddi:

DDI
---

DNS
^^^

DHCP
^^^^

IPAM
^^^^
