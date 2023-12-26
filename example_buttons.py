import streamlit as st
import pandas as pd

if "name" not in st.session_state:
    st.session_state["name"] = "John Doe"

st.header(st.session_state["name"])

if st.button("Jane"):
    st.session_state["name"] = "Jane Doe"
    st.rerun()

if st.button("John"):
    st.session_state["name"] = "John Doe"
    st.rerun()

st.header(st.session_state["name"])
