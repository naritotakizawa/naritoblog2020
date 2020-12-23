# naritoblog2020

Nuxt.js と Django rest framework で作成した、シンプルなブログです。

## 動かし方

```
git clone https://github.com/naritotakizawa/naritoblog2020
cd naritoblog2020
```

```
vim backend/src/project/settings.py
```

サーバーの IP アドレスを足す(公開しないならば不要)

```python
ALLOWED_HOSTS = ['127.0.0.1', 'backend', 'Add Your IP Address!!']
```

```
docker-compose up
```

〜この辺でコーヒーなどを淹れて待つ〜

http://your-ip にアクセスする（公開しないなら、http://127.0.0.1 にアクセス）

username: admin
password: admin123

でスーパーユーザーが一人作られるので、このユーザーでログインや記事の作成ができます。
