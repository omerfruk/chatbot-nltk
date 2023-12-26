import asyncio
import websockets
from chatbot import chat
import os
import signal
import sys
import webbrowser

async def handle_connection(websocket, path):
    # Yeni bir bağlantı kurulduğunda bu fonksiyon çalışacak
    try:
        while True:
            # Gelen mesajı bekliyoruz
            message = await websocket.recv()
            print(f"Client message: {message}")

            # Gelen mesajı geri gönderiyoruz
            await websocket.send(f"Bot: {chat(message)}")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")


# WebSocket sunucusunu başlatma
start_server = websockets.serve(handle_connection, "localhost", 8766)

def my_signal_handler(*args):
    if os.environ.get('RUN_MAIN') == 'true':
        print('stopped'.upper())
    print('exiting'.upper())
    sys.exit(0)



if __name__ == "__main__":
    print("Bismillah")
    mevcut_dizin = os.getcwd()
    html_dosya_adi = "template/chat.html"
    html_dosya_yolu = os.path.join(mevcut_dizin, html_dosya_adi)
    webbrowser.open('file://' + html_dosya_yolu, new=2)

    signal.signal(signal.SIGINT, my_signal_handler)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


