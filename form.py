import streamlit as st
with st.form('Form'):
    st.write('please fill the form')
    name=st.text_input('Name')
    college_name=st.text_input('Your college name')
    percentage=st.number_input('your percentage')
    working=st.checkbox("Are you working?")

    submitted=st.form_submit_button('submit')
    if submitted:
        st.write('Name:',name)
        st.write('college_name:',college_name)
        st.write('Percentage:',percentage)
        st.write('Are you working',working)