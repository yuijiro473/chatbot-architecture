## 環境構築

<h2>前提: Dockerのインストール</h2>
Dockerがインストールされていない場合のみ、以下の公式サイトからダウンロードしてください。

https://www.docker.com/products/docker-desktop/

<br>

<h2>1. リポジトリのクローン</h2>
ターミナルで以下のコマンドを実行し、任意のフォルダに対してリポジトリをクローンしてください。

```
git clone https://github.com/yuijiro473/chatbot-architect 
```

<br>

<h2>2. Dockerコンテナの起動</h2>
以下のコマンドを実行し、Dockerコンテナを起動してください。

```
docker-compose up -d --build
```

<br>

<h2>3. 「Hello,World!」表示の確認</h2>
ブラウザで以下のURLにアクセスしてください。   
<br>
http://localhost:5000
<br><br>
「Hello,World!」が表示されれば成功です。（お疲れ様でした！）
