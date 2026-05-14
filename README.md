# 🎯 Farai Mupfuti - Interactive Resume

An elegant, modern Streamlit web application showcasing my professional portfolio as a Data Scientist, ML Engineer, and Bioinformatics Specialist.

## 🌟 Features

- **Interactive Navigation**: Easy-to-use sidebar navigation across different sections
- **Modern UI/UX**: Clean, professional design with gradient themes and smooth animations
- **Comprehensive Content**:
  - Professional summary and key achievements
  - Detailed work experience including current role at Citadel Analytics
  - Education credentials (MSc Bioinformatics from University of Tübingen)
  - 20+ project showcases with live demo links
  - Technical skills with proficiency levels
  - Contact information and messaging
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Performance Optimized**: Fast loading and smooth transitions

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/resume-streamlit-app.git
cd resume-streamlit-app
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser**
The app will automatically open at `http://localhost:8501`

## 📦 Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **plotly**: Interactive visualizations
- **Pillow**: Image processing

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/resume-streamlit-app.git
git push -u origin main
```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and branch
   - Set main file path: `app.py`
   - Click "Deploy"

### Deploy to Other Platforms

**Heroku**
```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

**Railway**
- Connect your GitHub repository
- Railway will auto-detect Streamlit
- Deploy automatically

**Google Cloud Run**
```bash
# Create Dockerfile
gcloud run deploy --source . --platform managed
```

## 📁 Project Structure

```
resume-streamlit-app/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore           # Git ignore rules
└── .streamlit/          # Streamlit configuration (optional)
    └── config.toml      # Theme and settings
```

## 🎨 Customization

### Modify Colors
Edit the CSS section in `app.py` (lines 18-200) to change:
- Primary gradient colors
- Card backgrounds
- Text colors
- Button styles

### Add/Remove Sections
- Modify sidebar navigation in `app.py` (line 203)
- Add new page conditions following existing pattern
- Update section cards as needed

### Update Content
- **Experience**: Lines 450-550
- **Education**: Lines 560-650
- **Projects**: Lines 660-900
- **Skills**: Lines 910-1000

## 🔧 Configuration

Create `.streamlit/config.toml` for custom settings:

```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f5f7fa"
textColor = "#2d3748"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
```

## 📊 Features Breakdown

### Home Page
- Professional statistics display
- Key achievements showcase
- Professional summary

### About Page
- Detailed professional background
- Areas of expertise
- Career highlights

### Experience Page
- Current role: Data Scientist at Citadel Analytics (May 2025 - Present)
- Previous positions with detailed responsibilities
- Skills used in each role

### Education Page
- MSc Bioinformatics - University of Tübingen (2025)
- BSc Information Systems - Catholic University of Zimbabwe
- Professional certifications (Azure, AWS)

### Projects Page
- 20+ live project demonstrations
- Detailed descriptions and impact metrics
- Direct links to live demos

### Skills Page
- Interactive skill proficiency bars
- Categorized by domain (ML, Cloud, Analytics, Bioinformatics)
- Technology stack overview

### Contact Page
- Contact information
- Messaging form
- Social media links

## 🔒 Security Notes

- No sensitive data stored in code
- Contact form requires backend integration for production
- Environment variables for API keys (if needed)

## 🐛 Troubleshooting

**Port already in use**
```bash
streamlit run app.py --server.port 8502
```

**Module not found**
```bash
pip install -r requirements.txt --upgrade
```

**Styling not loading**
- Clear browser cache
- Check CSS in `st.markdown()` sections
- Ensure unsafe_allow_html=True

## 📝 TODO / Future Enhancements

- [ ] Add dark mode toggle
- [ ] Integrate contact form with email service (SendGrid/EmailJS)
- [ ] Add downloadable PDF resume
- [ ] Include visitor analytics
- [ ] Add blog section
- [ ] Implement project filtering
- [ ] Add testimonials section
- [ ] Create multilingual support

## 🤝 Contributing

Feel free to fork this project and customize it for your own resume. If you find bugs or have suggestions:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Contact

**Farai Mupfuti**
- Email: faraimupfuti@gmail.com
- LinkedIn: [linkedin.com/in/faraimupfuti](https://linkedin.com/in/faraimupfuti)
- GitHub: [github.com/faraimupfuti](https://github.com/faraimupfuti)
- Portfolio: [farai-datascientist.vercel.app](https://farai-datascientist.vercel.app/)

## 🌟 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Design inspired by modern portfolio trends
- Icons from emoji set
- Fonts from Google Fonts

---

**Built with ❤️ by Farai Mupfuti | © 2025**
