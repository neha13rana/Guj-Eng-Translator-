import streamlit as st
from ai4bharat.transliteration import XlitEngine
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from IndicTransTokenizer import IndicProcessor

e = XlitEngine(["gu", 'en'], beam_width=10, src_script_type="en")
model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/indictrans2-indic-en-1B", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indictrans2-indic-en-1B", trust_remote_code=True)
ip = IndicProcessor(inference=True)

def english_to_gujarati(text):
    return e.translit_sentence(text)['gu']

def translate_question(english_question):
    gujarati_question = english_to_gujarati(english_question)
    lst = [gujarati_question]
    st.write ("Gujarati Translation of the text:", gujarati_question)
    
    batch = ip.preprocess_batch(lst, src_lang="guj_Gujr", tgt_lang="eng_Latn")
    batch = tokenizer(batch, padding="longest", truncation=True, max_length=256, return_tensors="pt")

    with torch.inference_mode():
        outputs = model.generate(**batch, num_beams=5, num_return_sequences=1, max_length=256)

    with tokenizer.as_target_tokenizer():
        outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True, clean_up_tokenization_spaces=True)

    outputs = ip.postprocess_batch(outputs, lang="eng_Latn")
    return outputs

st.title("Gujarati to English Translator")
st.write("Enter your question:")

english_question = st.text_input("Question:")

if st.button("Translate"):
    if english_question:
        translated = translate_question(english_question)
        translated_result = translated[0]
        st.write("English translation of the user text:", translated_result)
    else:
        st.write("Please enter a question.")



