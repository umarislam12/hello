import streamlit as st
st.title('This is you graidng system')
marks=st.number_input('Enter obtained marks:',min_value=1)
total=st.number_input('Enter Total marks',min_value=1)

p=marks/total*100
r=st.button('Calculate results')
if(r):
    st.subheader(f'your percentage: :blue[{p} %]')

    if p>=80:
        st.success('excellent')
    elif p>=60 and p<80:
        st.info('pass')
    else:
        st.error('Fail')