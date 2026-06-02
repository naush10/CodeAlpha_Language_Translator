import streamlit as st
from deep_translator import GoogleTranslator
st.title("language translation tool")
text = st.text_area("enter text to translate")
languages = {
    "English": "en",
    "French":"fr",
    "Punjabi": "pa",
    "Spanish": "es",
    "German": "de",
    "Hindi" : "hi"
}
source = st.selectbox("source language", languages.keys())
target = st.selectbox("target language", languages.keys())
if st.button ("translate"):
    if text:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]).translate(text)
        st.success("translation completed!")
        st.write(translated)
    else:
        st.warning("please enter some text. ")