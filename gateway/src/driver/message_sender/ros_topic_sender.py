import asyncio

from driver.message_sender.base_sender import BaseSender


class RosTopicSender(BaseSender):
    '''ROSのトピック通信を行うクラス（WIP）
    通信ノードをもらう必要がある気がする

    Args:
        MessageSender (_type_): _description_
    '''

    def __init__(self, topic_name: str):
        '''コンストラクタ

        Args:
            topic_name (str): 送信先トピック名
        '''
        self._topic_name = topic_name

    async def send(self, data: bytes) -> None:
        '''送信処理（WIP）

        Args:
            data (bytes): 送信データ
        '''
        raise NotImplementedError
