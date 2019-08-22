from mastermind_import import *
from settings import *

if __name__ == "__main__":
    print("Mastermind Server - Ian Mallett")
    print("This computer's IP is \""+mastermind_get_local_ip()+"\".")
    server = Server()
    print("Starting.")
    server.connect(server_ip,port)
    try:
        server.accepting_allow_wait_forever()
    except:
        #Only way to break is with an exception
        pass
    server.accepting_disallow()
    server.disconnect_clients()
    server.disconnect()
