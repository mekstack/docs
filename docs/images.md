# Linux Autobuilds

> Мы собираем слегка модифицированные имаджи линуксов, чтобы они лучше интегрировались в мекстак и ими было приятней пользоваться.

**Поставить звездочку и почитать код нужно тут:** https://github.com/mekstack/images

Сейчас в арсенале автобилдов Ubuntu 22 и Debian 12.
Ubuntu minimal это очень легкий образ, который нужно использовать с
флейвором ``m2s.micro`` для ногинсков и бастионов.


## Что в имаджах

- **rootfs на btrfs**

  Можно делать снапшоты, проставлять квоты, на живую расширять файловые системы. ext4cels btfo.

  Еще там LZO сжатие, чтобы твои стогиговые бекапы /dev/zero не занимали места.

- **Пакеты**

  ``vim, ncdu, neofetch, fzf, pastebinit, nano, man,``

  ``iputils-ping, dnsutils, docker, qemu-guest-agent``

  ``bash-completion, python-is-python3, htop``

- **Кастомный .bashrc**

  [aliasы](https://github.com/mekstack/images/blob/ae6b022d0c5c6cbbefed7d817a09c7223cf68908/elements/mekstack/static/etc/skel/.bashrc#L82)

  **fzf**: ``<Ctrl-R>`` в баше для fuzzy поиска по ``history``

- **.vimrc с undofile**

- **Europe/Moscow таймзона**


## Что еще не в имаджах

- **Мекстак зеркала для apt, pip, docker**

  Появятся когда мы захостим кеширующие реджистри

- **MONaaS agent**

  Будет собирать логи с виртуалок для Monitoring as a Service

Что-то не работает или хочешь еще фичу?

Пиши, мы добавим. Или сам добавь.
