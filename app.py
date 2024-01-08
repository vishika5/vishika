import streamlit as st
st.set_page_config(page_title='dogs')
st.header("BTS")

col1,col2,col3,col4,col5,col6,col7=st.columns(7)
with col1:
     st.subheader("rm")
     st.image("./rm.jpg",caption="rm",width=300,use_column_width=True)
with col2:
      st.subheader("jin")
      st.image("./jin.jpg",caption="jin",width=300,use_column_width=True)
with col3:
     st.subheader("suga")
     st.image("./suga.jpg",caption="suga",width=300,use_column_width=True)
with col4:
      st.subheader("jhope")
      st.image("./jhope.jpg",caption="jhope",width=300,use_column_width=True)
with col5:
     st.subheader("jimin")
     st.image("./jimin.jpg",caption="jimin",width=300,use_column_width=True)
with col6:
      st.subheader("v")
      st.image("./v.jpg",caption="v",width=300,use_column_width=True)
with col7:
      st.subheader("jk")
      st.image("./jk.jpg",caption="jk",width=300,use_column_width=True)
