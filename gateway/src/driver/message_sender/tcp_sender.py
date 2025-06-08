import asyncio

from driver.message_sender.base_sender import BaseSender


class TcpSender(BaseSender):
    '''TCPでメッセージを送信するクラス
    排他処理は行っていないので注意
    '''

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._writer: asyncio.StreamWriter | None = None

    async def setup(self):
        '''非同期setup
        非同期関数のため同期関数であるコンストラクタで使用禁止
        TCP接続を再利用するために１度だけ実行する
        '''
        if self._writer is not None and not self._writer.is_closing():
            print(f"TCP connection is alive")
            return
        reader, writer = await asyncio.open_connection(self._host, self._port)
        self._writer = writer

    async def send(self, data: bytes) -> None:
        if self._writer is None or self._writer.is_closing():
            await self.setup()
        self._writer.write(data)
        await self._writer.drain()

    def close(self):
        if self._writer:
            self._writer.close()
            print("tcp sender closed")
