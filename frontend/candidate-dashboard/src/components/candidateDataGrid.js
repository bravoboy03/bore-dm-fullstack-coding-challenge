import { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { initSocket, sendMessage } from '../utils/socket';

const columns = [
  { field: 'id', headerName: 'ID', width: 100 },
  { field: 'firstName', headerName: 'First Name', width: 150 },
  // Add other columns as needed
];

function CandidateDataGrid() {
  const [candidates, setCandidates] = useState([]);

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
}

  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid rows={candidates} columns={columns} pageSize={5} />
    </div>
  );
}

export default CandidateDataGrid;




