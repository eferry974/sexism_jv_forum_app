import streamlit as st
import pandas as pd
import requests

#st.set_page_config(layout="wide")

'''
# Sexism detection on JV.com 18-25 forum
'''
'''
#
'''

'''
## Is this message sexist ?
'''
tweet = st.text_area(label='', value="Go on, copy paste here 18-25's finest jibber-jabber...")

#url = 'https://taxifare.lewagon.ai/predict'
#params = {
#    'tweet': f"{tweet}"
#}
#prediction = requests.get(url, params=params).json()['fare']
'''
#
'''
#col1, col2, col3 = st.columns(3)

#with col2:
if st.button('Evaluate'):
    st.write("Please implement your API!")
