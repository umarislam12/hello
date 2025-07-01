import streamlit as st

# Initialize session state for calculator
if 'calc_input' not in st.session_state:
    st.session_state.calc_input = ''

st.title("Umar's Calculator for AI Class")

col1, col2 = st.columns([0.7, 0.3], gap="small")

def clear_input():
    st.session_state.calc_input = ''

with col1:
    # Allow keyboard input
    st.session_state.calc_input = st.text_input(
        label="",
        value=st.session_state.calc_input,
        key="display",
        label_visibility="collapsed"
    )

with col2:
    st.button("🧼 Clear", on_click=clear_input, use_container_width=True)

# Function to append characters to input
def add_to_input(value):
    st.session_state.calc_input += str(value)

def remove_input():
    if st.session_state.calc_input:
        st.session_state.calc_input = st.session_state.calc_input[:-1]

def calculate():
    try:
        st.session_state.calc_input = str(eval(st.session_state.calc_input))
    except:
        st.session_state.calc_input = "Error"

# Calculator button grid
col1, col2, col3, col4 = st.columns([0.5, 0.5, 0.5, 0.5], vertical_alignment="top")

with col1:
    st.button("7", on_click=add_to_input, args=('7',), use_container_width=True)
    st.button("4", on_click=add_to_input, args=('4',), use_container_width=True)
    st.button("1", on_click=add_to_input, args=('1',), use_container_width=True)
    st.button("⌫", on_click=remove_input, use_container_width=True)

with col2:
    st.button("8", on_click=add_to_input, args=('8',), use_container_width=True)
    st.button("5", on_click=add_to_input, args=('5',), use_container_width=True)
    st.button("2", on_click=add_to_input, args=('2',), use_container_width=True)
    st.button("0", on_click=add_to_input, args=('0',), use_container_width=True)

with col3:
    st.button("9", on_click=add_to_input, args=('9',), use_container_width=True)
    st.button("6", on_click=add_to_input, args=('6',), use_container_width=True)
    st.button("3", on_click=add_to_input, args=('3',), use_container_width=True)
    st.button(".", on_click=add_to_input, args=('.',), use_container_width=True)

with col4:
    st.button("➖", on_click=add_to_input, args=('-',), use_container_width=True)
    st.button("➕", on_click=add_to_input, args=('+',), use_container_width=True)
    st.button("✖️", on_click=add_to_input, args=('*',), use_container_width=True)
    st.button("➗", on_click=add_to_input, args=('/',), use_container_width=True)

# Equal button spans full width
st.button("🟰", on_click=calculate, use_container_width=True)
