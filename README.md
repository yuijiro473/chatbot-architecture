## 環境構築

## 前提条件
1. **Dockerのインストール:** Dockerがまだインストールされていない場合は、[公式サイト](https://www.docker.com/products/docker-desktop/)からダウンロードし、インストールしてください。

2. **Gitのインストール:** Gitがまだインストールされていない場合は、インストールしてください。

<br>

<h2>1. リポジトリのクローン</h2>
ターミナルで以下のコマンドを実行し、任意のフォルダに対してリポジトリをクローンしてください。

```
git clone https://github.com/yuijiro473/chatbot-architecture
```

<br>

<h2>2. Dockerコンテナの起動</h2>
以下のコマンドを実行し、Dockerコンテナを起動してください。

```
cd chatbot-architecture
docker-compose up -d --build
```

<br>

<h2>3. 「Hello,World!」表示の確認</h2>
ブラウザで以下のURLにアクセスしてください。   
<br>
http://localhost:5011
<br><br>
「Hello,World!」が表示されれば成功です。
