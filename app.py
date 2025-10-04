import streamlit as st
from PIL import Image
from ocr_utils import read_text, read_words_with_boxes, draw_boxes

st.set_page_config(page_title="OCR Denemeleri", page_icon="🔎", layout="centered")
st.title("🔎 OCR Denemeleri")
st.write("Görsel yükle → metni çıkar → kelimeleri listele → kutuları çiz.")

uploaded = st.file_uploader("Bir görsel yükle (PNG/JPG)", type=["png", "jpg", "jpeg"])
lang = st.selectbox("Dil (Tesseract)", ["eng", "tur", "eng+tur"], index=0)

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Yüklenen görsel", use_container_width=True)

    if st.button("Metni Çıkar"):
        text = read_text(image, lang=lang)
        st.subheader("Metin")
        st.code(text or "(boş)")

        words = read_words_with_boxes(image, lang=lang)
        st.subheader(f"Kelime listesi ({len(words)})")
        st.write(", ".join([w for w, _ in words]) or "(kelime bulunamadı)")

        st.subheader("Kutulu görsel")
        st.image(draw_boxes(image, words), use_container_width=True)

        st.download_button("Metni .txt indir", text, file_name="ocr_output.txt")
else:
    st.info("Başlamak için bir görsel yükle.")
