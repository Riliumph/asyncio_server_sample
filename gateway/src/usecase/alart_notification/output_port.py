from abc import ABC


class AlartNotificationOutputPort(ABC):
    '''アラート通知のadapter層のOutputPort（抽象）クラス
    外部へ通信する用途のインターフェイスを定義している。

    Args:
        ABC (_type_): 抽象クラスを明示

    Raises:
        NotImplementedError: 具象クラスでは必ず実装される必要がある
    '''
    @classmethod
    def Send(self, msg: dict):
        raise NotImplementedError
