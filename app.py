import streamlit as st

st.set_page_config(
    page_title="Hello World",
    page_icon="👋",
    layout="centered",
    initial_sidebar_state="auto"
)
st.write("Hello World")
"Hello World"
st.markdown("Hello World")
st.title("Hello World")
st.header("Hello World")
st.subheader("Hello World")
st.text("Hello World")
st.badge("Hello World")
st.caption("Hello World")
st.code("Hello World")

with st.echo():
    st.write("Hello World")

st.divider()
st.html("<h1>Hello World</h1>")

st.sidebar.write("Hello World")
st.columns(3)
