import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="HumanizeAI Pro",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("✍️ HumanizeAI Pro")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🤖 AI Humanizer",
        "📊 Readability",
        "📄 Export",
        "ℹ️ About"
    ]
)

# ----------------------------
# Home Page
# ----------------------------
if page == "🏠 Home":

    st.title("HumanizeAI Pro")

    st.markdown("""
### Welcome 👋

HumanizeAI Pro is an AI-powered writing enhancement platform.

### Features

- ✨ AI Humanizer
- 📊 Readability Analysis
- 📄 Export to TXT
- 📄 Export to PDF
- 📄 Export to DOCX
- 📝 Multiple Writing Styles
- 🎯 Meaning Preservation
- 📈 Humanization Score
""")

# ----------------------------
# Humanizer Page
# ----------------------------
elif page == "🤖 AI Humanizer":

    st.title("AI Humanizer")

    style = st.selectbox(
        "Writing Style",
        [
            "Academic",
            "Professional",
            "Casual",
            "Creative"
        ]
    )

    user_text = st.text_area(
        "Paste your text here",
        height=250
    )

    if st.button("✨ Humanize Text"):
        st.info("Humanization engine will be added in the next step.")

# ----------------------------
# Readability
# ----------------------------
elif page == "📊 Readability":

    st.title("Readability Analysis")

    st.info("Coming Soon")

# ----------------------------
# Export
# ----------------------------
elif page == "📄 Export":

    st.title("Export")

    st.info("Coming Soon")

# ----------------------------
# About
# ----------------------------
elif page == "ℹ️ About":

    st.title("About HumanizeAI Pro")

    st.write("""
Version: 2.0

Developed by Harshal Magar

Built with Streamlit.
""")
