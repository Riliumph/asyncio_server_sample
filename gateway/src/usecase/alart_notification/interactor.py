import logging

from common.logger import context as ctx
from common.logger.access_log import RequestIDFilter
from entity.alart_notification.alart import Alart
from usecase.alart_notification.input_port import AlartNotificationInputPort
from usecase.alart_notification.output_port import AlartNotificationOutputPort

access_logger = logging.getLogger("access")


class AlartNotifier(AlartNotificationInputPort):
    def __init__(self, o: AlartNotificationOutputPort):
        self._o = o

    def Execute(self, request_msg: Alart):
        access_logger.addFilter(RequestIDFilter(ctx.request_id_var.get()))
        access_logger.info(f"notify alart logic")
        return self._o.Send(request_msg)
