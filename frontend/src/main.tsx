// src/main.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';

function App() {
  const [status, setStatus] = React.useState<string>('loading');

  React.useEffect(() => {
    fetch('http://127.0.0.1:8000/health')
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus('error'));
  }, []);

  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: '2rem' }}>
      <h1>TokenScope Dashboard (Phase 1)</h1>
      <p>Backend health: <strong>{status}</strong></p>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
