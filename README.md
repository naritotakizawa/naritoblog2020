# naritoblog2020

Nuxt.js と Django rest framework で作成した、シンプルなブログです。

TOPページ

![Screenshot_2020-12-28 frontend](https://user-images.githubusercontent.com/28292340/103190121-f135b580-4912-11eb-9f86-7ca6fda6233f.png)


記事ページ

![Screenshot_2020-12-28 Switchのゲームが沢山あって、どれをやるか決められない](https://user-images.githubusercontent.com/28292340/103190127-f5fa6980-4912-11eb-992f-f3672558082f.png)


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
