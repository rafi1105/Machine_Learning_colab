import streamlit as st
import pandas as pd
import joblib
import streamlit.components.v1 as components

# Load saved model, scaler, and expected columns
model = joblib.load("RFC_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("col.pkl")

# Configure page layout
st.set_page_config(
    page_title="❤️ Heart Disease Prediction ❤️",
    page_icon="💓",
    layout="wide"
)

# Add custom CSS
st.markdown("""
<style>
    .hero-animation {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem 0;
    }
    .main-title {
        font-size: 3rem;
        text-align: center;
        color: #e74c3c;
        margin-bottom: 1rem;
        font-weight: 800;
    }
    .form-section {

        margin: 1rem 0;

    }
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1rem;
        text-align: center;
        background: linear-gradient(135deg, #e74c3c, #c0392b);
        padding: 0.8rem;
        border-radius: 10px;
    }
    .input-description {
        font-size: 1.1rem;
        color: #ffffff;
        margin-top: 0.5rem;
        font-weight: 500;
    
        display: inline-block;
    }
    .stSelectbox label, .stSlider label, .stNumberInput label {
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        color: #2c3e50 !important;
        margin-bottom: 0.5rem !important;
    }
    .predict-button {
        background: linear-gradient(135deg, #e74c3c, #c0392b);
        color: white;
        font-size: 1.2rem;
        font-weight: 600;
        padding: 0.8rem 2rem;
        border-radius: 25px;
        border: none;
        width: 100%;
        margin: 2rem 0;
        transition: all 0.3s ease;
    }
    .predict-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(231, 76, 60, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Main title
# Hero Animation in center
st.markdown('<div class="hero-animation" style="width: 100%; display: flex; justify-content: center;">', unsafe_allow_html=True)
components.html("""
<script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.6.2/dist/dotlottie-wc.js" type="module"></script>
<div style="display: flex; justify-content: center; width: 100%;">
    <dotlottie-wc src="https://lottie.host/2c378b23-9c8e-47a7-baa9-beb54e0b6a50/Aen7jKq3nj.lottie" 
        style="width: 600px; height: 500px" 
        speed="1" 
        autoplay 
        loop>
    </dotlottie-wc>
</div>
""", height=520)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">❤️ Heart Disease Prediction ❤️</h1>', unsafe_allow_html=True)


st.markdown("---")
st.markdown("## 📋 Health Assessment Form")
st.markdown("Please fill out the following information to assess your heart disease risk:")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    # Personal Information Section
    st.markdown('<div class="form-section"> ', unsafe_allow_html=True)
    st.markdown('<h3 class="section-title">👤 Personal Information</h3>', unsafe_allow_html=True)
    
    st.markdown('<div class="input-description">Your current age in years</div>', unsafe_allow_html=True)
    age = st.slider("Age", 18, 100, 40, help="Age is a major risk factor for heart disease")
    
    st.markdown('<div class="input-description">Biological sex</div>', unsafe_allow_html=True)
    sex = st.selectbox("Gender", ["Male", "Female"], help="Gender affects heart disease risk patterns")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Cardiovascular Metrics Section
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<h3 class="section-title">🫀 Cardiovascular Health</h3>', unsafe_allow_html=True)
    
    st.markdown('<div class="input-description">Type of chest pain experienced</div>', unsafe_allow_html=True)
    chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"], 
                             help="ATA: Atypical Angina, NAP: Non-Anginal Pain, TA: Typical Angina, ASY: Asymptomatic")
    
    st.markdown('<div class="input-description">Blood pressure when at rest (normal: 80-120 mmHg)</div>', unsafe_allow_html=True)
    resting_bp = st.number_input("Resting Blood Pressure (mmHg)", 80, 200, 120, 
                                help="Higher values indicate increased risk")
    
    st.markdown('<div class="input-description">Total cholesterol level in blood (normal: <200 mg/dL)</div>', unsafe_allow_html=True)
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200, 
                                 help="Higher levels increase heart disease risk")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Blood Sugar & ECG Section
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<h3 class="section-title">🩸 Blood Tests & Heart Rhythm</h3>', unsafe_allow_html=True)
    
    st.markdown('<div class="input-description">Blood sugar level after fasting</div>', unsafe_allow_html=True)
    fasting_bs = st.selectbox("Fasting Blood Sugar", [0, 1], 
                             format_func=lambda x: "Normal (≤120 mg/dL)" if x == 0 else "High (>120 mg/dL)",
                             help="High blood sugar increases heart disease risk")
    
    st.markdown('<div class="input-description">Electrocardiogram results at rest</div>', unsafe_allow_html=True)
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"], 
                              help="ST: ST-T wave abnormality, LVH: Left ventricular hypertrophy")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Exercise & Heart Performance Section
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<h3 class="section-title">⚡ Exercise & Heart Performance</h3>', unsafe_allow_html=True)
    
    st.markdown('<div class="input-description">Maximum heart rate achieved during exercise</div>', unsafe_allow_html=True)
    max_hr = st.slider("Max Heart Rate (bpm)", 60, 220, 150, 
                      help="Lower max heart rate may indicate heart problems")
    
    st.markdown('<div class="input-description">Chest pain during exercise</div>', unsafe_allow_html=True)
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["N", "Y"], 
                                  format_func=lambda x: "No" if x == "N" else "Yes",
                                  help="Chest pain during exercise is a warning sign")
    
    st.markdown('<div class="input-description">ST depression induced by exercise relative to rest</div>', unsafe_allow_html=True)
    oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0, step=0.1,
                       help="Higher values indicate potential heart problems")
    
    st.markdown('<div class="input-description">Slope of the peak exercise ST segment</div>', unsafe_allow_html=True)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"], 
                           help="Flat or Down slopes may indicate heart disease")
    st.markdown('</div>', unsafe_allow_html=True)

# Prediction Section
st.markdown("---")
st.markdown("## 🔬 Risk Analysis")

# Create centered prediction button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔬 Analyze Heart Disease Risk", key="predict_btn", help="Click to get your heart disease risk assessment"):
        # Add progress indicator
        with st.spinner('🧠 Analyzing your health data...'):
            import time
            time.sleep(1)  # Simulate processing
            
            # Create a raw input dictionary
            raw_input = {
                'Age': age,
                'RestingBP': resting_bp,
                'Cholesterol': cholesterol,
                'FastingBS': fasting_bs,
                'MaxHR': max_hr,
                'Oldpeak': oldpeak,
                'Sex_' + sex: 1,
                'ChestPainType_' + chest_pain: 1,
                'RestingECG_' + resting_ecg: 1,
                'ExerciseAngina_' + exercise_angina: 1,
                'ST_Slope_' + st_slope: 1
            }

            # Create input dataframe
            input_df = pd.DataFrame([raw_input])

            # Fill in missing columns with 0s
            for col in expected_columns:
                if col not in input_df.columns:
                    input_df[col] = 0

            # Reorder columns
            input_df = input_df[expected_columns]

            # Scale the input
            scaled_input = scaler.transform(input_df)

            # Make prediction
            prediction = model.predict(scaled_input)[0]

        # Enhanced results display
        st.markdown("---")
        st.markdown("## 📊 Your Results")
        
        if prediction == 1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #e74c3c, #c0392b); color: white; padding: 2rem; border-radius: 15px; text-align: center; margin: 1rem 0; box-shadow: 0 4px 20px rgba(231, 76, 60, 0.3);">
                <h2 style="margin: 0; font-size: 2.5rem;">⚠️ HIGH RISK</h2>
                <h4 style="margin: 0.5rem 0; font-size: 1.2rem;">Heart Disease Risk Detected</h4>
                <p style="margin: 1rem 0; font-size: 1rem; opacity: 0.9;">Please consult with a healthcare professional immediately</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Recommendations for high risk
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### 🚨 Immediate Actions")
                st.markdown("""
                - 📞 **Contact your doctor** within 24-48 hours
                - 🏥 **Schedule heart tests** (ECG, Echocardiogram)
                - 💊 **Review medications** with healthcare provider
                - 🩺 **Monitor blood pressure** daily
                """)
            
            with col2:
                st.markdown("#### 🥗 Lifestyle Changes")
                st.markdown("""
                - 🥬 **Heart-healthy diet** (low sodium, saturated fat)
                - 🚶 **Light exercise** as approved by doctor
                - 🚭 **Quit smoking** immediately if applicable
                - 😌 **Stress management** techniques
                """)
                
        else:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #27ae60, #229954); color: white; padding: 2rem; border-radius: 15px; text-align: center; margin: 1rem 0; box-shadow: 0 4px 20px rgba(39, 174, 96, 0.3);">
                <h2 style="margin: 0; font-size: 2.5rem;">✅ LOW RISK</h2>
                <h4 style="margin: 0.5rem 0; font-size: 1.2rem;">Heart Health Looks Good</h4>
                <p style="margin: 1rem 0; font-size: 1rem; opacity: 0.9;">Continue your healthy lifestyle!</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Recommendations for low risk
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### ✅ Keep It Up!")
                st.markdown("""
                - 🏃 **Regular exercise** (150 min/week)
                - 🥗 **Balanced diet** with fruits & vegetables
                - 🩺 **Annual checkups** for prevention
                - 💤 **Quality sleep** (7-9 hours)
                """)
            
            with col2:
                st.markdown("#### 📅 Prevention Tips")
                st.markdown("""
                - 🧘 **Stress management** through relaxation
                - 🚭 **Avoid smoking** and limit alcohol
                - 🧂 **Limit sodium** intake (<2300mg/day)
                - 💧 **Stay hydrated** (8 glasses water/day)
                """)
        
        # Medical disclaimer
        st.markdown("---")
        st.markdown("""
        <div style="background: #e8f4fd; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #3498db; margin: 2rem 0;">
            <h4 style="color: #2980b9; margin: 0 0 0.5rem 0;">📞 Important Medical Disclaimer</h4>
            <p style="margin: 0; color: #2c3e50; font-size: 0.95rem;">
                This AI prediction is for <strong>educational purposes only</strong> and should not replace professional medical advice. 
                Always consult qualified healthcare professionals for proper medical diagnosis and treatment. 
                If you experience chest pain, shortness of breath, or other symptoms, seek immediate medical attention.
            </p>
        </div>
        """, unsafe_allow_html=True)