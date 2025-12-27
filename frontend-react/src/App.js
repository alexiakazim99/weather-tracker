import React, { useState } from 'react';

function App() {
  const [cities, setCities] = useState(''); // State för städer som användaren skriver
  const [result, setResult] = useState(null); // State för väderdata från backend
  const [loading, setLoading] = useState(false); // State för loading-status
  const [error, setError] = useState(''); // State för felmeddelanden

  const search = async () => {
    // Funktion som hämtar väderdata när användaren klickar Search
    
    if (!cities.trim()) {
      // Kontrollera om användaren skrev något
      setError('Please enter at least one city');
      return;
    }

    setLoading(true); // Sätt loading till true
    setError(''); // Rensa gamla felmeddelanden
    setResult(null); // Rensa gamla resultat

    try {
      // Gör en fetch-förfrågan till backend
      const response = await fetch(`http://localhost:8000/weather-multiple?cities=${cities}`);
      
      if (!response.ok) {
        // Om svaret inte är OK (200), kasta ett fel
        throw new Error('Failed to fetch weather data');
      }

      const data = await response.json(); // Konvertera svaret till JSON
      setResult(data); // Spara resultatet i state
    } catch (err) {
      // Om något gick fel, visa felmeddelande
      setError('Failed to fetch weather data. Make sure the backend is running.');
      console.error(err);
    } finally {
      // Sätt loading till false när förfrågan är klar (lyckat eller misslyckat)
      setLoading(false);
    }
  };

  const handleClear = () => {
    // Funktion för Clear-knappen
    setCities(''); // Rensa input
    setResult(null); // Rensa resultat
    setError(''); // Rensa felmeddelanden
  };

  const handleKeyPress = (e) => {
    // Tillåt att användaren trycker Enter för att söka
    if (e.key === 'Enter') {
      search();
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🌍 Weather Tracker</h1>
      <p style={styles.subtitle}>Real-time global weather data</p>

      <div style={styles.searchSection}>
        <input
          type="text"
          placeholder="Enter cities (e.g., Stockholm, Tokyo, Paris)"
          value={cities}
          onChange={(e) => setCities(e.target.value)} // Uppdatera state när användaren skriver
          onKeyPress={handleKeyPress} // Tillåt Enter-tangent för sökning
          style={styles.input}
        />
        <button onClick={search} style={styles.searchBtn}>
          Search
        </button>
        <button onClick={handleClear} style={styles.clearBtn}>
          Clear
        </button>
      </div>

      {loading && <p style={styles.loading}>Loading weather data...</p>}

      {error && <p style={styles.error}>{error}</p>}

      {result && result.weather_data && result.weather_data.length > 0 ? (
        <div style={styles.weatherGrid}>
          {result.weather_data.map((item, index) => (
            <div key={index} style={styles.weatherCard}>
              <h3 style={styles.cityName}>{item[1]}</h3>
              <p style={styles.temperature}>{item[0]}°C</p>
              <p style={styles.date}>Date: {item[2]}</p>
            </div>
          ))}
        </div>
      ) : (
        result && <p style={styles.noData}>No weather data found. Please try another city.</p>
      )}
    </div>
  );
}

// Stilar för appen
const styles = {
  container: {
    padding: '30px 20px',
    maxWidth: '1200px',
    margin: '0 auto',
    fontFamily: 'Arial, sans-serif',
    backgroundColor: '#0a0e27',
    minHeight: '100vh',
    color: '#ffffff',
  },
  title: {
    fontSize: '3rem',
    textAlign: 'center',
    marginBottom: '10px',
    color: '#00d4ff',
  },
  subtitle: {
    textAlign: 'center',
    color: '#a0aec0',
    marginBottom: '30px',
    fontSize: '1.1rem',
  },
  searchSection: {
    display: 'flex',
    gap: '10px',
    marginBottom: '30px',
    justifyContent: 'center',
    flexWrap: 'wrap',
  },
  input: {
    padding: '12px 16px',
    fontSize: '1rem',
    border: '2px solid #2d3748',
    borderRadius: '8px',
    backgroundColor: '#1f2749',
    color: '#ffffff',
    minWidth: '300px',
    cursor: 'text',
  },
  searchBtn: {
    padding: '12px 24px',
    fontSize: '1rem',
    backgroundColor: '#00d4ff',
    border: 'none',
    borderRadius: '8px',
    color: '#000',
    fontWeight: 'bold',
    cursor: 'pointer',
  },
  clearBtn: {
    padding: '12px 24px',
    fontSize: '1rem',
    backgroundColor: '#2d3748',
    border: '2px solid #2d3748',
    borderRadius: '8px',
    color: '#a0aec0',
    fontWeight: 'bold',
    cursor: 'pointer',
  },
  loading: {
    textAlign: 'center',
    color: '#00d4ff',
    fontSize: '1.2rem',
    marginTop: '20px',
  },
  error: {
    textAlign: 'center',
    color: '#ef4444',
    fontSize: '1.1rem',
    backgroundColor: 'rgba(239, 68, 68, 0.1)',
    padding: '15px',
    borderRadius: '8px',
    marginTop: '20px',
    border: '2px solid #ef4444',
  },
  noData: {
    textAlign: 'center',
    color: '#a0aec0',
    fontSize: '1.1rem',
    marginTop: '20px',
  },
  weatherGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
    gap: '20px',
    marginTop: '30px',
  },
  weatherCard: {
    backgroundColor: '#1f2749',
    border: '2px solid #2d3748',
    borderRadius: '12px',
    padding: '20px',
    textAlign: 'center',
    transition: 'all 0.3s ease',
    cursor: 'pointer',
  },
  cityName: {
    fontSize: '1.8rem',
    color: '#00d4ff',
    marginBottom: '10px',
  },
  temperature: {
    fontSize: '2.5rem',
    fontWeight: 'bold',
    color: '#ffffff',
    margin: '10px 0',
  },
  date: {
    color: '#a0aec0',
    fontSize: '0.95rem',
  },
};

export default App;