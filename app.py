import streamlit as st
st.set_page_config(page_title='BTS')
st.header("BTS:")

col1,col2,col3,col4,col5,col6,col7=st.columns(7)
with col1:
     st.subheader("RM ")
     st.image("./rm.jpg",caption="RM",width=300,use_column_width=True)
     
with col2:
      st.subheader("JIN ")
      st.image("./jin.jpg",caption="JIN",width=300,use_column_width=True)
with col3:
     st.subheader("SUGA ")
     st.image("./suga.jpg",caption="SUGA",width=300,use_column_width=True)
     

with col4:
     st.subheader("JHOPE ")
     st.image("./jhope1.jpg",caption="JHOPE",width=300,use_column_width=True)

with col5:
      st.subheader("JIMIN ")
      st.image("./jimin.jpg",caption="JIMIN",width=300,use_column_width=True)
with col6:
     st.subheader("V ")
     st.image("./v.jpg",caption="V",width=300,use_column_width=True)

with col7:
      st.subheader("JK ")
      st.image("./jk1.jpg",caption="Jk",width=300,use_column_width=True)
