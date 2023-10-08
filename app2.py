import streamlit as st
from googletrans import Translator

translator = Translator()

Indian_lang = {
    'Hindi': 'hi',
    'Marathi': 'mr',
    'Bengali': 'bn',
    'Gujarati': 'gu',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Kannada': 'kn',
    'Punjabi': 'pa',
    'Sindhi': 'sd',
    'Urdu': 'ur'
}

other_lang = {
    'English': 'en',
    'Japanese': 'ja',
    'French': 'fr',
    'Chinese': 'zh-cn',
    'Italian': 'it'
}

st.title('Text Translator')

text = st.text_area("Enter Text")

selection = st.radio('Select a language', ['Indian_Lang', 'Other_Lang'])

if selection == 'Indian_Lang':
    lang_to_be_used = st.selectbox('Select the Language', list(Indian_lang.keys()))
    select_lang = Indian_lang[lang_to_be_used]
else:
    lang_to_be_used = st.selectbox('Select the Language', list(other_lang.keys()))
    select_lang = other_lang[lang_to_be_used]

if st.button('Translate'):
    if text:
        output = translator.translate(text, dest=select_lang).text
        st.markdown(f'<p style="font-size:40px; color:Grey; ">{output}</p>',unsafe_allow_html=True)
        #st.write('Translated Text:', output)
