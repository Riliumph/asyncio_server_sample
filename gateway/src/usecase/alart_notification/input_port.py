from abc import ABC

from entity.alart_notification.alart import Alart


class AlartNotificationInputPort(ABC):
    @classmethod
    def Execute(self, request_msg: Alart):
        raise NotImplementedError
