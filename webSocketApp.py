import asyncio
import websockets
from chatbot import chat

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
start_server = websockets.serve(handle_connection, "localhost", 8767)

if __name__ == "__main__":
    print("Bismillah")
    # Asenkron etkinlik döngüsünü başlatma
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()