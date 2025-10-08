---
title: Gujarati ACPC 1
emoji: 👁
colorFrom: green
colorTo: green
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Gujarati to English Translator

A **web-based application** built using **Streamlit** that transliterates English text to Gujarati script and translates Gujarati text into English using AI4Bharat's pre-trained models.

---

## **Features**
- Transliteration of English text to Gujarati script.  
- Gujarati to English translation using **Transformer-based models**.  
- Interactive web interface with **Streamlit**.  
- Supports multiple beam search options for better translation quality.  
- Preprocessing and postprocessing handled for clean, accurate output.

---

## **Tech Stack**
- **Frontend & UI**: [Streamlit](https://streamlit.io/)  
- **Translation Model**: [AI4Bharat IndicTrans2](https://huggingface.co/ai4bharat/indictrans2-indic-en-1B)  
- **Libraries & Tools**:  
  - `torch` – For model inference  
  - `transformers` – Hugging Face Transformers for sequence-to-sequence models  
  - `ai4bharat.transliteration` – Transliteration engine  
  - `IndicTransTokenizer` – For preprocessing and postprocessing Indic languages  
  - `fairseq` – Required by some models for translation  

---

## **Installation**

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

## 2. Create a virtual environment

python -m venv venv
# Activate the virtual environment
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

## Install dependencies

pip install -r requirements.txt

## Run the Streamlit app

streamlit run app.py
