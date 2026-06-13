import streamlit as st

from humanizer import humanize
from quality_checker import similarity_score

st.set_page_config(
    page_title="AI Humanizer",
    page_icon="✍️",
    layout="wide"
)

st.title("AI Humanizer")

text = st.text_area(
    "Paste your text here",
    height=250
)

mode = st.selectbox(
    "Select Humanization Mode",
    [
        "casual",
        "professional",
        "academic",
        "creative"
    ]
)

if st.button("Humanize"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        with st.spinner("Humanizing..."):

            output = humanize(
                text,
                mode
            )

            score = similarity_score(
                text,
                output
            )

        st.subheader("Humanized Text")

        st.write(output)

        st.metric(
            "Meaning Preservation %",
            score
        )
