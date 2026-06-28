import { useState } from 'react';

export default function SuggestionBox({ globalSuggestions, addGlobalSuggestion }) {
  const [newSuggestion, setNewSuggestion] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newSuggestion.trim()) return;
    addGlobalSuggestion(newSuggestion.trim());
    setNewSuggestion('');
  };

  return (
    <>
      <div className="section-wrap">
        <div className="section-label">General Suggestions</div>
      </div>
      <div className="suggestion-wrap animate-on-scroll">
        <div className="sugg-card">
          <div className="sugg-icon">✉️</div>
          <h3>Add a general trip suggestion!</h3>
          <p>Have a hidden gem, restaurant, experience, or shopping spot? Drop it below — everyone in the group can add their ideas here.</p>
          <div className="sugg-list">
            {globalSuggestions.map((s, i) => (
              <div key={i} className="sugg-item" style={{ borderColor: s.new ? '#C9A84C' : 'var(--border)' }}>
                <span className="sugg-item-text">{s.text}</span>
                <span className="sugg-item-meta" style={{ color: s.new ? '#C9A84C' : 'var(--muted)' }}>
                  {s.meta}
                </span>
              </div>
            ))}
          </div>
          <form className="input-area" onSubmit={handleSubmit}>
            <input 
              type="text" 
              placeholder="Your suggestion (place, food, experience...)" 
              value={newSuggestion}
              onChange={(e) => setNewSuggestion(e.target.value)}
            />
            <button type="submit" className="add-btn">+ Add</button>
          </form>
        </div>
      </div>
    </>
  );
}
