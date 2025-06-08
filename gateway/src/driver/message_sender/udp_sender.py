import asyncio

from driver.message_sender.base_sender import BaseSender


class UdpSender(BaseSender):
    '''UDPでメッセージを送信するクラス
    排他処理は行っていないので注意
    '''

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._transport = None

    async def setup(self):
        '''非同期setup
        非同期関数のため同期関数であるコンストラクタで使用禁止
        UDP用のソケットを使いまわすために１度だけ実行する
        '''
        if self._transport is not None and not self._transport.is_closing():
            print(f"socket is alive")
            return
        loop = asyncio.get_running_loop()
        self._transport, _ = await loop.create_datagram_endpoint(
            lambda: asyncio.DatagramProtocol(),
            remote_addr=(self._host, self._port)
        )

    async def send(self, data: bytes) -> None:
        if self._transport is None or self._transport.is_closing():
            self.setup()
        self._transport.sendto(data)

    def close(self):
        if self._transport:
            self._transport.close()
            print("udp sender closed")
