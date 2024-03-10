// App.js

import React, { useEffect } from 'react';
import { initSocket, sendMessage } from './utils/socket';
import CandidateDataGrid from './components/candidateDataGrid'

const App = () => {
  useEffect(() => {
    // Initialize WebSocket connection when component mounts
    initSocket();

    // Clean up WebSocket connection when component unmounts
    return () => {
      initSocket.close();
    };
  }, []);

  const handleClick = () => {
    // Example: Send a message over WebSocket connection
    sendMessage({ type: 'chat', content: 'Hello, server!' });
  };

  return (
    <div>
      <CandidateDataGrid/>
    </div>
  );
};

export default App;
