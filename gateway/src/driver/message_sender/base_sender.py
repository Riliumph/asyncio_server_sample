from abc import ABC


class BaseSender(ABC):
    '''メッセージ送信の抽象クラス
    あらゆる送信処理を抽象化する役割を持つ。
    Args:
        ABC (_type_): 抽象クラスを明示

    Raises:
        NotImplementedError: 具象クラスでは必ず実装される必要がある
    '''
    @classmethod
    def send(self, data: bytes):
        '''送信処理（純粋仮想関数）
        Args:
            data (bytes): 送りたいデータ
        '''
        raise NotImplementedError
