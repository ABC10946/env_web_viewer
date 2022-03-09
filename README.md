# env_web_viewer

気温・湿度・気圧データを取得してグラフにプロットするwebアプリです。

![Screenshot from 2022-03-09 22-14-54](https://user-images.githubusercontent.com/42955848/157448950-56a64f4c-06fc-4c3b-8106-44555c91c42d.png)


# 必須ライブラリ

- Flask


# 運用方法

`web/main.py`と`batch/env_getter_batch.py`の2つのスクリプトをデーモンとして常時稼働させる必要があります。

ここでは`supervisor`を用いた設定例を以下に記載します。

```
[program:envWebViewer]
user=<user>
autostart=true
directory=/path/to/env_web_viewer/web
command=/usr/bin/python3 main.py
redirect_stderr=true
stdout_logfile=/path/to/env_web_viewer/web/envwebview.log
autorestart=true

[program:env_data_getter]
user=<user>
autostart=true
directory=/path/to/Projects/env_web_viewer/batch
command=/path/to/env_web_viewer/env/bin/python env_getter_batch.py
redirect_stderr=true
stdout_logfile=/path/to/env_web_viewer/batch/env_data_getter.log
autorestart=true
```

env_raspberrypiをraspberry pi上で稼働させる必要があります。

https://github.com/ABC10946/env_raspberrypi
