import streamlit as st
import base64
import time

st.set_page_config(
    page_title="AI Iris Flower Classifier",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- SESSION ----------------

if "step" not in st.session_state:
    st.session_state.step = 0

# ---------------- ROBOT IMAGE ----------------

with open("images/ai_robot.png", "rb") as f:
    robot = base64.b64encode(f.read()).decode()

# ---------------- CSS ----------------

st.markdown("""
<style>
header, footer{ visibility:hidden; }
.block-container{ padding-top:0rem; max-width:1400px; }

/* BACKGROUND */
.stApp{
    background: linear-gradient(135deg, #050816, #08142E, #1A1B4B);
    color:white;
}

/* FLOATING PARTICLES */
.particle{ position:fixed; width:14px; height:14px; border-radius:50%; z-index:0; }
.p1{ top:15%; left:8%; background:#EC4899; box-shadow:0 0 20px #EC4899; animation:float1 5s infinite ease-in-out; }
.p2{ top:35%; left:20%; background:#06B6D4; box-shadow:0 0 20px #06B6D4; animation:float2 6s infinite ease-in-out; }
.p3{ bottom:18%; left:15%; background:#A855F7; box-shadow:0 0 20px #A855F7; animation:float3 7s infinite ease-in-out; }
.p4{ top:18%; right:10%; background:#F472B6; box-shadow:0 0 20px #F472B6; animation:float4 6s infinite ease-in-out; }
.p5{ bottom:20%; right:12%; background:#22D3EE; box-shadow:0 0 20px #22D3EE; animation:float1 8s infinite ease-in-out; }

@keyframes float1{ 0%{transform:translateY(0);} 50%{transform:translateY(-20px);} 100%{transform:translateY(0);} }
@keyframes float2{ 0%{transform:translateX(0);} 50%{transform:translateX(20px);} 100%{transform:translateX(0);} }
@keyframes float3{ 0%{transform:translateY(0);} 50%{transform:translateY(25px);} 100%{transform:translateY(0);} }
@keyframes float4{ 0%{transform:translateX(0);} 50%{transform:translateX(-25px);} 100%{transform:translateX(0);} }

/* TITLE */
.title{ text-align:center; font-size:60px; font-weight:900; color:white; margin-top:15px; text-shadow: 0 0 20px #EC4899, 0 0 40px #8B5CF6; }
.subtitle{ text-align:center; font-size:22px; color:#CBD5E1; margin-bottom:25px; }

/* ROBOT */
.robot{ text-align:center; }
.robot-img{ width:380px; display:block; margin:auto; animation:floatRobot 3s infinite ease-in-out; filter: drop-shadow(0 0 25px #06B6D4) drop-shadow(0 0 50px #3B82F6) drop-shadow(0 0 80px rgba(59,130,246,.5)); }
@keyframes floatRobot{ 0%{transform:translateY(0);} 50%{transform:translateY(-18px);} 100%{transform:translateY(0);} }

div[data-testid="stButton"]{ display:flex; justify-content:center; }
.chat-bubble{ background:#071633; padding:15px 25px; margin-bottom:15px; border-radius:20px; font-size:22px; font-weight:500; width:fit-content; max-width:500px; color:white; display:block; box-shadow: 0 0 10px #FF4FD8, 0 0 20px #FF4FD8; }

/* BUTTON */
.stButton{ display:flex; justify-content:center; }
.stButton > button{ width:250px; height:65px; background:#071633 !important; color:white !important; font-size:24px; font-weight:700; border:none; border-radius:18px; box-shadow: 0 0 15px #FF4FD8, 0 0 30px #8B5CF6; transition:.3s; }
.title{ font-size: clamp(32px,5vw,60px); }
.subtitle{ font-size: clamp(14px,2vw,22px); }
.robot-img{ width:min(320px,80vw); }
.stButton > button:hover{ transform:translateY(-3px); box-shadow: 0 0 25px #FF4FD8, 0 0 50px #8B5CF6, 0 0 80px #06B6D4; }

/* PURE CSS FADE-IN ANIMATION FOR MESSAGES */
.fade-in-text { color: white; font-size: 28px; line-height: 2; padding-top: 40px; }
.msg-line { opacity: 0; animation: fadeInAnimation 0.5s forwards; }
.m1 { animation-delay: 0.2s; }
.m2 { animation-delay: 1.0s; }
.m3 { animation-delay: 1.8s; }
.m4 { animation-delay: 2.6s; }
@keyframes fadeInAnimation { to { opacity: 1; } }

@media(max-width:768px){ .title{ font-size:36px; } .subtitle{ font-size:16px; } .robot-img{ width:280px; } }
</style>
""", unsafe_allow_html=True)

# ---------------- PARTICLES ----------------
st.markdown("""
<div class="particle p1"></div>
<div class="particle p2"></div>
<div class="particle p3"></div>
<div class="particle p4"></div>
<div class="particle p5"></div>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("""
<div class='title'>🌸 AI Iris Flower Classifier</div>
<div class='subtitle'>Powered by Machine Learning & Intelligent Prediction</div>
""", unsafe_allow_html=True)

# ---------------- CONTROL FLOW ----------------
if st.session_state.step == 0:
    st.markdown(f"""
    <div class='robot'><img class='robot-img' src='data:image/png;base64,{robot}'></div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c2:
        if st.button("👋 Hey"):
            st.session_state.step = 1
            st.rerun()
    st.stop()

elif st.session_state.step == 1:
    left, right = st.columns([1, 1.2])

    with left:
        st.markdown(f"""
        <div class='robot'><img class='robot-img' src='data:image/png;base64,{robot}'></div>
        """, unsafe_allow_html=True)
        st.write("")
        c1, c2, c3 = st.columns(3)
        with c2:
            start_btn = st.button("🚀 Start Prediction", key="predict_btn")

    with right:
        st.markdown(
            """
            <div class="fade-in-text">
                <div class="msg-line m1">👋 Hi, I'm Iris AI</div><br>
                <div class="msg-line m2">🌸 Welcome to the Iris Flower Classification System</div><br>
                <div class="msg-line m3">⚡ I can analyze flower measurements instantly</div><br>
                <div class="msg-line m4">🚀 Click Start Prediction to begin</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if start_btn:
        # కరెక్ట్ పేజీ స్విచ్చింగ్ పాత్ (ఫోల్డర్ పేరు తీసేసి కేవలం ఫైల్ పేరు ఇవ్వాలి)
        st.switch_page("pages/Dashboard.py")
