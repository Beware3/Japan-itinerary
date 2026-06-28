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

# --- Premium Light Design System CSS ---
st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Noto+Serif+JP:wght@400;700&display=swap" rel="stylesheet">
<style>
    /* ── Reset & Global ─────────────────────────────────── */
    .stApp {
        background: #FAFAF7 !important;
        color: #1e293b;
        font-family: 'Outfit', sans-serif;
    }
    h1, h2, h3, h4 { font-family: 'Outfit', sans-serif !important; color: #1e293b !important; }

    /* ── Scrollbar ────────────────────────────────────── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #f5f5f0; }
    ::-webkit-scrollbar-thumb { background: #C8102E; border-radius: 3px; }


    /* ── Hero Banner ──────────────────────────────────── */
    .hero-wrap {
        position: relative;
        text-align: center;
        padding: 3.5rem 2rem 3rem;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 2rem;
    }
    .hero-wrap::before {
        content: '';
        position: absolute; inset: 0;
        background: linear-gradient(135deg, #1e293b 0%, #334155 40%, #475569 70%, #1e293b 100%);
        z-index: 0;
    }
    .hero-wrap::after {
        content: '';
        position: absolute; inset: 0;
        background: radial-gradient(circle at 70% 30%, rgba(200, 16, 46, 0.12) 0%, transparent 60%),
                    radial-gradient(circle at 30% 80%, rgba(201, 168, 76, 0.08) 0%, transparent 50%);
        z-index: 1;
    }
    .hero-content { position: relative; z-index: 2; }
    .hero-jp {
        font-family: 'Noto Serif JP', serif;
        color: #C9A84C;
        font-size: 1rem;
        letter-spacing: 6px;
        text-transform: uppercase;
        margin-bottom: 0.25rem;
        opacity: 0.9;
    }
    .hero-title {
        color: #fff;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700;
        font-size: 3.2rem;
        margin: 0.25rem 0;
        letter-spacing: -0.5px;
    }
    .hero-dates {
        color: rgba(255,255,255,0.6);
        font-size: 1rem;
        letter-spacing: 3px;
        font-weight: 300;
    }
    .hero-accent {
        width: 60px; height: 3px;
        background: linear-gradient(90deg, #C8102E, #C9A84C);
        margin: 1rem auto 0;
        border-radius: 2px;
    }

    /* ── Stat Cards ───────────────────────────────────── */
    .stat-row {
        display: flex;
        justify-content: center;
        gap: 1.25rem;
        margin-bottom: 2rem;
        flex-wrap: wrap;
    }
    .stat-card {
        background: #fff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 1.25rem 2rem;
        text-align: center;
        min-width: 120px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stat-card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
    .stat-val {
        font-size: 2rem;
        font-weight: 700;
        color: #C8102E;
        line-height: 1.2;
    }
    .stat-label { font-size: 0.75rem; color: #94a3b8; letter-spacing: 2px; text-transform: uppercase; margin-top: 4px; }

    /* ── Section Title ────────────────────────────────── */
    .section-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: #1e293b !important;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    .section-title::after {
        content: '';
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, #C8102E33, transparent);
    }

    /* ── Day Card Header ─────────────────────────────── */
    .day-header {
        position: relative;
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 0.5rem;
        min-height: 140px;
        display: flex;
        align-items: flex-end;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .day-header-bg {
        position: absolute; inset: 0;
        background-size: cover;
        background-position: center;
    }
    .day-header-overlay {
        position: absolute; inset: 0;
        background: linear-gradient(to top, rgba(30,41,59,0.92) 0%, rgba(30,41,59,0.4) 50%, rgba(30,41,59,0.15) 100%);
    }
    .day-header-content {
        position: relative;
        z-index: 2;
        padding: 1.25rem 1.5rem;
        width: 100%;
    }
    .day-number {
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #C9A84C;
        margin-bottom: 2px;
    }
    .day-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #fff !important;
        margin: 0;
        line-height: 1.3;
    }
    .day-date {
        font-size: 0.85rem;
        color: rgba(255,255,255,0.6);
        font-weight: 300;
        margin-top: 2px;
    }

    /* ── Activity Group Label ─────────────────────────── */
    .group-label {
        font-size: 0.9rem;
        font-weight: 600;
        color: #C8102E;
        letter-spacing: 1px;
        margin: 1rem 0 0.5rem;
        padding-bottom: 0.4rem;
        border-bottom: 1px solid #fce4e4;
    }

    /* ── Activity Item ────────────────────────────────── */
    .activity-item {
        display: flex;
        align-items: center;
        padding: 0.5rem 0.5rem;
        border-radius: 10px;
        margin: 2px 0;
        transition: background 0.15s;
    }
    .activity-item:hover { background: #f8f5f0; }
    .activity-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #C8102E;
        margin-right: 0.6rem;
        flex-shrink: 0;
    }
    .activity-name {
        flex: 1;
        color: #334155;
        font-size: 0.95rem;
    }
    .activity-name a {
        color: #2563eb;
        text-decoration: none;
        border-bottom: 1px solid rgba(37,99,235,0.2);
        transition: border-color 0.2s;
    }
    .activity-name a:hover { border-color: #2563eb; }
    .activity-desc {
        color: #94a3b8;
        font-size: 0.85rem;
        margin-left: 0.25rem;
    }

    /* ── Suggestion Item ──────────────────────────────── */
    .sugg-item-row {
        display: flex;
        align-items: center;
        padding: 0.6rem 0.75rem;
        background: #fff;
        border-radius: 8px;
        margin: 4px 0;
        border-left: 3px solid #C9A84C;
    }
    .sugg-text { flex: 1; color: #475569; font-size: 0.9rem; }

    /* ── Streamlit Widget Overrides ───────────────────── */
    .stButton > button {
        border-radius: 10px !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 500 !important;
        transition: all 0.2s !important;
        min-height: 40px !important;
        min-width: 40px !important;
    }
    .stTextInput > div > div > input {
        border-radius: 10px !important;
        font-family: 'Outfit', sans-serif !important;
        min-height: 44px !important;
        font-size: 16px !important;
    }
    .stExpander {
        border-radius: 12px !important;
        border-color: #e5e7eb !important;
        background: #fff !important;
    }

    /* ── Footer ───────────────────────────────────────── */
    .footer {
        text-align: center;
        padding: 3rem 0 2rem;
        color: #cbd5e1;
        font-size: 0.8rem;
        letter-spacing: 2px;
    }

    /* ── Mobile Responsive ────────────────────────────── */
    @media (max-width: 768px) {
        .hero-wrap { padding: 2.5rem 1rem 2rem; border-radius: 14px; margin-bottom: 1.5rem; }
        .hero-title { font-size: 2rem !important; }
        .hero-jp { font-size: 0.8rem; letter-spacing: 4px; }
        .hero-dates { font-size: 0.8rem; letter-spacing: 2px; }

        .stat-row { gap: 0.75rem; margin-bottom: 1.5rem; }
        .stat-card { min-width: 80px; padding: 0.75rem 1rem; border-radius: 12px; }
        .stat-val { font-size: 1.5rem; }
        .stat-label { font-size: 0.65rem; letter-spacing: 1px; }

        .section-title { font-size: 1.2rem; margin-bottom: 1rem; }

        .day-header { min-height: 100px; border-radius: 12px; }
        .day-header-content { padding: 0.75rem 1rem; }
        .day-title { font-size: 1.1rem; }
        .day-number { font-size: 0.6rem; letter-spacing: 2px; }
        .day-date { font-size: 0.7rem; }

        .group-label { font-size: 0.8rem; margin: 0.75rem 0 0.35rem; }
        .activity-item { padding: 0.35rem 0.15rem; }
        .activity-name { font-size: 0.82rem; }
        .activity-desc { font-size: 0.72rem; }
        .activity-dot { width: 5px; height: 5px; margin-right: 0.4rem; }

        .stButton > button { min-height: 38px !important; min-width: 38px !important; padding: 0.25rem 0.5rem !important; font-size: 0.9rem !important; }

        section[data-testid="stSidebar"] { display: none !important; }
        .block-container { padding: 0.5rem 0.75rem !important; }
        .footer { padding: 2rem 0 1.5rem; font-size: 0.7rem; }
    }

    @media (max-width: 400px) {
        .hero-title { font-size: 1.6rem !important; }
        .hero-wrap { padding: 2rem 0.75rem 1.5rem; }
        .stat-card { min-width: 70px; padding: 0.6rem 0.75rem; }
        .stat-val { font-size: 1.25rem; }
        .day-title { font-size: 1rem; }
        .activity-name { font-size: 0.78rem; }
    }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-content">
        <div class="hero-jp">日本旅行 二〇二六</div>
        <div class="hero-title">Japan 🌸 Itinerary</div>
        <div class="hero-dates">29 AUGUST — 8 SEPTEMBER 2026</div>
        <div class="hero-accent"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────
st.markdown("""
<div class="stat-row">
    <div class="stat-card"><div class="stat-val">10</div><div class="stat-label">Days</div></div>
    <div class="stat-card"><div class="stat-val">6</div><div class="stat-label">Cities</div></div>
    <div class="stat-card"><div class="stat-val">5</div><div class="stat-label">Travellers</div></div>
</div>
""", unsafe_allow_html=True)

# ── Load Data ─────────────────────────────────────────
data_file = "japan-itinerary-app/src/data/ItineraryData.json"
if "itinerary" not in st.session_state:
    if os.path.exists(data_file):
        with open(data_file, "r", encoding="utf-8") as f:
            st.session_state.itinerary = json.load(f)
    else:
        st.error("Itinerary data not found.")
        st.stop()

# ── State ─────────────────────────────────────────────
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

# ── Section Title ─────────────────────────────────────
st.markdown('<div class="section-title">🗾 Day-by-Day Itinerary</div>', unsafe_allow_html=True)

# ── Day Loop ──────────────────────────────────────────
for day_idx, day in enumerate(st.session_state.itinerary):
    day_id = str(day["id"])
    if day_id not in st.session_state.suggestions:
        st.session_state.suggestions[day_id] = []

    # Day Header with background image
    bg_css = ""
    if "image" in day:
        img_path = day["image"].lstrip("/")
        base64_img = get_base64_of_bin_file(img_path)
        if base64_img:
            bg_css = f"background-image: url('data:image/png;base64,{base64_img}');"

    st.markdown(f"""
    <div class="day-header">
        <div class="day-header-bg" style="{bg_css}"></div>
        <div class="day-header-overlay"></div>
        <div class="day-header-content">
            <div class="day-number">Day {day['dayNumber']}</div>
            <div class="day-title">{day['title']}</div>
            <div class="day-date">{day['date']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Edit heading
    if st.session_state.editing_item == f"edit_day_{day_id}":
        with st.container():
            new_title = st.text_input("Title", value=day['title'], key=f"edit_title_{day_id}")
            new_date = st.text_input("Date", value=day['date'], key=f"edit_date_{day_id}")
            c1, c2 = st.columns(2)
            if c1.button("💾 Save", key=f"save_day_{day_id}"):
                st.session_state.itinerary[day_idx]["title"] = new_title
                st.session_state.itinerary[day_idx]["date"] = new_date
                st.session_state.editing_item = None
                st.rerun()
            if c2.button("✖ Cancel", key=f"cancel_day_{day_id}"):
                st.session_state.editing_item = None
                st.rerun()
    else:
        if st.button("✏️ Edit Heading", key=f"edit_btn_day_{day_id}"):
            st.session_state.editing_item = f"edit_day_{day_id}"
            st.rerun()

    # Activities
    for group_idx, group in enumerate(day["activities"]):
        st.markdown(f'<div class="group-label">{group["icon"]} {group["group"]}</div>', unsafe_allow_html=True)

        for item_idx, item in enumerate(group["items"]):
            item_key = f"{day_id}_{group_idx}_{item_idx}"

            if st.session_state.editing_item == item_key:
                with st.container():
                    new_name = st.text_input("Name", value=item['name'], key=f"edit_name_{item_key}")
                    new_desc = st.text_input("Description", value=item.get('desc', ''), key=f"edit_desc_{item_key}")
                    new_link = st.text_input("Link", value=item.get('link', ''), key=f"edit_link_{item_key}")

                    c1, c2 = st.columns(2)
                    if c1.button("💾 Save", key=f"save_{item_key}"):
                        st.session_state.itinerary[day_idx]["activities"][group_idx]["items"][item_idx] = {
                            "name": new_name,
                            "desc": new_desc,
                            "link": new_link
                        }
                        st.session_state.editing_item = None
                        st.rerun()
                    if c2.button("✖ Cancel", key=f"cancel_{item_key}"):
                        st.session_state.editing_item = None
                        st.rerun()
            else:
                # Render activity + edit/delete on one row
                desc_html = f'<span class="activity-desc"> — {item["desc"]}</span>' if "desc" in item and item["desc"] else ""
                if "link" in item and item["link"]:
                    name_html = f'<a href="{item["link"]}" target="_blank">{item["name"]}</a>'
                else:
                    name_html = item["name"]

                colA, colB, colC = st.columns([8, 1, 1])
                with colA:
                    st.markdown(f"""
                    <div class="activity-item">
                        <div class="activity-dot"></div>
                        <div class="activity-name">{name_html}{desc_html}</div>
                    </div>
                    """, unsafe_allow_html=True)
                with colB:
                    if st.button("✏️", key=f"edit_btn_{item_key}", help="Edit"):
                        st.session_state.editing_item = item_key
                        st.rerun()
                with colC:
                    if st.button("🗑️", key=f"del_item_{item_key}", help="Delete"):
                        st.session_state.itinerary[day_idx]["activities"][group_idx]["items"].pop(item_idx)
                        st.rerun()

        # Add to group
        with st.expander(f"＋ Add to {group['group']}"):
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

    # Suggestions per day
    with st.expander(f"💬 Suggestions for Day {day['dayNumber']}"):
        for idx, s in enumerate(st.session_state.suggestions[day_id]):
            col_list1, col_list2 = st.columns([5, 1])
            with col_list1:
                st.write(f"- {s}")
            with col_list2:
                if st.button("🗑️", key=f"del_sugg_{day_id}_{idx}", help="Delete suggestion"):
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

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

# ── General Suggestions ──────────────────────────────
st.markdown('<div class="section-title">✉️ General Suggestions</div>', unsafe_allow_html=True)

for idx, s in enumerate(st.session_state.global_suggestions):
    col_g_list1, col_g_list2 = st.columns([5, 1])
    with col_g_list1:
        st.write(f"✉️ {s}")
    with col_g_list2:
        if st.button("🗑️", key=f"del_global_{idx}", help="Delete suggestion"):
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

# ── Footer ────────────────────────────────────────────
st.markdown('<div class="footer">🌸 JAPAN 2026 — BUILT WITH LOVE 🌸</div>', unsafe_allow_html=True)
