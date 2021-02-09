import streamlit as st
import os
import logging
import pandas as pd
import json
import logging as log


@st.cache(allow_output_mutation=True)
def get_log():
    """Set's up the default logger
    Returns:
        Logger: [description]
    """
    logger = logging.getLogger("FastEDA")
    logger.setLevel(logging.INFO)
    return logger

get_log()

# Streamlit specific widgets and displays
st.title("FastEDA")
st.subheader("File Upload")
st.write("Must have a LoadNum Column")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    dataframe = pd.read_excel(uploaded_file)
