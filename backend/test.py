import websocket

# Define WebSocket URL
ws_url = "ws://localhost:5000"

# Define headers (if needed)
headers = {
    "SECRET_KEY": "bravoboyRocks",
    "User-Agent": "WebSocketClient"
}

# Connect to WebSocket server
ws = websocket.create_connection(ws_url, header=headers)

# Send a message
ws.send("Hello, WebSocket!")

# Receive a message
response = ws.recv()
print("Received:", response)

# Close the WebSocket connection
ws.close()
