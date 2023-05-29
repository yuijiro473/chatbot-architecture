# 環境構築

## 前提条件

### Dockerのインストール

1. Docker公式ウェブサイト (https://www.docker.com/) からDocker Desktop for Windowsをダウンロードします。

2. ダウンロードしたインストーラー (`Docker Desktop Installer.exe`) を開きます。

3. インストーラーの指示に従ってDocker Desktopをインストールします。

4. インストールが完了したら、Docker Desktopが自動的に起動します。システムトレイ（タスクバーの右下）にDockerアイコンが表示されれば、Dockerが正常に動作しています。

5. インストールを確認するためにコマンドプロンプトまたはPowerShellを開き、以下のコマンドを入力します：

    ```
    docker version
    ```

    Dockerのバージョン情報が表示されれば、インストールは成功です。

### Gitのインストール

1. Git公式ウェブサイト (https://git-scm.com/) からGit for Windowsをダウンロードします。

2. ダウンロードしたインストーラー (`Git-<version>-64-bit.exe`) を開きます。

3. インストーラーの指示に従ってGitをインストールします。基本的にすべてデフォルトの設定で問題ありませんが、特定の要件がある場合は設定を調整してください。

4. インストールが完了したら、コマンドプロンプトまたはPowerShellを開き、以下のコマンドを入力します：

    ```
    git --version
    ```

    Gitのバージョン情報が表示されれば、インストールは成功です。

<br>

## コンテナの作成

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
