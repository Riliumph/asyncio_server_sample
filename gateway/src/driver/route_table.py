import atexit

from adapter.alart_notification.controller import AlartNotificationController
from driver.message_sender.udp_sender import UdpSender
from usecase.alart_notification.interactor_mock import AlartNotifierMock
from usecase.alart_notification.presenter_mock import AlartPresenterMock

# API内で状態を持つと継続するので注意
# ステートレスなAPIである必要がある
route_table = {
    "alart": AlartNotificationController(AlartNotifierMock(AlartPresenterMock()))
}
