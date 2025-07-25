import streamlit as st
from PIL import Image
from utils.predict import load_model, predict, load_catalog

st.set_page_config(page_title="Fergana Flowers Classifier 🌸", layout="centered")

st.title("🌼 Fergana Flowers - Flower Identifier")
st.markdown("Upload a flower image and get details like name, price, and care tips.")

# Load model and catalog
model = load_model()
catalog = load_catalog()

# Upload section
uploaded_file = st.file_uploader("Upload a flower image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Classifying..."):
        result = predict(image, model, catalog)

    st.subheader(f"🌸 Flower: {result['name']}")
    st.write(f"💰 Price: {result['price']}")
    st.write(f"📦 Available: {'✅ Yes' if result['available'] else '❌ No'}")
    st.write(f"🪴 Care Tips: {result['care']}")
