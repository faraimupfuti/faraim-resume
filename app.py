import streamlit as st
from datetime import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Farai Mupfuti | Data Scientist",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for elegant styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
    }
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        font-weight: 400;
        opacity: 0.95;
        margin-bottom: 2rem;
    }
    
    .cert-badge {
        background: rgba(255,255,255,0.2);
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        display: inline-block;
        margin: 0.5rem;
        font-weight: 500;
        backdrop-filter: blur(10px);
    }
    
    .section-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .section-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
        margin-bottom: 1.5rem;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
    }
    
    .skill-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        margin: 0.3rem;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    .project-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateX(10px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    .project-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.5rem;
    }
    
    .project-description {
        color: #4a5568;
        margin-bottom: 1rem;
        line-height: 1.6;
    }
    
    .project-link {
        background: #667eea;
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .project-link:hover {
        background: #764ba2;
        transform: scale(1.05);
    }
    
    .experience-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        border-left: 4px solid #48bb78;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    }
    
    .experience-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #2d3748;
    }
    
    .experience-company {
        font-size: 1.1rem;
        color: #667eea;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .experience-period {
        color: #718096;
        font-style: italic;
        margin-bottom: 1rem;
    }
    
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    
    .contact-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 1rem;
    }
    
    .contact-item {
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }
    
    .contact-item a {
        color: white;
        text-decoration: none;
        font-weight: 500;
    }
    
    .contact-item a:hover {
        text-decoration: underline;
    }
    
    .stDownloadButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] .css-1d391kg {
        color: white;
    }
    
    .sidebar-content {
        color: white;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
    st.image("https://via.placeholder.com/150", caption="Farai Mupfuti")
    st.markdown("### 🎯 Navigation")
    page = st.radio("", ["🏠 Home", "👤 About", "💼 Experience", "🎓 Education", "🚀 Projects", "🛠️ Skills", "📞 Contact"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📱 Connect")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/faraimupfuti)")
    st.markdown("[💻 GitHub](https://github.com/faraimupfuti)")
    st.markdown("[📧 Email](mailto:faraimupfuti@gmail.com)")

# Hero Section (visible on all pages)
st.markdown("""
    <div class="hero-section">
        <div class="hero-title">Farai Mupfuti</div>
        <div class="hero-subtitle">Data Scientist | ML Engineer | Bioinformatics Specialist</div>
        <div>
            <span class="cert-badge">🎓 MSc Bioinformatics</span>
            <span class="cert-badge">☁️ Azure Data Scientist</span>
            <span class="cert-badge">🤖 ML Expert</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Home Page
if page == "🏠 Home":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">20+</div>
                <div class="stat-label">Projects Delivered</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">1TB+</div>
                <div class="stat-label">Data Processed</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">5+</div>
                <div class="stat-label">Years Experience</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="section-card">
            <h2 class="section-title">🎯 Professional Summary</h2>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #4a5568;">
                Accomplished Data Scientist and Machine Learning Engineer with a <strong>Master's degree in Bioinformatics</strong> 
                from the University of Tübingen and <strong>Azure Data Scientist Associate certification</strong>. 
                Specialized in building scalable ML solutions for healthcare, fraud detection, and drug discovery using 
                advanced deep learning, cloud computing, and bioinformatics techniques.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #4a5568;">
                Currently working as a <strong>Data Scientist at Citadel Analytics</strong>, developing AI-powered fraud detection 
                systems for enterprise clients. Proven track record of delivering 20+ ML projects across healthcare AI, 
                computer vision, NLP, and data analytics domains.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="section-card">
            <h2 class="section-title">🏆 Key Achievements</h2>
            <ul style="font-size: 1.1rem; line-height: 2; color: #4a5568;">
                <li>🎯 Built skin cancer detection model with <strong>94% accuracy</strong>, enabling early diagnosis</li>
                <li>💊 Accelerated drug discovery by <strong>60%</strong> using AI-powered molecular analysis</li>
                <li>🗣️ Achieved <strong>96% accuracy</strong> in real-time speech recognition with sub-second latency</li>
                <li>📊 Optimized TV advertising spend resulting in <strong>45% ROI improvement</strong></li>
                <li>🎯 Increased marketing effectiveness by <strong>35%</strong> through customer segmentation</li>
                <li>🔍 Developed fraud detection ML models for enterprise clients at Citadel Analytics</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# About Page
elif page == "👤 About":
    st.markdown("""
        <div class="section-card">
            <h2 class="section-title">About Me</h2>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #4a5568;">
                I'm a passionate Data Scientist with a unique blend of expertise in <strong>bioinformatics, 
                machine learning, and cloud computing</strong>. With a Master's degree in Bioinformatics from 
                the University of Tübingen (2025) and Azure Data Scientist Associate certification, I specialize 
                in building intelligent systems that solve real-world problems.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #4a5568;">
                My expertise spans from <strong>healthcare AI and drug discovery</strong> to <strong>fraud detection 
                and business intelligence</strong>. I've successfully delivered projects in computer vision, 
                natural language processing, predictive analytics, and real-time ML systems.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #4a5568;">
                Currently, I'm leveraging my skills at <strong>Citadel Analytics</strong> to build sophisticated 
                fraud detection systems using cutting-edge machine learning algorithms, helping organizations 
                protect themselves against financial crimes.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="section-card">
            <h2 class="section-title">🎯 Areas of Expertise</h2>
            <div style="font-size: 1.1rem; line-height: 2; color: #4a5568;">
                <strong>🧬 Bioinformatics & Healthcare AI</strong><br>
                • Drug discovery and molecular modeling<br>
                • Medical image analysis and disease prediction<br>
                • Genomics and clinical data analysis<br><br>
                
                <strong>🤖 Machine Learning & AI</strong><br>
                • Deep learning (CNN, RNN, Transformers)<br>
                • Computer vision and NLP<br>
                • Fraud detection and anomaly detection<br>
                • Predictive modeling and time series analysis<br><br>
                
                <strong>☁️ Cloud & Data Engineering</strong><br>
                • Azure ML, Databricks, Synapse Analytics<br>
                • ETL pipelines and data orchestration<br>
                • Real-time processing and model deployment<br><br>
                
                <strong>📊 Data Analytics & Visualization</strong><br>
                • Power BI, Tableau, Looker Studio<br>
                • Statistical analysis and A/B testing<br>
                • Dashboard development and reporting
            </div>
        </div>
    """, unsafe_allow_html=True)

# Experience Page
elif page == "💼 Experience":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>💼 Professional Experience</h2>", unsafe_allow_html=True)
    
    # Current role at Citadel Analytics
    st.markdown("""
        <div class="experience-card">
            <div class="experience-title">🔍 Data Scientist</div>
            <div class="experience-company">Citadel Analytics</div>
            <div class="experience-period">May 2025 - Present</div>
            <ul style="color: #4a5568; line-height: 1.8;">
                <li>Develop and deploy machine learning models for fraud detection and financial crime prevention</li>
                <li>Build anomaly detection systems using advanced ML algorithms (XGBoost, Random Forest, Neural Networks)</li>
                <li>Analyze large-scale transaction data to identify suspicious patterns and behaviors</li>
                <li>Create real-time fraud scoring models integrated with client systems</li>
                <li>Collaborate with cross-functional teams to implement AI-driven security solutions</li>
                <li>Optimize model performance and reduce false positive rates through iterative refinement</li>
                <li>Present findings and insights to clients through data visualizations and reports</li>
            </ul>
            <div>
                <span class="skill-badge">Fraud Detection</span>
                <span class="skill-badge">Machine Learning</span>
                <span class="skill-badge">Anomaly Detection</span>
                <span class="skill-badge">XGBoost</span>
                <span class="skill-badge">Python</span>
                <span class="skill-badge">Financial Analytics</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Previous role at Innovent
    st.markdown("""
        <div class="experience-card">
            <div class="experience-title">📊 Data Analyst</div>
            <div class="experience-company">Innovent South Africa</div>
            <div class="experience-period">2022 - 2025</div>
            <ul style="color: #4a5568; line-height: 1.8;">
                <li>Systematically collected, processed, and performed statistical analyses on large datasets</li>
                <li>Extracted practical insights and communicated findings effectively to stakeholders</li>
                <li>Identified trends, patterns, and growth opportunities through complex data analysis</li>
                <li>Built predictive models to forecast customer churn with 85%+ accuracy</li>
                <li>Proactively analyzed data to answer key questions about business performance drivers</li>
                <li>Developed comprehensive dashboards and generated regular reports for business teams</li>
                <li>Collaborated with product and marketing teams to optimize business strategies</li>
            </ul>
            <div>
                <span class="skill-badge">Data Analysis</span>
                <span class="skill-badge">Predictive Modeling</span>
                <span class="skill-badge">SQL</span>
                <span class="skill-badge">Python</span>
                <span class="skill-badge">Power BI</span>
                <span class="skill-badge">Statistical Analysis</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # System Administrator role
    st.markdown("""
        <div class="experience-card">
            <div class="experience-title">⚙️ System Administrator</div>
            <div class="experience-company">Qrent Zimbabwe</div>
            <div class="experience-period">2017 - 2022</div>
            <ul style="color: #4a5568; line-height: 1.8;">
                <li>Administered enterprise IT infrastructure with Windows and Linux servers</li>
                <li>Established robust security frameworks and conducted proactive system monitoring</li>
                <li>Streamlined operations through automation scripts and infrastructure optimization</li>
                <li>Managed user provisioning, access controls, and technical support</li>
                <li>Coordinated infrastructure upgrades and developed business continuity strategies</li>
                <li>Ensured compliance with cybersecurity standards and regulatory requirements</li>
            </ul>
            <div>
                <span class="skill-badge">System Administration</span>
                <span class="skill-badge">Linux</span>
                <span class="skill-badge">Windows Server</span>
                <span class="skill-badge">Networking</span>
                <span class="skill-badge">Security</span>
                <span class="skill-badge">Automation</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # ICT Officer role
    st.markdown("""
        <div class="experience-card">
            <div class="experience-title">💻 ICT Officer</div>
            <div class="experience-company">Jairos Jiri Association</div>
            <div class="experience-period">2014 - 2017</div>
            <ul style="color: #4a5568; line-height: 1.8;">
                <li>Managed and maintained organizational IT infrastructure including networks and hardware</li>
                <li>Provided technical support to end-users and troubleshot system issues</li>
                <li>Implemented cybersecurity protocols and data backup procedures</li>
                <li>Coordinated software installations, updates, and compliance with IT policies</li>
                <li>Collaborated with teams to optimize technology solutions and improve efficiency</li>
            </ul>
            <div>
                <span class="skill-badge">IT Support</span>
                <span class="skill-badge">Network Management</span>
                <span class="skill-badge">Cybersecurity</span>
                <span class="skill-badge">Technical Support</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Education Page
elif page == "🎓 Education":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>🎓 Education & Certifications</h2>", unsafe_allow_html=True)
    
    # Master's Degree in Bioinformatics
    st.markdown("""
        <div class="experience-card" style="border-left: 4px solid #667eea;">
            <div class="experience-title">🧬 Master of Science in Bioinformatics</div>
            <div class="experience-company">University of Tübingen, Germany</div>
            <div class="experience-period">2025</div>
            <p style="color: #4a5568; line-height: 1.8; margin-top: 1rem;">
                Advanced graduate degree focusing on computational biology, genomics, drug discovery, 
                and machine learning applications in biological systems. Specialized in AI-powered 
                drug repurposing, molecular modeling, and bioinformatics algorithms.
            </p>
            <div>
                <span class="skill-badge">Bioinformatics</span>
                <span class="skill-badge">Computational Biology</span>
                <span class="skill-badge">Genomics</span>
                <span class="skill-badge">Drug Discovery</span>
                <span class="skill-badge">Machine Learning</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Bachelor's Degree
    st.markdown("""
        <div class="experience-card" style="border-left: 4px solid #48bb78;">
            <div class="experience-title">🎓 Bachelor of Science</div>
            <div class="experience-company">Catholic University of Zimbabwe</div>
            <div class="experience-period">2010 - 2014</div>
            <p style="color: #4a5568; line-height: 1.8; margin-top: 1rem;">
                Specialized in <strong>Information Systems and Business Management</strong>, combining 
                technical expertise with business acumen. Developed strong foundation in data management, 
                systems analysis, and business strategy.
            </p>
            <div>
                <span class="skill-badge">Information Systems</span>
                <span class="skill-badge">Business Management</span>
                <span class="skill-badge">Data Management</span>
                <span class="skill-badge">Systems Analysis</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><h3 style='color: #667eea; margin-top: 2rem;'>🏆 Professional Certifications</h3>", unsafe_allow_html=True)
    
    # Azure Data Scientist Certification
    st.markdown("""
        <div class="experience-card" style="border-left: 4px solid #0078d4;">
            <div class="experience-title">☁️ Azure Data Scientist Associate</div>
            <div class="experience-company">Microsoft</div>
            <div class="experience-period">2025</div>
            <p style="color: #4a5568; line-height: 1.8; margin-top: 1rem;">
                Certified in designing and implementing data science solutions on Azure cloud platform. 
                Expertise in Azure ML, automated ML, model deployment, and MLOps practices.
            </p>
            <div>
                <span class="skill-badge">Azure ML</span>
                <span class="skill-badge">MLOps</span>
                <span class="skill-badge">Cloud Computing</span>
                <span class="skill-badge">Model Deployment</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # AWS Certification
    st.markdown("""
        <div class="experience-card" style="border-left: 4px solid #ff9900;">
            <div class="experience-title">☁️ AWS Solutions Architect Associate</div>
            <div class="experience-company">Amazon Web Services</div>
            <div class="experience-period">2021</div>
            <p style="color: #4a5568; line-height: 1.8; margin-top: 1rem;">
                Certified in designing and deploying scalable, highly available systems on AWS. 
                Focus on cloud architecture, security, and best practices.
            </p>
            <div>
                <span class="skill-badge">AWS</span>
                <span class="skill-badge">Cloud Architecture</span>
                <span class="skill-badge">System Design</span>
                <span class="skill-badge">Security</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Projects Page
elif page == "🚀 Projects":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>🚀 Featured Projects</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #4a5568; font-size: 1.1rem; margin-bottom: 2rem;'>Real-world applications of data science and machine learning across healthcare, AI, and analytics domains.</p>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "🔬 Skin Cancer Classification - Computer Vision",
            "description": "Advanced computer vision model for automated skin cancer detection and classification using deep learning techniques. Achieved 94% accuracy in skin lesion classification, potentially enabling early detection through accessible AI-powered screening.",
            "tags": ["Machine Learning", "Computer Vision", "Deep Learning", "CNN", "TensorFlow", "Medical AI", "Hugging Face"],
            "impact": "Achieved 94% accuracy, potentially saving lives through early detection",
            "link": "https://faraimupfuti-skin-cancer-image-classification.hf.space/"
        },
        {
            "title": "💊 AI-Powered Drug Discovery Platform",
            "description": "Advanced pharmaceutical research platform using artificial intelligence for drug discovery and development, integrating BioGPT for literature analysis, molecular representation, and therapeutic compound identification.",
            "tags": ["AI", "Drug Discovery", "BioGPT", "Bioinformatics", "Cheminformatics", "NLP", "Pharmaceutical AI"],
            "impact": "Accelerated drug discovery by 60% through AI-powered molecular analysis",
            "link": "https://faraimupfuti-drug-discovery-using-ai.hf.space/"
        },
        {
            "title": "🗣️ Real-time Speech Recognition System",
            "description": "State-of-the-art real-time speech recognition system using Whisper models, deployed for instant audio-to-text conversion with high accuracy and low latency.",
            "tags": ["Machine Learning", "Speech Recognition", "NLP", "Transformers", "Whisper", "PyTorch", "Real-time"],
            "impact": "96% accuracy with sub-second latency for accessible communication",
            "link": "https://faraimupfuti-real-time-speech-recognition.hf.space/"
        },
        {
            "title": "🩺 Skin Cancer Risk Prediction Model",
            "description": "Machine learning model for skin cancer risk prediction using clinical data and patient history, enabling early intervention and preventive care for high-risk patients.",
            "tags": ["Machine Learning", "Healthcare AI", "XGBoost", "Predictive Modeling", "Risk Assessment"],
            "impact": "91% accuracy enabling early intervention for high-risk patients",
            "link": "https://huggingface.co/spaces/faraimupfuti/Skin_Cancer.Prediction"
        },
        {
            "title": "💬 Diabetes Healthcare Chatbot",
            "description": "Interactive AI-powered chatbot for diabetes management and health consultation, providing 24/7 patient support with personalized health recommendations.",
            "tags": ["Machine Learning", "NLP", "Transformers", "Healthcare AI", "Chatbot Development"],
            "impact": "500+ users served with 92% satisfaction rate",
            "link": "https://faraimupfuti-diabetes-chat-model.hf.space/"
        },
        {
            "title": "😊 Facial Emotion Detection System",
            "description": "Real-time facial emotion recognition using deep learning models for instant emotion analysis from images and video streams across 7 emotion categories.",
            "tags": ["Computer Vision", "Deep Learning", "CNN", "OpenCV", "TensorFlow", "Emotion Recognition"],
            "impact": "93% accuracy enabling mental health and customer experience applications",
            "link": "https://faraimupfuti-facial-emotion-detection.hf.space/"
        },
        {
            "title": "📊 Customer Segmentation Analysis",
            "description": "Advanced machine learning project implementing RFM analysis and clustering algorithms to identify distinct customer segments for targeted marketing strategies.",
            "tags": ["Python", "K-means", "RFM Analysis", "Machine Learning", "Marketing Analytics"],
            "impact": "35% increase in marketing campaign effectiveness",
            "link": "https://julius.ai/s/notebooks/ee7cdbcf-3caf-4689-9282-0d407e4aa400"
        },
        {
            "title": "📺 TV Ad Performance Analytics - Google Looker",
            "description": "Comprehensive television advertising performance dashboard tracking campaign effectiveness, audience reach, and ROI metrics across networks.",
            "tags": ["Google Looker Studio", "TV Analytics", "Media Planning", "Data Visualization", "ROI Analysis"],
            "impact": "45% ROI improvement and 30% increase in audience engagement",
            "link": "https://lookerstudio.google.com/s/sUCyKzwvsCE"
        },
        {
            "title": "📈 Tesla Stock Analysis - Databricks",
            "description": "Financial analytics dashboard analyzing Tesla stock movements, trading patterns, and market trends using Databricks with real-time processing.",
            "tags": ["Databricks", "Apache Spark", "Python", "Financial Analytics", "Time Series", "Delta Lake"],
            "impact": "85% accuracy in trend prediction for data-driven investment decisions",
            "link": "https://dbc-787daf76-9c88.cloud.databricks.com/dashboardsv3/01f0559d1c2714f9975819762c41890d/published"
        },
        {
            "title": "🌍 US Aid Funding in Africa - Tableau",
            "description": "Interactive Tableau dashboard analyzing US foreign aid distribution across African countries with comprehensive visualizations of funding patterns.",
            "tags": ["Tableau", "Data Visualization", "Geospatial Analysis", "Public Policy Analytics"],
            "impact": "Enhanced transparency in foreign aid allocation",
            "link": "https://public.tableau.com/authoring/farai_USFUNDEDAIDAfrica/Dashboard1"
        },
        {
            "title": "🏥 Meningitis & Neonatal Sepsis Tracker",
            "description": "Public health surveillance dashboard tracking meningitis and neonatal sepsis cases, providing insights for healthcare policy and intervention strategies.",
            "tags": ["Tableau", "Public Health", "Epidemiology", "Healthcare Analytics", "Disease Surveillance"],
            "impact": "Data-driven public health decision making and resource allocation",
            "link": "https://public.tableau.com/authoring/faraiMeningitisneonatalsepsis/CasesandDeaths"
        },
        {
            "title": "⚔️ Political Conflict in Africa Dashboard",
            "description": "Geopolitical analysis dashboard tracking political conflicts, civil unrest, and security incidents across African nations.",
            "tags": ["Tableau", "Geopolitical Analysis", "Conflict Mapping", "Security Analytics"],
            "impact": "Enhanced understanding of conflict patterns for policy makers",
            "link": "https://public.tableau.com/authoring/Farai-PoliticalconflictinAfrica/Story1"
        },
        {
            "title": "🌐 Internet Usage in Africa Analysis",
            "description": "Digital connectivity analysis tracking internet penetration, usage patterns, and digital infrastructure development across Africa.",
            "tags": ["Tableau", "Digital Analytics", "Telecommunications", "Infrastructure Mapping"],
            "impact": "Informed digital policy and infrastructure investment strategies",
            "link": "https://public.tableau.com/authoring/faraiInternetUsageinAfrica/Africa"
        },
        {
            "title": "📊 Marketing Website Analytics - Google",
            "description": "Comprehensive web analytics dashboard tracking marketing performance, user behavior, and conversion metrics.",
            "tags": ["Google Analytics", "Looker Studio", "Web Analytics", "Conversion Tracking"],
            "impact": "40% improvement in marketing ROI",
            "link": "https://lookerstudio.google.com/reporting/323a553e-802f-429f-927e-c335e44d6f75"
        },
        {
            "title": "🌍 Human Development Index - Databricks",
            "description": "Global HDI trends analysis using Databricks with interactive dashboards and predictive modeling for development indicators.",
            "tags": ["Databricks", "Apache Spark", "Python", "Statistical Analysis", "Machine Learning"],
            "impact": "Data-driven policy recommendations for development organizations",
            "link": "https://dbc-787daf76-9c88.cloud.databricks.com/dashboardsv3/01f0559536101c31a8d13231e1282484/published"
        },
        {
            "title": "🎵 Spotify & YouTube Data Analysis",
            "description": "Music streaming patterns analysis comparing Spotify and YouTube platforms using advanced statistical methods.",
            "tags": ["Python", "Matplotlib", "Pandas", "Streamlit", "Music Analytics"],
            "impact": "Revealed key insights into music consumption patterns",
            "link": "https://farai-spotify-youtube-6uqw7wxdt8c-demo.streamlit.app/"
        },
        {
            "title": "🎬 Movie Dataset Analysis - TMDB",
            "description": "TMDB movie metadata analysis exploring box office performance, genre trends, and industry insights.",
            "tags": ["Python", "Matplotlib", "Pandas", "Streamlit", "Movie Analytics"],
            "impact": "Identified key factors driving movie success",
            "link": "https://farai-movies-dataset-fl8cdutz7we.streamlit.app/"
        },
        {
            "title": "👶 Minimum Working Age Analysis",
            "description": "Interactive data analysis of minimum working age regulations across different regions.",
            "tags": ["Python", "Pandas", "Streamlit", "Data Analysis"],
            "impact": "Streamlined age regulation compliance analysis",
            "link": "https://urban-train-5g64599x55j2vgvv-8501.app.github.dev/"
        },
        {
            "title": "🔍 Pandas EDA Toolkit",
            "description": "Comprehensive exploratory data analysis toolkit with interactive visualizations and statistical insights.",
            "tags": ["Python", "Pandas", "Streamlit", "EDA", "Statistical Analysis"],
            "impact": "60% reduction in data exploration time",
            "link": "https://pandas-for-eda.streamlit.app/"
        },
        {
            "title": "📊 Matplotlib Plotting Demo",
            "description": "Interactive demonstration of Matplotlib plotting capabilities with fundamental chart types and customization.",
            "tags": ["Python", "Matplotlib", "Streamlit", "Data Visualization"],
            "impact": "Simplified visualization workflow for teams",
            "link": "https://matplotlibplotting-nn2eyrufj7jyyxrtjiziqt.streamlit.app/"
        }
    ]
    
    for project in projects:
        st.markdown(f"""
            <div class="project-card">
                <div class="project-title">{project['title']}</div>
                <div class="project-description">{project['description']}</div>
                <div style="margin-bottom: 1rem;">
                    {''.join([f'<span class="skill-badge">{tag}</span>' for tag in project['tags']])}
                </div>
                <div style="color: #48bb78; font-weight: 600; margin-bottom: 1rem;">
                    💡 Impact: {project['impact']}
                </div>
                <a href="{project['link']}" target="_blank" class="project-link">🔗 View Live Demo</a>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Skills Page
elif page == "🛠️ Skills":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>🛠️ Technical Skills</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🤖 Machine Learning & AI")
        skills_ml = {
            "Python": 95,
            "Machine Learning": 90,
            "Deep Learning": 88,
            "TensorFlow / PyTorch": 85,
            "Scikit-learn": 92,
            "XGBoost": 88
        }
        for skill, level in skills_ml.items():
            st.progress(level / 100, text=f"{skill}: {level}%")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### ☁️ Cloud Platforms")
        skills_cloud = {
            "Azure ML": 85,
            "AWS": 80,
            "Databricks": 82,
            "Synapse Analytics": 78,
            "Data Factory": 80
        }
        for skill, level in skills_cloud.items():
            st.progress(level / 100, text=f"{skill}: {level}%")
    
    with col2:
        st.markdown("### 📊 Data Analytics")
        skills_analytics = {
            "SQL": 88,
            "Power BI": 82,
            "Tableau": 85,
            "Pandas / NumPy": 90,
            "Statistics": 92
        }
        for skill, level in skills_analytics.items():
            st.progress(level / 100, text=f"{skill}: {level}%")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🧬 Bioinformatics")
        skills_bio = {
            "Drug Discovery": 85,
            "Molecular Modeling": 80,
            "Genomics": 82,
            "Bioinformatics Tools": 85,
            "Clinical Data Analysis": 80
        }
        for skill, level in skills_bio.items():
            st.progress(level / 100, text=f"{skill}: {level}%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 🔧 Technical Proficiencies")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            **Machine Learning Libraries**
            <div>
            """ + "".join([f'<span class="skill-badge">{s}</span>' for s in 
                          ["Scikit-learn", "TensorFlow", "PyTorch", "XGBoost", "Keras", "LightGBM"]]) + """
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            **Cloud & Data Platforms**
            <div>
            """ + "".join([f'<span class="skill-badge">{s}</span>' for s in 
                          ["Azure ML", "AWS", "Databricks", "Synapse", "Power BI", "Looker"]]) + """
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            **Specialized Skills**
            <div>
            """ + "".join([f'<span class="skill-badge">{s}</span>' for s in 
                          ["Fraud Detection", "Computer Vision", "NLP", "Bioinformatics", "Healthcare AI", "Drug Discovery"]]) + """
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Contact Page
elif page == "📞 Contact":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>📞 Get In Touch</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <div class="contact-info">
                <h3 style="margin-bottom: 1.5rem;">📬 Contact Information</h3>
                <div class="contact-item">
                    📧 <strong>Email:</strong><br>
                    <a href="mailto:faraimupfuti@gmail.com">faraimupfuti@gmail.com</a>
                </div>
                <div class="contact-item">
                    💼 <strong>LinkedIn:</strong><br>
                    <a href="https://linkedin.com/in/faraimupfuti" target="_blank">linkedin.com/in/faraimupfuti</a>
                </div>
                <div class="contact-item">
                    💻 <strong>GitHub:</strong><br>
                    <a href="https://github.com/faraimupfuti" target="_blank">github.com/faraimupfuti</a>
                </div>
                <div class="contact-item">
                    🌍 <strong>Location:</strong><br>
                    Harare, Zimbabwe
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
            <div style="background: linear-gradient(135deg, #48bb78 0%, #38a169 100%); 
                        color: white; padding: 1.5rem; border-radius: 12px;">
                <h3>💼 Open to Opportunities</h3>
                <p style="margin-bottom: 0;">
                    I'm available for exciting projects in:
                </p>
                <ul>
                    <li>🔍 Fraud Detection & Financial AI</li>
                    <li>🧬 Bioinformatics & Drug Discovery</li>
                    <li>🏥 Healthcare AI & Medical Imaging</li>
                    <li>📊 Data Science Consulting</li>
                    <li>☁️ Cloud ML Solutions</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📝 Send Me a Message")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=200)
            
            submit = st.form_submit_button("📨 Send Message")
            
            if submit:
                if name and email and message:
                    st.success("✅ Thank you for your message! I'll get back to you within 24 hours.")
                    # In production, integrate with email service
                else:
                    st.error("❌ Please fill in all required fields.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("💡 **Quick Response Time**: I typically respond to all inquiries within 24 hours.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 15px; color: white;">
        <p style="margin: 0; font-size: 1.1rem; font-weight: 500;">
            © 2025 Farai Mupfuti | Data Scientist | ML Engineer | Bioinformatics Specialist
        </p>
        <p style="margin-top: 0.5rem; opacity: 0.9;">
            🎯 Building AI Solutions for Healthcare, Finance & Beyond
        </p>
    </div>
""", unsafe_allow_html=True)
