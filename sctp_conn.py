import socket
import sctp

sk = sctp.sctpsocket_tcp(socket.AF_INET)
sk.connect(("127.0.0.1",38412))

print("Sending Message")

sk.sctp_send(msg = "RARI SYSTEMS")
sk.shutdown(0)

sk.close()

