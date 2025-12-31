# クラウド・シンカー

自身のローカルフォルダの内容をクラウドに同期できる Python スクリプトです。
基本的に `s3 sync` コマンドを叩くだけのラッパーになります。

## 動作方法
1. 以下のパッケージが事前にインストールされている必要があります。

- uv
- aws
- tree
- cron

2. 以下のパスにファイルを配置し、同期するファイルを記載してください。

- ./src/data/sync_path.json
- ./src/data/sync_path_archive.json

```
{
    "<local_path>": "<sync_path>",
    ...
}
```

3. 任意で cron ジョブを設定し、uv コマンドを実行してください。