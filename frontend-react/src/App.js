import React, { useState } from 'react';

function App() {
  const [cities, setCities] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const search = async () => {
    if (!cities.trim()) {
      setError('Please enter at least one city');
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await fetch(`http://127.0.0.1:8000/weather-multiple?cities=${cities}`);
      
      if (!response.ok) {
        throw new Error('Failed to fetch weather data');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError('Failed to fetch weather data. Make sure the backend is running.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setCities('');
    setResult(null);
    setError('');
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      search();
    }
  };

  return (
    <div style={styles.pageWrapper}>
      {/* Hero Section */}
      <div style={styles.heroSection}>
        <div style={styles.heroContent}>
          <h1 style={styles.mainTitle}>🌍 Weather Tracker</h1>
          <p style={styles.mainSubtitle}>Real-time Global Weather Data</p>
          
          <div style={styles.descriptionBox}>
            <p style={styles.descriptionText}>
              Welcome to Weather Tracker - your ultimate destination for real-time weather information from cities around the world. 
              Whether you're planning a trip, checking conditions for work, or just curious about the weather, 
              we've got you covered with accurate, up-to-date data.
            </p>
          </div>
        </div>
      </div>

      {/* Search Section */}
      <div style={styles.searchContainer}>
        <h2 style={styles.searchTitle}>Start Exploring Weather</h2>
        <p style={styles.searchSubtitle}>
          Enter one or multiple cities separated by commas (e.g., "Paris, Tokyo, New York")
        </p>

        <div style={styles.searchSection}>
          <input
            type="text"
            placeholder="e.g., Stockholm, Tokyo, Paris"
            value={cities}
            onChange={(e) => setCities(e.target.value)}
            onKeyPress={handleKeyPress}
            style={styles.input}
          />
          <button onClick={search} style={styles.searchBtn}>
            {loading ? 'Searching...' : 'Search'}
          </button>
          <button onClick={handleClear} style={styles.clearBtn}>
            Clear
          </button>
        </div>
      </div>

      {/* Results Section */}
      <div style={styles.resultsContainer}>
        {loading && (
          <div style={styles.loadingBox}>
            <div style={styles.spinner}></div>
            <p style={styles.loadingText}>Fetching weather data...</p>
          </div>
        )}

        {error && (
          <div style={styles.errorBox}>
            <p style={styles.errorIcon}>⚠️</p>
            <p style={styles.errorText}>{error}</p>
          </div>
        )}

        {result && result.weather_data && result.weather_data.length > 0 ? (
          <div style={styles.resultsSection}>
            <h2 style={styles.resultsTitle}>
              Weather for {result.weather_data.length} {result.weather_data.length === 1 ? 'City' : 'Cities'}
            </h2>
            <div style={styles.weatherGrid}>
              {result.weather_data.map((item, index) => (
                <div key={index} style={styles.weatherCard}>
                  <div style={styles.cardHeader}>
                    <h3 style={styles.cityName}>{item[1]}</h3>
                    <span style={styles.tempBadge}>{item[0]}°C</span>
                  </div>
                  
                  <div style={styles.cardBody}>
                    <div style={styles.tempDisplay}>
                      <span style={styles.tempValue}>{item[0]}</span>
                      <span style={styles.tempUnit}>°C</span>
                    </div>
                    
                    <div style={styles.weatherInfo}>
                      <div style={styles.infoItem}>
                        <span style={styles.infoLabel}>📅 Date</span>
                        <span style={styles.infoValue}>{item[2]}</span>
                      </div>
                      <div style={styles.infoItem}>
                        <span style={styles.infoLabel}>🌡️ Temperature</span>
                        <span style={styles.infoValue}>{item[0]}°C</span>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ) : (
          result && (
            <div style={styles.noDataBox}>
              <p style={styles.noDataIcon}>🔍</p>
              <p style={styles.noDataText}>No weather data found. Please try another city.</p>
            </div>
          )
        )}
      </div>

      {/* Footer */}
      <div style={styles.footer}>
        <p style={styles.footerText}>Weather Tracker © 2025 | Real-time weather data for the world</p>
      </div>
    </div>
  );
}

// Stilar
const styles = {
  pageWrapper: {
    minHeight: '100vh',
    background: 'linear-gradient(135deg, #0a0e27 0%, #151a2f 50%, #0d1425 100%)',
    color: '#ffffff',
    fontFamily: "'Poppins', Arial, sans-serif",
    paddingBottom: '50px',
  },

  heroSection: {
    padding: '60px 20px',
    textAlign: 'center',
    background: 'linear-gradient(180deg, rgba(0, 212, 255, 0.1) 0%, transparent 100%)',
    borderBottom: '2px solid rgba(0, 212, 255, 0.2)',
  },

  heroContent: {
    maxWidth: '900px',
    margin: '0 auto',
  },

  mainTitle: {
    fontSize: '4rem',
    fontWeight: '800',
    background: 'linear-gradient(135deg, #00d4ff 0%, #0099cc 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    marginBottom: '10px',
    letterSpacing: '-1px',
  },

  mainSubtitle: {
    fontSize: '1.3rem',
    color: '#a0aec0',
    marginBottom: '30px',
    fontWeight: '300',
  },

  descriptionBox: {
    background: 'rgba(31, 39, 73, 0.4)',
    border: '2px solid rgba(0, 212, 255, 0.2)',
    borderRadius: '12px',
    padding: '25px',
    marginBottom: '30px',
    backdropFilter: 'blur(10px)',
  },

  descriptionText: {
    fontSize: '1.05rem',
    lineHeight: '1.6',
    color: '#cbd5e1',
    margin: '0',
  },

  searchContainer: {
    maxWidth: '900px',
    margin: '50px auto 0',
    padding: '40px 20px',
    textAlign: 'center',
  },

  searchTitle: {
    fontSize: '2.2rem',
    marginBottom: '10px',
    color: '#00d4ff',
    fontWeight: '700',
  },

  searchSubtitle: {
    fontSize: '1rem',
    color: '#a0aec0',
    marginBottom: '30px',
  },

  searchSection: {
    display: 'flex',
    gap: '12px',
    marginBottom: '15px',
    flexWrap: 'wrap',
    justifyContent: 'center',
  },

  input: {
    padding: '14px 20px',
    fontSize: '1rem',
    border: '2px solid #2d3748',
    borderRadius: '10px',
    backgroundColor: '#1f2749',
    color: '#ffffff',
    minWidth: '350px',
    fontFamily: "'Poppins', Arial",
    transition: 'all 0.3s ease',
    outline: 'none',
    backdropFilter: 'blur(10px)',
  },

  searchBtn: {
    padding: '14px 28px',
    fontSize: '1rem',
    backgroundColor: '#00d4ff',
    border: 'none',
    borderRadius: '10px',
    color: '#000',
    fontWeight: '700',
    cursor: 'pointer',
    transition: 'all 0.3s ease',
    fontFamily: "'Poppins', Arial",
    textTransform: 'uppercase',
    letterSpacing: '0.5px',
  },

  clearBtn: {
    padding: '14px 28px',
    fontSize: '1rem',
    backgroundColor: 'rgba(31, 39, 73, 0.6)',
    border: '2px solid #2d3748',
    borderRadius: '10px',
    color: '#a0aec0',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.3s ease',
    fontFamily: "'Poppins', Arial",
    textTransform: 'uppercase',
    letterSpacing: '0.5px',
  },

  resultsContainer: {
    maxWidth: '1100px',
    margin: '40px auto',
    padding: '0 20px',
  },

  loadingBox: {
    textAlign: 'center',
    padding: '60px 20px',
  },

  spinner: {
    width: '50px',
    height: '50px',
    border: '4px solid rgba(0, 212, 255, 0.2)',
    borderTop: '4px solid #00d4ff',
    borderRadius: '50%',
    animation: 'spin 1s linear infinite',
    margin: '0 auto 20px',
  },

  loadingText: {
    fontSize: '1.1rem',
    color: '#a0aec0',
  },

  errorBox: {
    background: 'rgba(239, 68, 68, 0.1)',
    border: '2px solid #ef4444',
    borderRadius: '12px',
    padding: '30px',
    textAlign: 'center',
    backdropFilter: 'blur(10px)',
  },

  errorIcon: {
    fontSize: '2.5rem',
    marginBottom: '10px',
  },

  errorText: {
    color: '#fca5a5',
    fontSize: '1.05rem',
    margin: '0',
  },

  resultsSection: {
    animation: 'fadeIn 0.5s ease-out',
  },

  resultsTitle: {
    fontSize: '1.8rem',
    marginBottom: '30px',
    color: '#00d4ff',
    textAlign: 'center',
  },

  weatherGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))',
    gap: '25px',
  },

  weatherCard: {
    background: 'linear-gradient(135deg, rgba(31, 39, 73, 0.5) 0%, rgba(25, 32, 60, 0.3) 100%)',
    border: '2px solid #2d3748',
    borderRadius: '16px',
    padding: '25px',
    transition: 'all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)',
    cursor: 'pointer',
    backdropFilter: 'blur(10px)',
    overflow: 'hidden',
  },

  cardHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '20px',
  },

  cityName: {
    fontSize: '1.8rem',
    color: '#00d4ff',
    margin: '0',
    fontWeight: '700',
  },

  tempBadge: {
    background: 'rgba(0, 212, 255, 0.2)',
    border: '2px solid #00d4ff',
    color: '#00d4ff',
    padding: '8px 15px',
    borderRadius: '20px',
    fontWeight: '700',
    fontSize: '0.95rem',
  },

  cardBody: {
    padding: '20px 0',
  },

  tempDisplay: {
    textAlign: 'center',
    marginBottom: '25px',
  },

  tempValue: {
    fontSize: '3.5rem',
    fontWeight: '800',
    color: '#ffffff',
    lineHeight: '1',
  },

  tempUnit: {
    fontSize: '1.5rem',
    color: '#00d4ff',
    fontWeight: '600',
    marginLeft: '5px',
  },

  weatherInfo: {
    display: 'grid',
    gap: '15px',
  },

  infoItem: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '12px',
    background: 'rgba(0, 212, 255, 0.05)',
    borderRadius: '8px',
    border: '1px solid rgba(0, 212, 255, 0.1)',
  },

  infoLabel: {
    color: '#a0aec0',
    fontSize: '0.95rem',
    fontWeight: '500',
  },

  infoValue: {
    color: '#00d4ff',
    fontWeight: '700',
    fontSize: '0.95rem',
  },

  noDataBox: {
    textAlign: 'center',
    padding: '80px 20px',
    background: 'rgba(31, 39, 73, 0.3)',
    borderRadius: '16px',
    border: '2px dashed rgba(0, 212, 255, 0.2)',
  },

  noDataIcon: {
    fontSize: '3rem',
    marginBottom: '15px',
  },

  noDataText: {
    color: '#a0aec0',
    fontSize: '1.1rem',
    margin: '0',
  },

  footer: {
    textAlign: 'center',
    padding: '30px 20px',
    borderTop: '2px solid rgba(0, 212, 255, 0.2)',
    marginTop: '50px',
    background: 'rgba(31, 39, 73, 0.2)',
  },

  footerText: {
    color: '#a0aec0',
    fontSize: '0.95rem',
    margin: '0',
  },
};

export default App;