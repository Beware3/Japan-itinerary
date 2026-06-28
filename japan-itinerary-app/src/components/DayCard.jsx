import { useState, useEffect } from 'react';

export default function DayCard({ day, updateDayData }) {
  const [newSuggestion, setNewSuggestion] = useState('');
  
  // Tag styling based on theme
  const getTagStyle = (tag) => {
    if (tag.toLowerCase().includes('tokyo')) return 'tag-tokyo';
    if (tag.toLowerCase().includes('kyoto')) return 'tag-kyoto';
    if (tag.toLowerCase().includes('osaka')) return 'tag-osaka';
    if (tag.toLowerCase().includes('nara')) return 'tag-nara';
    if (tag.toLowerCase().includes('fuji')) return 'tag-fuji';
    return '';
  };
  
  const getBadgeStyle = (theme) => {
    switch(theme) {
      case 'tokyo': return { background: '#1a2744' };
      case 'kyoto': return { background: '#4a1878' };
      case 'osaka': return { background: '#882010' };
      case 'fuji': return { background: '#C9A84C' };
      default: return { background: '#4a7050' };
    }
  };

  const handleAddSuggestion = (e) => {
    e.preventDefault();
    if (!newSuggestion.trim()) return;
    
    const updatedDay = {
      ...day,
      suggestions: [...(day.suggestions || []), newSuggestion.trim()]
    };
    
    updateDayData(updatedDay);
    setNewSuggestion('');
  };

  const handleUpdateCost = (groupIndex, itemIndex, newCost) => {
    const cost = parseFloat(newCost) || 0;
    const updatedActivities = [...day.activities];
    updatedActivities[groupIndex].items[itemIndex].cost = cost;
    
    updateDayData({
      ...day,
      activities: updatedActivities
    });
  };

  const calculateTotal = () => {
    let total = 0;
    day.activities.forEach(group => {
      group.items.forEach(item => {
        total += item.cost || 0;
      });
    });
    return total;
  };

  return (
    <div className="day-card animate-on-scroll">
      <div className="day-image-wrap">
        <img className="day-image" src={day.image} alt={day.title} loading="lazy" />
        <div className="day-image-overlay"></div>
        <div className="day-image-badge">
          <div className="day-badge-num" style={getBadgeStyle(day.theme)}>{day.dayNumber}</div>
          <span className="day-badge-text">Day {day.dayNumber}</span>
        </div>
        <div className="day-image-caption">
          <h3>{day.title}</h3>
          <p>{day.date}</p>
          <div className="city-tags">
            {day.tags.map((tag, i) => (
              <span key={i} className={`city-tag ${getTagStyle(tag)}`}>{tag}</span>
            ))}
            {day.note && <span className="timing-note" style={{color: 'rgba(255,255,255,0.7)'}}>{day.note}</span>}
          </div>
        </div>
      </div>
      
      <div className="day-body">
        {day.activities.map((group, gIdx) => (
          <div key={gIdx} className="activity-group">
            <div className="group-label">
              <span className="group-label-icon">{group.icon}</span> {group.group}
            </div>
            {group.items.map((item, iIdx) => (
              <div key={iIdx} className="act-item">
                <div>
                  {item.link ? (
                    <a href={item.link} target="_blank" rel="noreferrer">{item.name}</a>
                  ) : (
                    <span>{item.name}</span>
                  )}
                  {item.desc && <span> — {item.desc}</span>}
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span className="cost-badge">¥{item.cost || 0}</span>
                  <button 
                    className="add-cost-btn"
                    onClick={() => {
                      const val = prompt(`Enter cost in ¥ for ${item.name}:`, item.cost || 0);
                      if (val !== null) handleUpdateCost(gIdx, iIdx, val);
                    }}
                  >
                    Edit Cost
                  </button>
                </div>
              </div>
            ))}
          </div>
        ))}
        
        <div className="daily-total">
          <span>Daily Total:</span>
          <span style={{ color: 'var(--red)' }}>¥{calculateTotal().toLocaleString()}</span>
        </div>

        {day.distance && (
          <div className="dist-row">{day.distance}</div>
        )}

        {/* Day-specific suggestions */}
        <div style={{ marginTop: '1.5rem', borderTop: '1px solid var(--border)', paddingTop: '1rem' }}>
          <h4 style={{ fontSize: '0.8rem', color: 'var(--navy)', marginBottom: '0.5rem' }}>Group Suggestions for Day {day.dayNumber}:</h4>
          {day.suggestions && day.suggestions.length > 0 && (
            <div className="sugg-list" style={{ marginBottom: '1rem' }}>
              {day.suggestions.map((s, i) => (
                <div key={i} className="sugg-item" style={{ padding: '0.5rem 0.8rem' }}>
                  <span className="sugg-item-text">{s}</span>
                </div>
              ))}
            </div>
          )}
          <form className="input-area" onSubmit={handleAddSuggestion}>
            <input 
              type="text" 
              placeholder="Suggest an activity or spot for this day..."
              value={newSuggestion}
              onChange={(e) => setNewSuggestion(e.target.value)}
            />
            <button type="submit" className="add-btn">Add</button>
          </form>
        </div>
      </div>
    </div>
  );
}
