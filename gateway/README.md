# gateway

TCPで接続を受け、別のサーバーへ転送する処理を行う。

## 使い方

特になし。  
dockerで立ち上げると勝手に動き出す

### コンテナへの入り方

```console
$ docker compose exec -it gateway /bin/bash
```

### senderからリクエストを投げた場合

以下のログを生成する

```json
{"asctime": "2025-06-08 18:44:53,440", "filename": "tcp_server.py", "lineno": 25, "funcName": "handle_client", "levelname": "INFO", "request_id": "ba0a78b6-ec83-4906-bf91-519dc1d39771", "message": "Connected from ('172.19.0.2', 51176)"}
{"asctime": "2025-06-08 18:44:53,441", "filename": "controller.py", "lineno": 21, "funcName": "Execute", "levelname": "INFO", "request_id": "ba0a78b6-ec83-4906-bf91-519dc1d39771", "message": "call alart notification api"}
{"asctime": "2025-06-08 18:44:53,441", "filename": "interactor_mock.py", "lineno": 19, "funcName": "Execute", "levelname": "INFO", "request_id": "ba0a78b6-ec83-4906-bf91-519dc1d39771", "message": "Alart notifier works"}
{"asctime": "2025-06-08 18:44:53,441", "filename": "presenter_mock.py", "lineno": 53, "funcName": "MakeMesage", "levelname": "INFO", "request_id": "ba0a78b6-ec83-4906-bf91-519dc1d39771", "message": "sending message: {\"msg\": \"server down\", \"timestamp\": \"2025\\u5e7406\\u670809\\u65e5 01\\u664224\\u520600\\u79d2\", \"severity\": \"warning\"}"}
{"asctime": "2025-06-08 18:44:53,441", "filename": "presenter_mock.py", "lineno": 36, "funcName": "Send", "levelname": "INFO", "request_id": "ba0a78b6-ec83-4906-bf91-519dc1d39771", "message": "notify dummy alart"}
```
