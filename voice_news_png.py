import streamlit as st
import torch
import torchaudio
from TTS.api import TTS
from io import BytesIO
import datetime

# Set PNG 50th Anniversary theme colors
st.set_page_config(page_title="Voice News PNG", page_icon="🇵🇬", layout="centered")

st.markdown("""
<style>
body {
    background-color: #fffbe6;
}
.stApp {
    background-color: #fffbe6;
}
.title {
    font-size: 36px;
    font-weight: bold;
    color: #cc0000;
    text-align: center;
}
.footer {
    font-size: 14px;
    text-align: center;
    margin-top: 20px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🇵🇬 Voice News PNG</div>', unsafe_allow_html=True)
st.markdown("### 🔊 Powered by Pulse of PNG voice — 50th Anniversary Edition")

# Load the model (your own cloned voice must be stored locally or via link)
@st.cache_resource
def load_model():
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=torch.cuda.is_available())
    return tts

tts = load_model()

# Text input
news_text = st.text_area("📰 Paste your News or Story Script here:", height=200, placeholder="Write your script in Tok Pisin or English...")

speaker_wav = "your_cloned_voice.wav"  # Replace with your own path or file

if st.button("🎙️ Generate Voice"):
    if news_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating your voice..."):
            output = BytesIO()
            tts.tts_to_file(text=news_text, speaker_wav=speaker_wav, file_path="output.wav")
            audio, sr = torchaudio.load("output.wav")
            torchaudio.save("voice_news_output.wav", audio, sr)

            st.audio("voice_news_output.wav", format="audio/wav")
            with open("voice_news_output.wav", "rb") as f:
                st.download_button("⬇️ Download Voice", f, file_name=f"voice_news_{datetime.date.today()}.wav")

st.markdown('<div class="footer">Created with ❤️ for Papua New Guinea 50th Independence Anniversary</div>', unsafe_allow_html=True)
