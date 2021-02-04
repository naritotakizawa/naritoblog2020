# naritoblog2020

Nuxt.js と Django rest framework で作成した、シンプルなブログです。

## 動かし方

```
git clone https://github.com/naritotakizawa/naritoblog2020
cd naritoblog2020
```

```
vim docker-compose.yml
```

サーバーの IP アドレスやドメインに書き換える(サーバーではなく、手元の PC で動かしたいなら不要)

```python
ALLOWED_HOSTS=127.0.0.1
↓
ALLOWED_HOSTS=narito.ninja
```

```
docker-compose build
docker-compose up
```

少し待った後、http://IPorDomain にアクセスする（サーバーではなく、手元の PC で動かしたいならhttp://127.0.0.1 にアクセス）

username: admin
password: admin123

でスーパーユーザーが一人作られるので、このユーザーでログインや記事の作成ができます。
