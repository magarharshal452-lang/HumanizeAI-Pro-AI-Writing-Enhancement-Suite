import streamlit as st
st.markdown("""
<style>

/* Main App */
.main{
    padding-top:20px;
}

/* Hide Streamlit Branding */
#MainMenu{
    visibility:hidden;
}
footer{
    visibility:hidden;
}
header{
    visibility:hidden;
}

/* Buttons */
.stButton>button{
    width:100%;
    height:52px;
    border-radius:12px;
    border:none;
    background:#4F46E5;
    color:white;
    font-size:17px;
    font-weight:600;
}

.stButton>button:hover{
    background:#4338CA;
}

/* Text Area */
textarea{
    border-radius:12px !important;
}

/* Metrics */
[data-testid="metric-container"]{
    border-radius:12px;
    padding:15px;
    border:1px solid #E5E7EB;
    box-shadow:0 2px 10px rgba(0,0,0,.05);
}

</style>
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="HumanizeAI Pro",
    page_icon="✍️",
    layout="wide"
)

st.title("✍️ HumanizeAI Pro")
st.caption("Transform AI-generated text into natural human writing.")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Input")

    style = st.selectbox(
        "Writing Style",
        [
            "Academic",
            "Assignment",
            "Research Paper",
            "Professional",
            "Casual"
        ]
    )

    input_text = st.text_area(
        "Paste AI-generated text",
        height=350,
        placeholder="Paste your AI-generated content here..."
    )

    humanize = st.button(
        "✨ Humanize Text",
        use_container_width=True
    )

with col2:

    st.subheader("Humanized Output")

    output = st.text_area(
        "",
        height=350,
        placeholder="Your humanized text will appear here...",
        key="output"
    )

    st.button(
        "📋 Copy Humanized Text",
        use_container_width=True
    )

st.divider()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Words", 0)
c2.metric("Characters", 0)
c3.metric("Reading Time", "0 min")
c4.metric("Quality", "--")
