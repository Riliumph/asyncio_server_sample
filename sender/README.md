# sender

gatewayコンテナへリクエストを投げる役割のコンテナ

## 使い方

### コンテナへの入り方

```console
$ docker compose exec -it sender /bin/bash
```

### リクエストの送り方

#### ncatを使う場合

```console
ncat gateway 80 < data.json
```

#### telnetを使う場合

> 予めコンテナに入っておく

```console
# telnet gateway 80
{"api": "alart", "occurence_time": "2025-06-09T01:24:00.000", "severity": "warning", "msg": "server down"}
```
