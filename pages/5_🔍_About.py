import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.markdown(
"""
This web app is maintained by ACE,  
Remote sensing and Geographic Information Science (GIS) researchers group from Geomatics Engineering, Institute Technology of Sepuluh Nopember. 
"""
)

col1, col2, col3= st.columns(3)

with col2:
    st.subheader("About Us")
    #st.image("https://static.streamlit.io/examples/cat.jpg")

st.markdown(
""" 
"""
)

coll1, coll2, coll3= st.columns(3)

with coll1:
    #st.subheader("Member 1")
    st.image("https://i.postimg.cc/6pcKF60n/white.png")
    st.markdown(
        """
        Amalia Putri Rivani    
        03311940000026
        amaliarvn@gmail.com    
        [LinkedIn](https://www.linkedin.com/in/amalia-putri-rivani-6315a51b0/) | [Instagram](https://instagram.com/putrijklmn?igshid=YmMyMTA2M2Y=)
        """
    )

with coll3:
    #st.subheader("Member 2")
    st.image("https://i.postimg.cc/CLDfTLFr/Jurnalistik-Megivareza-Putri-Hanansyah-03311940000041.jpg")
    st.markdown(
        """
        Megivareza Putri Hanansyah
        03311940000041
        varezamegi@gmail.com    
        [LinkedIn](https://www.linkedin.com/in/megivareza-putri-hanansyah-b6b4b720a/) | [Instagram](https://instagram.com/megivareza?igshid=YmMyMTA2M2Y=)
        """
    )

st.markdown(
"""
Adviser :                               
1. Hartanto Sanjaya, S.Si., MSc                                                        
2. Lalu Muhamad Jaelani, ST, M.Sc, Ph.D
"""
)
    
st.markdown(
"""
"""
)
    
st.markdown(
"""
You can follow us on social media: [GitHub](https://github.com/putrimegi/kerjapraktek)
"""
)
st.markdown(
"""
Web App URL: https://template.streamlitapp.com                                             
GitHub Repository: https://github.com/giswqs/streamlit-multipage-template
"""
)



