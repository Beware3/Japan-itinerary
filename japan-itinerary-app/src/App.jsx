import { useState, useEffect } from 'react';
import Hero from './components/Hero';
import StatsBar from './components/StatsBar';
import RouteMap from './components/RouteMap';
import DayCard from './components/DayCard';
import SuggestionBox from './components/SuggestionBox';
import itineraryDataInitial from './data/ItineraryData.json';
import './index.css';

const INITIAL_SUGGESTIONS = [
  { text: '🍣 Tsukiji Outer Market — fresh sushi breakfast, Tokyo (any morning)', meta: 'Food suggestion' },
  { text: '🌿 Philosopher\'s Path — peaceful canal walk lined with cherry trees, Kyoto', meta: 'Nature' },
  { text: '🥢 Nishiki Market — Kyoto\'s famous 5-block covered food market, "Kyoto\'s kitchen"', meta: 'Food' },
  { text: '🎐 Yanaka Ginza — old-Tokyo neighbourhood, pottery, cats & street food (Tokyo)', meta: 'Culture' }
];

export default function App() {
  const [itinerary, setItinerary] = useState([]);
  const [globalSuggestions, setGlobalSuggestions] = useState([]);

  // Load from local storage or initialize
  useEffect(() => {
    const savedItinerary = localStorage.getItem('japanItinerary_days');
    if (savedItinerary) {
      setItinerary(JSON.parse(savedItinerary));
    } else {
      setItinerary(itineraryDataInitial);
    }

    const savedSuggestions = localStorage.getItem('japanItinerary_suggestions');
    if (savedSuggestions) {
      setGlobalSuggestions(JSON.parse(savedSuggestions));
    } else {
      setGlobalSuggestions(INITIAL_SUGGESTIONS);
    }

    // Scroll Observer for animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, i) => {
        if(entry.isIntersecting){
          setTimeout(() => {
            entry.target.classList.add('visible');
          }, i * 80);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

    setTimeout(() => {
      document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
    }, 100);

    return () => observer.disconnect();
  }, []);

  // Save changes to local storage
  const updateDayData = (updatedDay) => {
    const newItinerary = itinerary.map(day => day.id === updatedDay.id ? updatedDay : day);
    setItinerary(newItinerary);
    localStorage.setItem('japanItinerary_days', JSON.stringify(newItinerary));
  };

  const addGlobalSuggestion = (text) => {
    const newSuggestion = { text, meta: 'Just added ✓', new: true };
    const updated = [...globalSuggestions, newSuggestion];
    setGlobalSuggestions(updated);
    localStorage.setItem('japanItinerary_suggestions', JSON.stringify(updated));
  };

  // Back to top button logic
  const [showTopBtn, setShowTopBtn] = useState(false);
  useEffect(() => {
    const handleScroll = () => {
      setShowTopBtn(window.scrollY > 600);
    };
    window.addEventListener('scroll', handleScroll, {passive: true});
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div>
      <Hero />
      <div className="container">
        <StatsBar />
        <RouteMap />
        
        <div className="section-wrap">
          <div className="section-label">Day-by-Day Itinerary</div>
        </div>
        
        <div className="days-grid">
          {itinerary.map((day) => (
            <DayCard key={day.id} day={day} updateDayData={updateDayData} />
          ))}
        </div>

        <SuggestionBox 
          globalSuggestions={globalSuggestions} 
          addGlobalSuggestion={addGlobalSuggestion} 
        />
      </div>

      <div className="footer">
        <div className="footer-brand">日本 2026</div>
        Japan Itinerary 2026 · Group of 5 · Made with ❤ for an unforgettable trip
      </div>

      <button 
        className={`back-top ${showTopBtn ? 'show' : ''}`}
        onClick={() => window.scrollTo({top: 0, behavior: 'smooth'})}
        aria-label="Back to top"
      >
        ↑
      </button>
    </div>
  );
}
