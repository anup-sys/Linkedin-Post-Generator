import streamlit as st
from gemini_client import generate_post

st.set_page_config(
    page_title="LinkedIn Post Generator",
    layout="wide",
)

st.title("🚀 LinkedIn Post Generator")
st.write("Create professional, high-quality LinkedIn posts")

# Input fields
topic = st.text_input("Post Topic")
tone = st.selectbox(
    "Tone Style",
    ["Professional", "Motivational", "Storytelling", "Casual", "Direct"]
)
audience = st.text_input("Target Audience")
points = st.text_area("Key Points (optional, bullet list, etc.)")

# Generate button
if st.button("Generate Post"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Crafting your LinkedIn post..."):
            post = generate_post(topic, tone, audience, points)

        st.subheader("✨ Your LinkedIn Post")
        st.write(post)

        # Download button
        st.download_button(
            label="Download as .txt",
            data=post,
            file_name="linkedin_post.txt"
        )

