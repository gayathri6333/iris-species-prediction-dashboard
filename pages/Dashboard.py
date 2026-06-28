import streamlit as st
import time
import joblib
import base64

st.set_page_config(
    page_title="Prediction Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- MODEL CONFIGURATION ----------------
@st.cache_resource
def load_iris_model():
    try:
        return joblib.load("models/model.joblib")
    except:
        return None

model = load_iris_model()

# Helper function to convert local images to clean HTML base64 strings
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# ---------------- DASHBOARD STYLING ----------------
st.markdown("""
<style>
            
            
header, footer { visibility: hidden !important; display: none !important; }
.block-container { padding-top: 2rem !important; max-width: 1400px; margin: auto; }

/* THE OVERRIDE CORE BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #050816, #08142E, #1A1B4B) !important;
    color: white !important;
}

/* ❌ ABSOLUTELY ERASE HOME PAGE ARTIFACTS AND EXTRA WRAPPERS ❌ */
[class*="chat-bubble"], [class*="particle"], [class*="hp"], [class*="p1"], [class*="p2"], [class*="p3"] {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
}

/* SHADOW CARDS */
.custom-card {
    background: rgba(7, 22, 51, 0.6);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255, 79, 216, 0.25);
    box-shadow: 0 0 25px rgba(139, 92, 246, 0.15);
    margin-bottom: 20px;
}

.result-card {
    background: linear-gradient(135deg, #0D1B3E, #1B1235);
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    border: 2px solid #06B6D4;
    box-shadow: 0 0 35px rgba(6, 182, 212, 0.35);
    margin-bottom: 25px;
}

/* SLIDERS SETUP */
.stSlider label p {
    color: white !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}

/* COMPACT ACTION BUTTONS SETUP */
div[data-testid="stHeader"] + div button, .stButton > button {
    width: 100% !important;
    max-width: 320px !important; 
    height: 65px !important;
    background: linear-gradient(90deg, #FF4FD8, #8B5CF6) !important;
    color: white !important;
    font-size: 28px !important; 
    font-weight: 800 !important;
    border: none !important;
    border-radius: 14px !important;
    box-shadow: 0 0 15px rgba(255, 79, 216, 0.4) !important;
    transition: 0.3s !important;
    margin: 0 auto !important;
    display: block !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 25px rgba(6, 182, 212, 0.6) !important;
}

/* 🌟 PURE HTML MODERN FLOWER DISPLAY CARDS (NO STREAMLIT WRAPPER CIRCLES) 🌟 */
.html-flower-showcase {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
    width: 100%;
}

.html-flower-frame {
    background: rgba(13, 27, 62, 0.4);
    padding: 15px;
    border-radius: 28px;
    border: 2px solid rgba(139, 92, 246, 0.6);
    box-shadow: 0 0 30px rgba(139, 92, 246, 0.4);
    max-width: 320px;
    text-align: center;
}

.html-flower-frame img {
    width: 100%;
    border-radius: 20px;
    display: block;
    margin-bottom: 10px;
}

.html-flower-frame span {
    color: #CBD5E1;
    font-size: 14px;
    font-weight: 500;
}

/* SAFE FOOTER NAVIGATION */
div.element-container:has(button[key="back_home_left"]) {
    display: flex !important;
    justify-content: flex-start !important;
    width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- RESPONSE LAYOUT CHANNELS ----------------
col1, col2 = st.columns([1.1, 1], gap="large")

with col1:
    st.markdown("""
    <div class='custom-card'>
        <h2 style='color: #06B6D4; margin: 0 0 25px 0; padding: 0; font-size: 36px; font-weight: 800;'>
            📐 Input Features (cm)
        </h2>
    """, unsafe_allow_html=True)
    
    sepal_length = st.slider("Sepal Length", 0.0, 8.0, 0.0, step=0.1)
    sepal_width = st.slider("Sepal Width", 0.0, 4.5, 0.0, step=0.1)
    petal_length = st.slider("Petal Length", 0.0, 7.0, 0.0, step=0.1)
    petal_width = st.slider("Petal Width", 0.0, 2.5, 0.0, step=0.1)
    
    st.markdown("<br>", unsafe_allow_html=True)
    predict_clicked = st.button("🔮 Predict Species")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if predict_clicked:
        with st.spinner("🤖 AI is analyzing features..."):
            time.sleep(1.2)
        
        predicted_species = "Iris-Versicolor"
        confidence = "Available"
        
        if model is not None:
            try:
                features = [[sepal_length, sepal_width, petal_length, petal_width]]
                prediction = model.predict(features)
                
                # ఉదాహరణకు [0] వస్తే, అందులోని మొదటి వాల్యూ (0) ని మాత్రం తీసుకుంటుంది
                if hasattr(prediction, "__len__") and len(prediction) > 0:
                    pred_val = prediction[0]
                else:
                    pred_val = prediction

                species_mapping = {0: "Iris-Setosa", 1: "Iris-Versicolor", 2: "Iris-Virginica"}
                
                # ఇండెక్స్ నంబర్ ఆధారంగా పేరును మార్చడం
                try:
                    predicted_species = species_mapping[int(pred_val)]
                except:
                    predicted_species = str(pred_val)
                
                # కాన్ఫిడెన్స్ స్కోర్ (Probability) లెక్కించడం
                try:
                    prob = model.predict_proba(features)
                    confidence = f"{max(prob[0]) * 100:.1f}%"
                except:
                    confidence = "Not Available"
            except Exception as e:
                predicted_species = f"Error: {str(e)}"
        
        # Result visual card render
        st.markdown(f"""
        <div class='result-card'>
            <h2 style='color: #FF4FD8; font-size: 30px; margin-top:0;'>✨ Prediction Result</h2>
            <p style='font-size: 16px; color: #CBD5E1;'>The model identified the species as:</p>
            <h1 style='font-size: 40px; color: #06B6D4; margin: 15px 0; text-shadow: 0 0 10px #06B6D4;'>
                {predicted_species}
            </h1>
            <div style='background: rgba(6, 182, 212, 0.1); padding: 10px 20px; border-radius: 10px; display: inline-block;'>
                <span style='color: #06B6D4; font-weight: bold;'>Confidence Score: {confidence}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Determine paths and labels
        clean_name = predicted_species.lower()
        if "setosa" in clean_name:
            img_path, caption_str = "images/setosa.jpg", "Iris Setosa"
        elif "virginica" in clean_name:
            img_path, caption_str = "images/virginica.jpg", "Iris Virginica"
        else:
            img_path, caption_str = "images/versicolor.jpg", "Iris Versicolor"
            
        b64_data = get_image_base64(img_path)
        
        st.markdown(f"""
        <div class='html-flower-showcase'>
            <div class='html-flower-frame'>
                <img src='data:image/jpeg;base64,{b64_data}'>
                <span>{caption_str}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div style='border: 2px dashed rgba(255,255,255,0.1); padding: 80px; border-radius: 25px; text-align: center; color: #64748B;'>
            <span style='font-size: 60px;'>📊</span>
            <h3 style='margin-top: 15px; color: #CBD5E1;'>Awaiting Input</h3>
            <p style='font-size: 14px;'>Adjust the metrics on the left column and trigger 'Predict Species' to view classifications.</p>
        </div>
        """, unsafe_allow_html=True)
