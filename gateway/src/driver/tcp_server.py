import asyncio
import json
import logging
import uuid
from asyncio import StreamReader, StreamWriter

from common.log import context as ctx
from common.log.access_log import RequestIDFilter

access_logger = logging.getLogger("access")
app_logger = logging.getLogger("app")


class TcpServer:
    def __init__(self, host: str, port: int, route_table: dict):
        self._host = host
        self._port = port
        self._route_table = route_table

    async def handle_client(self, request_reader: StreamReader, response_writer: StreamWriter):
        request_id = str(uuid.uuid4())
        ctx.request_id_var.set(request_id)
        access_logger.addFilter(RequestIDFilter(request_id))
        addr = response_writer.get_extra_info('peername')
        access_logger.info(f"Connected from {addr}")
        try:
            while data := await request_reader.read(1024):
                try:
                    text = data.decode()
                    payload = json.loads(text)
                    called_api = payload["api"]
                    controller = self._route_table[called_api]
                    await controller.Execute(payload)
                except Exception as e:
                    access_logger.error(f"exception occur", exc_info=e)
        except asyncio.IncompleteReadError:
            pass
        finally:
            access_logger.info(f"Disconnected: {addr}")
            response_writer.close()
            await response_writer.wait_closed()

    async def run(self):
        server = await asyncio.start_server(self.handle_client, self._host, self._port)
        app_logger.info(f"TCP Server listening on {self._host}:{self._port}")
        async with server:
            await server.serve_forever()
