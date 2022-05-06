import logging, json
from websocket_server import WebsocketServer
# https://github.com/Pithikos/python-websocket-server

def new_client(client, server): # one ip can have multiple clients (if online)
    print(f"{client['address'][0]} connected and was assigned id {client['id']}")

def new_message(client, server, message):
    print(f"[{client['id']}|{client['address'][0]}] {message}")

    servermsg = {
        "client": {
            "id": client['id'],
            "address": client['address'][0],
            "port": client['address'][1]
        },
        "message": json.loads(message)
    }
    server.send_message_to_all(json.dumps(servermsg))

def client_left(client, server):
    print(f"Client {client['id']} left")

server = WebsocketServer(host='0.0.0.0', port=9876, loglevel=logging.DEBUG)
server.set_fn_new_client(new_client)
server.set_fn_message_received(new_message)
server.set_fn_client_left(client_left)
server.run_forever()