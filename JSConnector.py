import asyncio
import websockets
from multiprocessing import Process, Pipe
import json
    

async def main(ws, path):
    while True:
        message = main.CONN.recv()
        await ws.send(json.dumps(message)) 
    

def run(port, child_conn):
    main.CONN = child_conn
    start_server = websockets.serve(main, 'localhost', port)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.run_forever()


def send(message = None):
    try:
        send.CONN.send(message)
    except NameError:
        print("Server must be started before sending")


def stop():
    stop.p.terminate()
    stop.p = None


def start(port=5555):
    try:
        stop()
    except:
        pass

    parent_conn, child_conn = Pipe()
    send.CONN = parent_conn
    p = Process(target=run, args=(port, child_conn))
    stop.p = p
    p.start()
