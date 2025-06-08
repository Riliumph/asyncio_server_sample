import argparse
import asyncio
import logging

from common.log import logger
from driver.route_table import route_table
from driver.tcp_server import TcpServer

app_logger = logging.getLogger("app")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="L4 Server with epoll")
    parser.add_argument("--host", type=str, default="0.0.0.0",
                        help="Server host (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=80,
                        help="Server port (default: 80)")
    args = parser.parse_args()
    logger.init("/app/common/log/config.json")

    # TCPサーバーを起動
    server = TcpServer(host=args.host, port=args.port, route_table=route_table)
    asyncio.run(server.run())
