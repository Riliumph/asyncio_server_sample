import json
import logging
from dataclasses import asdict

from common.logger import context as ctx
from common.logger.access_log import RequestIDFilter
from driver.message_sender.base_sender import BaseSender
from entity.alart_notification.alart import Alart
from usecase.alart_notification.output_port import AlartNotificationOutputPort

access_logger = logging.getLogger("access")


class AlartNotifierPresenter(AlartNotificationOutputPort):
    def __init__(self, sender: BaseSender):
        self._sender = sender

    def Send(self, msg: Alart):
        '''送信処置
        送信自体はコンストラクタで受け取りsenderクラスに行わせる。
        ここでは実際に送信が行われるまでの準備処理が行われる。
        - 送信電文の作成
        - 通信相手の生死確認
        - セキュリティチェック
        - etc...
        Args:
            msg (Alart): 送信を予定しているエンティティ
        '''
        access_logger.addFilter(RequestIDFilter(ctx.request_id_var.get()))
        byte_data = self.MakeMesage(msg)
        self._sender.send(byte_data)

    def MakeMesage(self, msg: Alart) -> bytes:
        '''送信電文を作る

        Args:
            msg (Alart): メッセージ送信用のアラート情報

        Returns:
            bytes: jsonデータのバイト列
        '''
        j = json.dumps(asdict(msg))
        access_logger(f"send message: {j}")
        return j.encode("utf-8")
