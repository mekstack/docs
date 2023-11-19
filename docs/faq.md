# FAQ

Если что-то не понятно: **#mekstack** в Zulip.


## А где пароль для моей виртуалочки

Пароли это несесурно, делайте ссш ключи


## Create SSH key

``` bash
    ssh-keygen -t ed25519 -c "mekstack-key"
```


## Один из моих проектов не отображается

Актуальная информация о членах проекта берётся из [Кабинета МИЭМ](https://cabinet.miem.hse.ru). Если вас нет в проекте, попросите своего
руководителя вас добавить.


## 401 The request you have made requires authentication

Такая ошибка при логине возникает если вы не состоите ни в одном проекте.
Попросите своего руководителя добавить вас в проект.


## Как добавить несколько ssh ключей в инстанс?

Два варианта:

1. **Передать их в user-data.**

   В ``Launch Instance / Configuration`` вставьте в Configuration Script YAML
   конфигурацию формата cloud-init. [Пример](https://cloudinit.readthedocs.io/en/latest/topics/examples.html#configure-instances-ssh-keys).

2. **Сложить их в keypair.**

   В [Import Public Key](https://mekstack.ru/project/key_pairs) в поле Public
   Key нужно вставить все публичные ключи. Они будут скопированы в ``authorized_keys``.

   > Если в keypair несколько ключей, то сломается Managed K8s (Magnum). Для него
   > в keypair должен быть строго один ключ.


### Хайповый вариант: SSH PKI

Выпишите корневой SSH сертификат и подпишите им ваши ключи.
[Хорошая лекция про SSH PKI](https://www.youtube.com/watch?v=lYzklWPTbsQ).
