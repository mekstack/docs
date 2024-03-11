# Redpilled Quick Start

С помощью этой инструкции вы создадите виртуалку, подключитесь к VPN и настроете на ней простой HTTPS сервер.

## Настройка сети

Без сетей в наше время никуда, создай себе одну.

{% list tabs %}

- Web

  test

- Terraform

  ```terraform
  data "openstack_networking_network_v2" "public" {
    name = var.public_network_name
  }
  resource "openstack_networking_network_v2" "network" {
    name           = var.name
    admin_state_up = true
  }
  resource "openstack_networking_subnet_v2" "subnet" {
    name       = var.name
    network_id = openstack_networking_network_v2.network.id
    cidr       = "10.0.0.0/24"
    ip_version = 4
  }
  ```

- CLI




{% endlist %}

### Создание Overlay (internal) сети

### Создание Роутера

### Настройка Security Groups

## Запуск Инстанса

### Добавление FIP
