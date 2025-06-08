import json
import logging
from dataclasses import asdict

from entity.alart_notification.alart import Alart
from usecase.alart_notification.output_port import AlartNotificationOutputPort

from common.log import context as ctx
from common.log.access_log import RequestIDFilter

access_logger = logging.getLogger("access")


class AlartPresenterMock(AlartNotificationOutputPort):
    '''アラート通知のadapter層のモックプレゼンター
    リクエスト・レスポンス問わず、外部へ通信する用途で呼び出される。
    モックはstdoutへ出力する
    Args:
        AlartNotificationOutputPort : Sendメソッドを持つIF
    '''

    def __init__(self):
        '''コンストラクタ
        stdoutへの出力のため宛先情報は不要である
        '''

    def Send(self, msg: Alart):
        '''送信処理（モック）
        送信の代わりにstdoutへ出力する

        Args:
            msg (dict): 送りたいentity
        '''
        access_logger.addFilter(RequestIDFilter(ctx.request_id_var.get()))
        byte_data = self.MakeMesage(msg)
        access_logger.info(f"notify dummy alart: {byte_data}")

    def MakeMesage(self, msg: Alart) -> bytes:
        '''送信電文を作る

        Args:
            msg (Alart): メッセージ送信用のアラート情報

        Returns:
            bytes: jsonデータのバイト列
        '''
        j = json.dumps(asdict(msg))
        access_logger(f"sending message: {j}")
        return j.encode("utf-8")
