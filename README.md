# READ ME (Free5GC_sctp_connection)
code is configured by default to establish a connection between RAN and AMF of Free5GC using pysctp 

#Requirements :
    Free 5GC,
    python2(2.7),
    pysctp (including installed dependencies),

Procedure:
start: 
    Wireshark,
    AMF on Free5GC (./bin/amf),
    sctp_conn.py (python sctp_conn.py),

Verify:
Port nos,
message received on sctp_conn.py (SENDING MESSAGE),
message/DATA received by AMF on Wireshark (RARI SYSTEMS),

