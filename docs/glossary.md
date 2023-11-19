# Glossary


## Инстанс {#instance}

In OpenStack, we refer to provisioned compute nodes as **instances** and not
**virtual machines**. Although this might seem like a matter of semantics, it's
a useful device for a few reasons. The first reason is that it describes the
deployment mechanism; all compute in OpenStack is the instantiation of a [glance](services.md#glance)
image with a specified hardware template, the [flavor](glossary.md#flavor).

The second reason that the term instance is useful is that virtual machines in
OpenStack do not typically have the same life cycle as they do in traditional
virtualization. Although we might expect virtual machines to have a multiyear
life cycle like physical machines, we would expect instances to have a life
cycle which is measured in days or weeks. Virtual machines are backed up and
recovered, whereas instances are rescued or evacuated. Legacy virtualization
platforms assume resizing and modifying behaviors are in place; cloud
platforms such as OpenStack expect redeployment of virtual machines or adding
additional capacity through additional instances, not adding additional
resources to existing virtual machines.

The third reason that we find it useful to use the term instance is that the
Compute service has evolved over the years to launch a number of different
types of compute. Some OpenStack deployments may only launch physical machines,
whereas others may launch a combination of physical, virtual, and
container-based instances. The same construct applies, regardless of the
compute provider. Some of the lines between virtual machines and instances are
becoming more blurred as more enterprise features are added to the OpenStack
Compute service.


## Image {#image}

Имадж это файл, который содержит виртуальный диск с операционной системой.
Имаджи используются для создания инстансов.


## Flavor {#flavor}

The flavor describes the characteristics of the instantiated image, and it
normally represents a number of cores of compute with a given amount of memory
and storage. Storage may be provided by the Compute service or the block
storage service.


## Zarm {#zarm}

В наших имаджах есть zram, он позволяет в 2-3 раза сжимать использующуюся
оперативную память, тем самым уменьшая количество потребляемых ресурсов.

Если на обычных серверах вашему сервису нужен 1 GB RAM, в нашем имадже ему
хватит 500 MB.


## Network {#network}

Контейнер для подсетей и роутеров.


## Subnetwork {#subnetwork}

Блок IP адресов. Подсети используются как источники IP адресов для новых
портов. Проекты могут создавать подсети с любыми адресами без ограничений.


## Provider (external) network {#provider-network}

Сеть, из которой есть доступ в интернет и которой нельзя управлять из облака.
Например, сеть ВШЭ. IP адреса в этой сети доступны всем, кто физически
подключён к этой сети даже вне облака.


## Overlay (internal) network {#overlay-network}

Виртуальная сеть, которой полностью управляет tenant. Реализована при помощи
VXLAN или GRE протоколов. Для того, чтобы из неё получить доступ в интернет,
нужно прикрепить к ней виртуальный роутер с default gateway в provider network.

Для того, чтобы получить доступ к адресам внутренней сети из внешней и наоборот,
необходимо соединить их виртуальным роутером.


## Floating IP {#fip}

Адрес в provider сети, с которого входящие пакеты форвардятся на адрес overlay
сети. Если такой адрес привязать к инстансу из оверлей сети, к нему можно будет
подключаться по этому адресу.


## Security Group {#security-group}

Firewall. Набор правил, по которым определяется решение раутинга входящего
и исходящего трафика. По дефолту запрещает все входящие подключения **кроме
подключений от инстансов из этой Security Group** и разрешает все исходящие.

By default, all security groups contain a series of basic (sanity) and
anti-spoofing rules that perform the following actions:

* Allow egress traffic only if it uses the source MAC and IP addresses of the
  port for the instance, source MAC and IP combination in
  **allowed-address-pairs**, or valid MAC address (port or
  **allowed-address-pairs**) and associated EUI64 link-local IPv6 address.
* Allow egress DHCP discovery and request messages that use the source MAC
  address of the port for the instance and the unspecified IPv4 address
  (0.0.0.0).
* Allow ingress DHCP and DHCPv6 responses from the DHCP server on the subnet so
  instances can acquire IP addresses.
* Deny egress DHCP and DHCPv6 responses to prevent instances from acting as
  DHCP(v6) servers.
* Allow ingress/egress ICMPv6 MLD, neighbor solicitation, and neighbor
  discovery messages so instances can discover neighbors and join multicast
  groups.
* Deny egress ICMPv6 router advertisements to prevent instances from acting as
  IPv6 routers and forwarding IPv6 traffic for other instances.
* Allow egress ICMPv6 MLD reports (v1 and v2) and neighbor solicitation
  messages that use the source MAC address of a particular instance and the
  unspecified IPv6 address (::). Duplicate address detection (DAD) relies on
  these messages.
* Allow egress non-IP traffic from the MAC address of the port for the instance
  and any additional MAC addresses in **allowed-address-pairs** on the port for
  the instance.


## Load Balancer {#load_balancer}

Балансировщик нагрузки используется для распределения входящего трафика между
уже существующими виртуальными машинами.

Наши балансировщики запускаются в конфигурации ACTIVE-STANDBY для обеспечения
максимальной доступности.

