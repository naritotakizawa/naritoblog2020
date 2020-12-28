# naritoblog2020

Nuxt.js と Django rest framework で作成した、シンプルなブログです。

![Screenshot_2020-12-28 frontend](https://user-images.githubusercontent.com/28292340/103190121-f135b580-4912-11eb-9f86-7ca6fda6233f.png)


![Screenshot_2020-12-28 Switchのゲームが沢山あって、どれをやるか決められない](https://user-images.githubusercontent.com/28292340/103190127-f5fa6980-4912-11eb-992f-f3672558082f.png)


## 動かし方

```
git clone https://github.com/naritotakizawa/naritoblog2020
cd naritoblog2020
```

```
vim backend/project/settings.py
```

サーバーの IP アドレスを足す(サーバーではなく、手元の PC で動かしたいなら不要)

```python
ALLOWED_HOSTS = ['127.0.0.1', 'backend', 'Add Your IP Address!!']
```

```
docker-compose up
```

〜この辺でコーヒーなどを淹れて待つ〜

http://your-ip にアクセスする（サーバーではなく、手元の PC で動かしたいならhttp://127.0.0.1 にアクセス）

username: admin
password: admin123

でスーパーユーザーが一人作られるので、このユーザーでログインや記事の作成ができます。
