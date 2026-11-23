import streamlit as st
import pandas as pd
from PIL import Image
from src.vision import analyse_image, demo_classify
from src.history import add_record, load_history, clear_history

st.set_page_config(page_title="SmartVision AI", page_icon="👁️", layout="wide")
st.title("👁️ SmartVision AI")
st.caption("Image intelligence and classification research prototype")
st.info("This is an educational prototype. Its built-in classifier uses simple image features, not a trained deep-learning model. Do not use it for safety-critical decisions.")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Image Analysis", "Demo Classifier", "History", "About"])

if page == "Image Analysis":
    st.subheader("Upload an image")
    uploaded = st.file_uploader("Choose JPG, JPEG or PNG", type=["jpg", "jpeg", "png"])
    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        st.image(image, caption="Uploaded image", use_container_width=True)
        result = analyse_image(image)
        a, b, c = st.columns(3)
        a.metric("Image width", f'{result["width"]} px')
        b.metric("Image height", f'{result["height"]} px')
        c.metric("Brightness", f'{result["brightness"]:.3f}')
        st.subheader("Image quality report")
        st.json(result)
        add_record(uploaded.name, result["width"], result["height"], result["brightness"], result["contrast"])
        st.caption("Quality analysis only: no semantic object detection is performed on this page.")

elif page == "Demo Classifier":
    st.subheader("Rule-based demo classification")
    st.write("This demo illustrates a prediction workflow using image statistics. It does not recognize actual image contents.")
    brightness = st.slider("Brightness", 0.0, 1.0, 0.50, 0.01)
    contrast = st.slider("Contrast", 0.0, 1.0, 0.25, 0.01)
    label, score, explanation = demo_classify(brightness, contrast)
    x, y = st.columns(2)
    x.metric("Demo category", label)
    y.metric("Heuristic score", f"{score:.1%}")
    st.progress(score)
    st.write(explanation)
    st.warning("The score is a rule-based illustrative value, not a calibrated probability.")

elif page == "History":
    st.subheader("Recent image analysis history")
    records = load_history()
    if records:
        st.dataframe(pd.DataFrame(records), use_container_width=True, hide_index=True)
        if st.button("Clear history"):
            clear_history()
            st.rerun()
    else:
        st.write("No analyses saved yet. Upload an image in Image Analysis.")

else:
    st.subheader("Project overview")
    st.markdown("""
    **SmartVision AI** is a starter project for learning computer vision application development.

    Modules:
    - Image loading and preprocessing
    - Brightness and contrast analysis
    - Rule-based demo prediction workflow
    - Local analysis history
    - Streamlit dashboard

    **Suggested research extension:** integrate a properly trained and validated image classifier, document the dataset and licensing, and evaluate macro-F1, precision, recall, confusion matrix, latency and calibration.
    """)
