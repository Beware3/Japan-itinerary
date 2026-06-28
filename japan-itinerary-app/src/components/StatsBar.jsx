export default function StatsBar() {
  return (
    <div className="section-wrap">
      <div className="section-label">Trip Overview</div>
      <div className="stats-bar">
        <div className="stat-card animate-on-scroll">
          <div className="stat-num accent">10</div>
          <div className="stat-label">Days</div>
        </div>
        <div className="stat-card animate-on-scroll">
          <div className="stat-num">6</div>
          <div className="stat-label">Cities</div>
        </div>
        <div className="stat-card animate-on-scroll">
          <div className="stat-num">5</div>
          <div className="stat-label">Travellers</div>
        </div>
        <div className="stat-card animate-on-scroll">
          <div className="stat-num">~1,200</div>
          <div className="stat-label">km covered</div>
        </div>
      </div>
    </div>
  );
}
