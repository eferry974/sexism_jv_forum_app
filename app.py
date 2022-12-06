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
text = st.text_area(label='', placeholder="Paste here 18-25's finest jibber-jabber...")

url = 'https://jvcom-lncm5vxigq-ew.a.run.app/pred'
params = {
    'text': f"{text}"
}

#proba = requests.get(url, params=params).json()['proba']
'''
#
'''
#col1, col2, col3 = st.columns(3)

#with col2:
if st.button('Evaluate'):
    '''
    #
    '''
    type = requests.get(url, params=params).json()['type']
    if type == 0:
        st.write(f'### ✅ This message is NOT considered SEXIST by our model.')
        #st.write(proba)
    else:
        st.write(f'### 🟥 This message is considered SEXIST by our model.')
        #st.write(proba)
