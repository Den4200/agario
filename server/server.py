from pathlib import Path
import socket
import time

from frost import FrostServer
from frost.server import logger
from frost.server.socketio.base_server import ConnectionData

from server.agario import Agario
from server.scheduler import Scheduler


class Server(FrostServer):

    def __init__(self, file: str) -> None:
        db = Path('pyfrost.sqlite3')
        if not db.exists():
            from server.utils import init_db
            init_db()

        super().__init__(file)

        # Load up cogs
        Agario()

    def start(self) -> None:
        """Starts the threaded, multi-client server.
        """
        try:
            self._socket.bind((self.ip, self.port))

        except socket.error as e:
            print(e)

        else:
            self._socket.listen()
            logger.info('Server is online!')

            run = True
            while run:
                conn_data = ConnectionData()
                self._accept_conn(conn_data)

                prev = time.time()

                # Makes the server stoppable
                while conn_data.conn is None or conn_data.addr is None:
                    try:
                        now = time.time()
                        Scheduler.collect(now - prev)
                        prev = now

                        time.sleep(0.1)
                    except KeyboardInterrupt:
                        run = False
                        break

                conn, addr = conn_data.conn, conn_data.addr
                logger.info(f'Connection established to {addr}')

                if self.func is not None:
                    self.func(conn, addr)
