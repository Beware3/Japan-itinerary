export default function RouteMap() {
  return (
    <div className="section-wrap">
      <div className="section-label">Route Map</div>
      <div className="map-wrap animate-on-scroll">
        <svg className="route-svg" viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <marker id="arr-red" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
              <path d="M0,0 L7,3.5 L0,7 Z" fill="#C8102E" opacity="0.75"/>
            </marker>
            <marker id="arr-gold" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
              <path d="M0,0 L7,3.5 L0,7 Z" fill="#C9A84C" opacity="0.8"/>
            </marker>
            <marker id="arr-sage" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
              <path d="M0,0 L7,3.5 L0,7 Z" fill="#5a7c5e" opacity="0.8"/>
            </marker>
            <marker id="arr-green" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
              <path d="M0,0 L7,3.5 L0,7 Z" fill="#1a5228" opacity="0.8"/>
            </marker>
          </defs>
          <rect width="700" height="260" fill="#FDF6EC" rx="12"/>
          <text x="350" y="18" textAnchor="middle" fontSize="9" fill="#c4b89a" fontFamily="Inter" letterSpacing="3" fontWeight="500">JAPAN   日 本</text>
          
          <circle cx="590" cy="90" r="34" fill="#1a2744"/>
          <text x="590" y="85" textAnchor="middle" fontSize="9.5" fill="#fff" fontFamily="Inter" fontWeight="600" letterSpacing="0.5">TOKYO</text>
          <text x="590" y="97" textAnchor="middle" fontSize="7" fill="rgba(255,255,255,0.55)" fontFamily="Inter">Aug 30–Sep 2</text>
          <text x="590" y="107" textAnchor="middle" fontSize="7" fill="rgba(255,255,255,0.55)" fontFamily="Inter">Sep 5–8</text>
          
          <circle cx="360" cy="120" r="30" fill="#4a1878"/>
          <text x="360" y="115" textAnchor="middle" fontSize="9.5" fill="#fff" fontFamily="Inter" fontWeight="600" letterSpacing="0.5">KYOTO</text>
          <text x="360" y="127" textAnchor="middle" fontSize="7" fill="rgba(255,255,255,0.55)" fontFamily="Inter">Sep 1–5</text>
          
          <circle cx="200" cy="170" r="25" fill="#882010"/>
          <text x="200" y="165" textAnchor="middle" fontSize="9" fill="#fff" fontFamily="Inter" fontWeight="600">OSAKA</text>
          <text x="200" y="177" textAnchor="middle" fontSize="7" fill="rgba(255,255,255,0.55)" fontFamily="Inter">Sep 2 (day)</text>
          
          <circle cx="460" cy="185" r="22" fill="#1a5228"/>
          <text x="460" y="181" textAnchor="middle" fontSize="8.5" fill="#fff" fontFamily="Inter" fontWeight="600">NARA</text>
          <text x="460" y="191" textAnchor="middle" fontSize="7" fill="rgba(255,255,255,0.55)" fontFamily="Inter">Sep 1 (day)</text>
          
          <ellipse cx="108" cy="90" rx="46" ry="22" fill="#4a7050"/>
          <text x="108" y="86" textAnchor="middle" fontSize="7.5" fill="#fff" fontFamily="Inter" fontWeight="600">AMANOHASHIDATE</text>
          <text x="108" y="98" textAnchor="middle" fontSize="7" fill="rgba(255,255,255,0.55)" fontFamily="Inter">Sep 5 (day)</text>
          
          <polygon points="590,185 610,230 570,230" fill="#C9A84C" opacity="0.9"/>
          <text x="590" y="218" textAnchor="middle" fontSize="7.5" fill="#fff" fontFamily="Inter" fontWeight="600">MT. FUJI</text>
          <text x="590" y="240" textAnchor="middle" fontSize="7" fill="#7a6f5e" fontFamily="Inter">Sep 7 (day)</text>
          
          <path d="M 558,100 Q 475,70 390,112" stroke="#C8102E" strokeWidth="2" fill="none" strokeDasharray="6,4" opacity="0.65" markerEnd="url(#arr-red)"/>
          <text x="474" y="74" fontSize="8" fill="#C8102E" fontFamily="Inter" textAnchor="middle" fontWeight="500" opacity="0.9">Shinkansen ~2h15m · 450km</text>
          <path d="M 332,130 Q 268,155 224,166" stroke="#C9A84C" strokeWidth="1.5" fill="none" strokeDasharray="5,4" opacity="0.75" markerEnd="url(#arr-gold)"/>
          <text x="274" y="143" fontSize="7.5" fill="#C9A84C" fontFamily="Inter" textAnchor="middle" fontWeight="500">~75km · 15min</text>
          <path d="M 388,128 Q 422,155 441,178" stroke="#1a5228" strokeWidth="1.5" fill="none" strokeDasharray="5,4" opacity="0.7" markerEnd="url(#arr-green)"/>
          <text x="428" y="148" fontSize="7.5" fill="#1a5228" fontFamily="Inter" textAnchor="middle" fontWeight="500">~45km</text>
          <path d="M 331,111 Q 230,85 153,88" stroke="#5a7c5e" strokeWidth="1.5" fill="none" strokeDasharray="5,4" opacity="0.7" markerEnd="url(#arr-sage)"/>
          <text x="242" y="80" fontSize="7.5" fill="#5a7c5e" fontFamily="Inter" textAnchor="middle" fontWeight="500">~100km · 2hr JR</text>
          <path d="M 577,121 L 588,182" stroke="#C9A84C" strokeWidth="1.5" fill="none" strokeDasharray="5,4" opacity="0.7" markerEnd="url(#arr-gold)"/>
          <text x="615" y="155" fontSize="7.5" fill="#C9A84C" fontFamily="Inter" textAnchor="middle" fontWeight="500">~120km</text>
          <path d="M 390,108 Q 475,80 557,86" stroke="#1a2744" strokeWidth="1" fill="none" strokeDasharray="3,5" opacity="0.2" markerEnd="url(#arr-red)"/>
          
          <rect x="18" y="240" width="8" height="3" rx="1.5" fill="#C8102E" opacity="0.7"/>
          <text x="30" y="246" fontSize="7.5" fill="#7a6f5e" fontFamily="Inter">Shinkansen</text>
          <rect x="100" y="240" width="8" height="3" rx="1.5" fill="#C9A84C" opacity="0.8"/>
          <text x="112" y="246" fontSize="7.5" fill="#7a6f5e" fontFamily="Inter">Day trip</text>
          <rect x="165" y="240" width="8" height="3" rx="1.5" fill="#5a7c5e" opacity="0.8"/>
          <text x="177" y="246" fontSize="7.5" fill="#7a6f5e" fontFamily="Inter">Scenic excursion</text>
        </svg>
      </div>
    </div>
  );
}
