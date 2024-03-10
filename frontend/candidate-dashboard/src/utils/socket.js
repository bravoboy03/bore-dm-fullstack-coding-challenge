// socket.js

let socket;

export const initSocket = () => {
  // Initialize WebSocket connection
  socket = new WebSocket('ws://localhost:8080'); // Example URL, adjust as needed

  // Handle connection open event
  socket.onopen = () => {
    console.log('WebSocket connection established');
  };

  // Handle incoming messages
  socket.onmessage = (event) => {
    const message = JSON.parse(event.data);
    // Handle incoming message data
  };

  // Handle connection close event
  socket.onclose = () => {
    console.log('WebSocket connection closed');
  };

  // Handle connection error event
  socket.onerror = (error) => {
    console.error('WebSocket connection error:', error);
  };
};

export const sendMessage = (message) => {
  // Send message over WebSocket connection
  socket.send(JSON.stringify(message));
};
