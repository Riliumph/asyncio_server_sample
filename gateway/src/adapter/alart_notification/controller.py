import asyncio
import logging

from adapter.base_controller import BaseController
from common.logger import context as ctx
from common.logger.access_log import RequestIDFilter
from entity.alart_notification.alart import Alart
from usecase.alart_notification.input_port import AlartNotificationInputPort

app_logger = logging.getLogger("app")
access_logger = logging.getLogger("access")


class AlartNotificationController(BaseController):
    def __init__(self, i: AlartNotificationInputPort):
        self._i = i

    async def Execute(self, msg: dict):
        access_logger.addFilter(RequestIDFilter(ctx.request_id_var.get()))
        access_logger.info("call alart notification api")
        alart = Alart(**msg)
        self._i.Execute(request_msg=alart)
