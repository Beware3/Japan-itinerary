import { useEffect, useState } from 'react';

export default function Hero() {
  const [scrollY, setScrollY] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      setScrollY(window.scrollY);
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div className="hero" id="top">
      <div 
        className="hero-bg" 
        style={{ transform: `scale(1.05) translateY(${scrollY * 0.3}px)` }}
      ></div>
      <div className="hero-overlay"></div>
      <div className="hero-content">
        <div className="hero-jp">日本旅行 二〇二六</div>
        <h1 className="hero-title">Japan <span>🌸</span> Itinerary</h1>
        <div className="hero-divider"></div>
        <div className="hero-dates">✈  29 August – 8 September 2026</div>
        <div className="hero-meta">Group of 5 · 10 Days · Washi-paper thin plans, bold adventures</div>
        <div className="hero-cities">
          <span className="hero-city">✈ Tokyo</span>
          <span className="hero-city">⛩ Kyoto</span>
          <span className="hero-city">🍜 Osaka</span>
          <span className="hero-city">🦌 Nara</span>
          <span className="hero-city">🗻 Mt. Fuji</span>
          <span className="hero-city">🌊 Amanohashidate</span>
        </div>
      </div>
      <div className="scroll-hint">Scroll to explore</div>
    </div>
  );
}
