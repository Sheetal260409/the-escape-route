import streamlit as st

st.set_page_config(page_title="The Escape Route", page_icon="🗺️")

st.title("🗺️ The Escape Route")
st.markdown("### Travel from heartbreak to hope")

if st.button("Start Your Escape"):
    st.balloons()
    st.success("You're on your way to healing! 💪")
