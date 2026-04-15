import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="The Escape Route", page_icon="🗺️", layout="wide")

# Custom CSS for better design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
}
h1, h2, h3 {
    color: #ff6b6b;
}
</style>
""", unsafe_allow_html=True)

st.title("🗺️ The Escape Route")
st.markdown("### Travel from heartbreak to hope")
st.markdown("---")

# Create trip data
trips_data = {
    'destination': ['Bali, Indonesia', 'Swiss Alps, Switzerland', 'Kyoto, Japan', 'Costa Rica', 'Santorini, Greece', 'Thailand', 'Iceland', 'New Zealand'],
    'type': ['Beach', 'Adventure', 'Culture', 'Nature', 'Beach', 'Beach', 'Adventure', 'Nature'],
    'price': [1200, 2500, 2000, 1800, 1500, 900, 2200, 2800],
    'days': [7, 10, 5, 8, 6, 9, 7, 12],
    'spots': [5, 3, 7, 4, 6, 8, 2, 4]
}
trips = pd.DataFrame(trips_data)

# Sidebar
with st.sidebar:
    st.header("🌟 Your Profile")
    name = st.text_input("Name", "Traveler")
    days_since = st.slider("Days since heartbreak", 1, 180, 30)
    stage = st.select_slider("Your stage", 
        options=["Just happened", "Processing", "Healing", "Almost there", "Ready to love again"])
    st.markdown("---")
    st.metric("Community", "1,247 healing hearts")

# Three columns
col1, col2, col3 = st.columns(3)

# Column 1 - Trips
with col1:
    st.subheader("✈️ Find Your Escape")
    for i in range(len(trips)):
        trip = trips.iloc[i]
        with st.expander(f"🗺️ {trip['destination']}"):
            st.write(f"**Type:** {trip['type']} Trip")
            st.write(f"**Duration:** {trip['days']} days")
            st.write(f"**Price:** ${trip['price']}")
            st.write(f"**Spots left:** {trip['spots']}")
            if st.button(f"Join {trip['destination'].split(',')[0]}", key=f"trip_{i}"):
                st.success(f"You're escaping to {trip['destination']}! 🎉")
                st.balloons()

# Column 2 - Buddies
with col2:
    st.subheader("👥 Travel Buddies")
    buddies = [
        {"name": "Sarah", "age": 28, "city": "NYC", "stage": "Healing"},
        {"name": "Mike", "age": 32, "city": "LA", "stage": "Processing"},
        {"name": "Emma", "age": 26, "city": "Chicago", "stage": "Almost there"},
        {"name": "Alex", "age": 30, "city": "Miami", "stage": "Healing"},
        {"name": "Lisa", "age": 29, "city": "Seattle", "stage": "Processing"},
        {"name": "James", "age": 35, "city": "Denver", "stage": "Healing"},
    ]
    for idx, buddy in enumerate(buddies[:6]):
        with st.container():
            st.markdown(f"**{buddy['name']}**, {buddy['age']} - {buddy['city']}")
            st.markdown(f"💔 {buddy['stage']}")
            if st.button(f"Connect with {buddy['name']}", key=f"buddy_{idx}"):
                st.success(f"Connected with {buddy['name']}! 🤝")
            st.markdown("---")

# Column 3 - Healing
with col3:
    st.subheader("📊 Your Healing Journey")
    progress = min(100, int(days_since / 180 * 100))
    st.metric("Healing Progress", f"{progress}%")
    st.progress(progress / 100)
    
    st.markdown("---")
    st.subheader("💡 Healing Tip")
    if progress < 30:
        st.info("✨ Now is the perfect time for an escape trip!")
    elif progress < 70:
        st.success("🌱 You're healing beautifully! Keep going.")
    else:
        st.balloons()
        st.success("❤️ You're ready to love again!")
    
    st.markdown("---")
    st.subheader("📈 Quick Stats")
    st.write("🏖️ Beach trips heal 34% faster")
    st.write("👥 Group travel = 2.4x recovery")
    st.write("💝 94% make lasting friends")

st.markdown("---")
st.markdown("<p style='text-align: center;'>💔 → 🗺️ → ❤️ Every escape is a new beginning</p>", unsafe_allow_html=True)
