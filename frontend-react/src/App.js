import React, { useState } from 'react';

function App() {
  const [cities, setCities] = useState('');
  const [result, setResult] = useState(null);

  const search = async () => {
    const response = await fetch(`http://localhost:8000/weather-multiple?cities=${cities}`);
    const data = await response.json();
    setResult(data);
  };

  return (
    <div style={{padding: '20px'}}>
      <h1>Weather Tracker</h1>
      <input value={cities} onChange={(e) => setCities(e.target.value)} placeholder="City" />
      <button onClick={search}>Search</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}

export default App;
