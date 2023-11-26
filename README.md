# Mekstack Cloud Docs

Diplodoc is a toolchain to build and publish static documentation.
Markdown files are rendered into HTMLs with a pipeline and stored on S3.

Docs `.md` sources are in `./docs`.

## mekstack/docs structure

```
docs
|-- .yfm                      (yfm config)
|-- toc.yaml                  (leftmost tabe of contents config)
|-- index.yaml                (main page)
|-- presets.yaml              (variables that expand at compile time)
|-- images
|-- files
manifests                     (k8s stuff managed by rancher fleet)

index.html                    (index for local builds with npm start)
package.json                  (npm packages)
package-lock.json
serve.js                      (script to serve build and live reload)
```

# How to build

```
npm i
npm start
```

# How to contribute

Fork the repo. Edit the markdown. Commit. Push. Create Pull Request.

Your changes will be available at the link in pr's comments.

# S3 Setup

Currently we use Yandex as our S3 provider. This will change after we deploy Ceph.

##

1. Переходим на сайт [Yandex Cloud](https://cloud.yandex.ru/services/storage)
2. Регистрируемся при необходимости и переходим в [консоль](https://console.cloud.yandex.ru/)
3. Жмем в верхнем правом углу **Создать ресурс**, там выбираем **Бакет**, вводим желаемое имя бакета и его размер, выбираем **Доступ на чтение объектов: публичный**, чтобы Nginx имел доступ к документации.
4. Далее нужно создать своего рода токен, по которому через API мы сможем управлять бакетом. Переходим на главную страницу [консоли](https://console.cloud.yandex.ru/) и жмем на **Сервисные аккаунты**, в верхнем правом углу выбираем **Создать сервисный аккаунт**, вводит желаемое имя и описание, выбираем **Роль: admin**, жмем создать и записываем куда-нибудь **acces_key** и **secret_key**.
5. Переходим на главной странице [консоли](https://console.cloud.yandex.ru/) в свои бакеты и выбираем созданный. В боковом меню выбираем **Веб-сайт**. Далее жмем **Хостинг**, в качестве главной страницы выбираем **index.html** и жмем сохранить. Это нужно для того чтобы S3 сам хостил наши статические файлы, а мы через Nginx просто проксировали все запросы с *.docs.mekstack.ru на этот веб-сайт.
6. Переходим в Репозиторий -> Settings -> Secrets and variables -> Actions.
    - Во вкладке Secrets с помощью кнопки **New repository** secret создаем два секрета, куда вписываем соответственно полученные ранее **acces_key** и **secret_key**:
        - **DIPLODOC_ACCESS_KEY_ID**
        - **DIPLODOC_SECRET_ACCESS_KEY**
    - Во вкладке Variables с помощью кнопки **New repository variable** создаем три переменые:
        - **DIPLODOC_STORAGE_BUCKET** со значением имени бакета, которое вы указали на этапе создания бакета
        - DIPLODOC_STORAGE_ENDPOINT со значением `https://storage.yandexcloud.net`
        - DIPLODOC_STORAGE_REGION со значением `ru-central1`
