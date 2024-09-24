import pandas as pd
import streamlit as st
from pandasai.agent import Agent
from io import StringIO
import os

st.title("Pandas AI App")
# Upload CSV file
uploaded_file = st.file_uploader("Upload csv file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    string_data = StringIO(bytes_data.decode("utf-8"))
    # Read CSV data into a DataFrame
    df = pd.read_csv(string_data)
    # Display DataFrame
    st.dataframe(df)

    os.environ["PANDASAI_API_KEY"] = "PANDASAI_API_KEY"
    agent = Agent(df)
    # Get user query
    query = st.text_input("Enter your query")
    if query:
        response = agent.chat(query)
        # Display the response
        st.write(response)