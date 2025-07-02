import streamlit as st
from streamlit import session_state, columns

# Initialize session state for calculator
if 'calc_input' not in st.session_state:
    st.session_state.calc_input = ''

# Calculator layout
st.title(":primary[Umar's calculator for AI class]")
st.title("")
col1,col2=st.columns([0.7,0.3],gap="small")


def clear_input():
    st.session_state.calc_input = ''
with col1:
    # Display text field for input/output
    result = st.text_input("", st.session_state.calc_input, key="display", disabled=True,label_visibility="collapsed")

with col2:

    st.button("🗑️Clear",type="primary", on_click=clear_input,use_container_width=True)
# Create buttons for calculator
col1, col2, col3, col4 = st.columns([0.5,0.5,0.5,0.5], vertical_alignment="top")

def add_to_input(value):
    st.session_state.calc_input += str(value)
    # st.write("Current input:", st.session_state.calc_input)

def remove_input():
    if st.session_state.calc_input:  # Check if input isn't empty
        st.session_state.calc_input = st.session_state.calc_input[:-1]
def calculate():
    try:
        st.session_state.calc_input = str(eval(st.session_state.calc_input))
    except:
        st.session_state.calc_input = "Error:press clear button to continue"

with col1:

    st.button("7", on_click=add_to_input,use_container_width=True, args=('7',))
    st.button("4", on_click=add_to_input,use_container_width=True, args=('4',))

    st.button("1", on_click=add_to_input,use_container_width=True, args=('1',))
    st.button("⌫", on_click=remove_input,type="primary", use_container_width=True)

with col2:

    st.button("8", on_click=add_to_input,use_container_width=True, args=('8',))
    st.button("5", on_click=add_to_input, use_container_width=True,args=('5',))
    st.button("2", on_click=add_to_input,use_container_width=True, args=('2',))

    st.button("0", on_click=add_to_input,use_container_width=True, args=('0',))

with col3:

    st.button("9",use_container_width=True, on_click=add_to_input, args=('9',))
    st.button("6",use_container_width=True, on_click=add_to_input, args=('6',))
    st.button("3",use_container_width=True, on_click=add_to_input, args=('3',))
    st.button(".",use_container_width=True, on_click=add_to_input, args=('.',))

with col4:
    st.button("➖", on_click=add_to_input, type="primary", args=('-',),use_container_width=True)
    st.button("➕", on_click=add_to_input,type="primary", args=('+',),use_container_width=True)
    st.button("✖️", type="primary", on_click=add_to_input, args=('*',),use_container_width=True)
    st.button("➗",type="primary", on_click=add_to_input, args=('/',),use_container_width=True)
# Equal button spanning full width
st.button("🟰", icon="⭐", type="primary", on_click=calculate, use_container_width=True)