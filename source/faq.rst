FAQ
===

Если ответа на ваш вопрос здесь нет, пишите в **#mekstack** в Zulip.

Create SSH key
--------------

.. code::

    ssh-keygen -t ed25519 -c "mekstack-key"

Один из моих проектов не отображается
-------------------------------------

Актуальная информация о членах проекта берётся из `Кабинета МИЭМ
<https://cabinet.miem.hse.ru>`_. Если вас нет в проекте, попросите своего
руководителя вас добавить.

401 The request you have made requires authentication
-----------------------------------------------------

Такая ошибка возникает если вы не состоите ни в одном проекте.
Попросите своего руководителя добавить вас в проект.

Как добавить несколько ssh ключей в инстанс?
--------------------------------------------

Два варианта:

#. **Передать их в user-data.** 

   В ``Launch Instance / Configuration`` вставьте в Configuration Script YAML
   конфигурацию формата cloud-init. `Пример.
   <https://cloudinit.readthedocs.io/en/latest/topics/examples.html#configure-instances-ssh-keys>`_

#. **Сложить их в keypair.**

   В `Import Public Key <https://mekstack.ru/project/key_pairs>`_ в поле Public
   Key нужно вставить все публичные ключи. Они будут скопированы в ``~/.ssh/authorized_keys``.
