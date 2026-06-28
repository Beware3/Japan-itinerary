# pyrefly: ignore [missing-import]
import streamlit as st
import json
import os

st.set_page_config(page_title="Japan Itinerary 2026", page_icon="🌸", layout="centered")

# --- Custom CSS ---
st.markdown("""
<style>
    .hero {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #111827, #1a2744);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .hero h1 { color: white; font-family: 'serif'; font-size: 3rem; margin-bottom: 0; }
    .hero p { color: #C9A84C; font-size: 1.2rem; letter-spacing: 2px; }
    .day-card {
        background: #FDF6EC;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #C8102E;
        margin-bottom: 1.5rem;
        color: #111827;
    }
    .day-card h3 { color: #111827; margin-top: 0; }
    .cost-badge {
        background: #e2e8f0; padding: 2px 8px; border-radius: 5px; font-size: 0.8rem; color: #334155;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><p>日本旅行 二〇二六</p><h1>Japan 🌸 Itinerary</h1><p>29 August – 8 September 2026</p></div>', unsafe_allow_html=True)

st.write("### Trip Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Days", "10")
col2.metric("Cities", "6")
col3.metric("Travellers", "5")
st.divider()

# Load Data
data_file = "japan-itinerary-app/src/data/ItineraryData.json"
if os.path.exists(data_file):
    with open(data_file, "r", encoding="utf-8") as f:
        itinerary = json.load(f)
else:
    st.error("Itinerary data not found.")
    st.stop()

# State for costs and suggestions
if "costs" not in st.session_state:
    st.session_state.costs = {}
if "suggestions" not in st.session_state:
    st.session_state.suggestions = {}
if "global_suggestions" not in st.session_state:
    st.session_state.global_suggestions = []
if "last_notification" not in st.session_state:
    st.session_state.last_notification = None

if st.session_state.last_notification:
    st.toast(st.session_state.last_notification, icon="🔔")
    st.success(f"🔔 {st.session_state.last_notification}")
    st.session_state.last_notification = None

st.header("Day-by-Day Itinerary")

for day in itinerary:
    day_id = str(day["id"])
    if day_id not in st.session_state.suggestions:
        st.session_state.suggestions[day_id] = []
        
    day_col1, day_col2 = st.columns([2, 1])
    
    with day_col1:
        st.markdown(f"""
        <div class="day-card">
            <h3>Day {day['dayNumber']}: {day['title']}</h3>
            <p><strong>{day['date']}</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        daily_total = 0
        
        for group_idx, group in enumerate(day["activities"]):
            st.subheader(f"{group['icon']} {group['group']}")
            for item_idx, item in enumerate(group["items"]):
                cost_key = f"cost_{day_id}_{group_idx}_{item_idx}"
                if cost_key not in st.session_state.costs:
                    st.session_state.costs[cost_key] = item.get("cost", 0)
                    
                colA, colB = st.columns([3, 1])
                with colA:
                    desc = f" — {item['desc']}" if "desc" in item else ""
                    if "link" in item:
                        st.markdown(f"- [{item['name']}]({item['link']}){desc}")
                    else:
                        st.markdown(f"- {item['name']}{desc}")
                with colB:
                    new_cost = st.number_input("Cost (¥)", value=st.session_state.costs[cost_key], key=f"input_{cost_key}", label_visibility="collapsed")
                    st.session_state.costs[cost_key] = new_cost
                    daily_total += new_cost
                    
        st.info(f"**Daily Total: ¥{daily_total}**")
        
        with st.expander(f"Suggestions for Day {day['dayNumber']}"):
            for idx, s in enumerate(st.session_state.suggestions[day_id]):
                col_list1, col_list2 = st.columns([5, 1])
                with col_list1:
                    st.write(f"- {s}")
                with col_list2:
                    if st.button("❌", key=f"del_sugg_{day_id}_{idx}", help="Delete suggestion"):
                        st.session_state.suggestions[day_id].pop(idx)
                        st.rerun()
            
            col_s1, col_s2 = st.columns([1, 3])
            with col_s1:
                sugg_name = st.text_input("Your Name", key=f"sugg_name_{day_id}")
            with col_s2:
                new_sugg = st.text_input("Add suggestion", key=f"sugg_input_{day_id}")
                
            if st.button("Add", key=f"sugg_btn_{day_id}"):
                if new_sugg:
                    display_sugg = f"**{sugg_name or 'Anonymous'}**: {new_sugg}"
                    st.session_state.suggestions[day_id].append(display_sugg)
                    st.session_state.last_notification = f"New suggestion for Day {day['dayNumber']} by {sugg_name or 'Anonymous'}!"
                    st.rerun()
                    
    with day_col2:
        if "image" in day:
            img_path = day["image"].lstrip("/")
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
                
    st.divider()

st.header("General Suggestions")
for idx, s in enumerate(st.session_state.global_suggestions):
    col_g_list1, col_g_list2 = st.columns([5, 1])
    with col_g_list1:
        st.write(f"✉️ {s}")
    with col_g_list2:
        if st.button("❌", key=f"del_global_{idx}", help="Delete suggestion"):
            st.session_state.global_suggestions.pop(idx)
            st.rerun()
    
col_g1, col_g2 = st.columns([1, 3])
with col_g1:
    global_name = st.text_input("Your Name", key="global_name")
with col_g2:
    global_sugg = st.text_input("Add a general trip suggestion:")
    
if st.button("Add General Suggestion"):
    if global_sugg:
        display_sugg = f"**{global_name or 'Anonymous'}**: {global_sugg}"
        st.session_state.global_suggestions.append(display_sugg)
        st.session_state.last_notification = f"New general suggestion by {global_name or 'Anonymous'}!"
        st.rerun()
