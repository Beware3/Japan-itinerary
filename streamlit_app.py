import streamlit as st
import json
import os
import base64

def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""


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
if "itinerary" not in st.session_state:
    if os.path.exists(data_file):
        with open(data_file, "r", encoding="utf-8") as f:
            st.session_state.itinerary = json.load(f)
    else:
        st.error("Itinerary data not found.")
        st.stop()

# State for suggestions and editing
if "suggestions" not in st.session_state:
    st.session_state.suggestions = {}
if "global_suggestions" not in st.session_state:
    st.session_state.global_suggestions = []
if "editing_item" not in st.session_state:
    st.session_state.editing_item = None
if "last_notification" not in st.session_state:
    st.session_state.last_notification = None

if st.session_state.last_notification:
    st.toast(st.session_state.last_notification, icon="🔔")
    st.success(f"🔔 {st.session_state.last_notification}")
    st.session_state.last_notification = None

st.header("Day-by-Day Itinerary")

for day_idx, day in enumerate(st.session_state.itinerary):
    day_id = str(day["id"])
    if day_id not in st.session_state.suggestions:
        st.session_state.suggestions[day_id] = []
        
    bg_style = ""
    if "image" in day:
        img_path = day["image"].lstrip("/")
        base64_img = get_base64_of_bin_file(img_path)
        if base64_img:
            bg_style = f"background: linear-gradient(rgba(17, 24, 39, 0.65), rgba(17, 24, 39, 0.85)), url('data:image/png;base64,{base64_img}') center/cover;"

    with st.container():
        st.markdown(f"""
        <div class="day-card" style="{bg_style}">
            <h3 style="color: white; text-shadow: 0 2px 4px rgba(0,0,0,0.8);">Day {day['dayNumber']}: {day['title']}</h3>
            <p style="color: #FDF6EC; text-shadow: 0 1px 2px rgba(0,0,0,0.8);"><strong>{day['date']}</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.editing_item == f"edit_day_{day_id}":
            with st.container():
                new_title = st.text_input("Title", value=day['title'], key=f"edit_title_{day_id}")
                new_date = st.text_input("Date", value=day['date'], key=f"edit_date_{day_id}")
                c1, c2 = st.columns(2)
                if c1.button("Save", key=f"save_day_{day_id}"):
                    st.session_state.itinerary[day_idx]["title"] = new_title
                    st.session_state.itinerary[day_idx]["date"] = new_date
                    st.session_state.editing_item = None
                    st.rerun()
                if c2.button("Cancel", key=f"cancel_day_{day_id}"):
                    st.session_state.editing_item = None
                    st.rerun()
        else:
            if st.button("✏️ Edit Heading", key=f"edit_btn_day_{day_id}"):
                st.session_state.editing_item = f"edit_day_{day_id}"
                st.rerun()
        
        for group_idx, group in enumerate(day["activities"]):
            st.subheader(f"{group['icon']} {group['group']}")
            for item_idx, item in enumerate(group["items"]):
                item_key = f"{day_id}_{group_idx}_{item_idx}"
                
                if st.session_state.editing_item == item_key:
                    with st.container():
                        new_name = st.text_input("Name", value=item['name'], key=f"edit_name_{item_key}")
                        new_desc = st.text_input("Description", value=item.get('desc', ''), key=f"edit_desc_{item_key}")
                        new_link = st.text_input("Link", value=item.get('link', ''), key=f"edit_link_{item_key}")
                        
                        c1, c2 = st.columns(2)
                        if c1.button("Save", key=f"save_{item_key}"):
                            st.session_state.itinerary[day_idx]["activities"][group_idx]["items"][item_idx] = {
                                "name": new_name,
                                "desc": new_desc,
                                "link": new_link
                            }
                            st.session_state.editing_item = None
                            st.rerun()
                        if c2.button("Cancel", key=f"cancel_{item_key}"):
                            st.session_state.editing_item = None
                            st.rerun()
                else:
                    colA, colB, colC = st.columns([6, 1, 1])
                    with colA:
                        desc = f" — {item['desc']}" if "desc" in item and item['desc'] else ""
                        if "link" in item and item['link']:
                            st.markdown(f"- [{item['name']}]({item['link']}){desc}")
                        else:
                            st.markdown(f"- {item['name']}{desc}")
                    with colB:
                        if st.button("✏️", key=f"edit_btn_{item_key}", help="Edit"):
                            st.session_state.editing_item = item_key
                            st.rerun()
                    with colC:
                        if st.button("❌", key=f"del_item_{item_key}", help="Delete"):
                            st.session_state.itinerary[day_idx]["activities"][group_idx]["items"].pop(item_idx)
                            st.rerun()
                            
            with st.expander(f"+ Add to {group['group']}"):
                add_name = st.text_input("Name", key=f"add_name_{day_id}_{group_idx}")
                add_desc = st.text_input("Description", key=f"add_desc_{day_id}_{group_idx}")
                add_link = st.text_input("Link (Google Maps etc)", key=f"add_link_{day_id}_{group_idx}")
                if st.button("Add Activity", key=f"add_btn_{day_id}_{group_idx}"):
                    if add_name:
                        st.session_state.itinerary[day_idx]["activities"][group_idx]["items"].append({
                            "name": add_name,
                            "desc": add_desc,
                            "link": add_link
                        })
                        st.rerun()
        
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
