# ⚡ Quick Start Guide

Get your resume app running in **5 minutes**!

## 🎯 Prerequisites

- Python 3.8 or higher
- Git (optional, for version control)
- A GitHub account (for cloud deployment)

---

## 🚀 Option 1: Run Locally (Fastest)

### Step 1: Download & Extract
Download the project folder and navigate to it:
```bash
cd resume-streamlit-app
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run!
```bash
streamlit run app.py
```

**That's it!** Your browser will open at `http://localhost:8501`

---

## ☁️ Option 2: Deploy to Cloud (Free)

### Step 1: Push to GitHub

```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "My resume app"

# Create repository on GitHub (github.com/new)
# Then push
git remote add origin https://github.com/YOUR_USERNAME/resume-streamlit-app.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to **[share.streamlit.io](https://share.streamlit.io)**
2. Click **"New app"**
3. Select your GitHub repository
4. Click **"Deploy"**
5. Wait 2-3 minutes

**Done!** Your resume is live at: `https://YOUR_USERNAME-resume-streamlit-app.streamlit.app`

---

## 🎨 Customization Quick Tips

### Change Colors
Edit `app.py` lines 18-200 (CSS section):
```python
# Find these lines and change hex colors:
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# Change #667eea (purple) and #764ba2 (darker purple) to your colors
```

### Add Your Photo
Replace the placeholder in `app.py` line 207:
```python
st.image("https://via.placeholder.com/150", caption="Farai Mupfuti")
# Change to:
st.image("path/to/your/photo.jpg", caption="Your Name")
```

### Update Contact Info
Edit `app.py` around lines 950-980 (Contact page section)

---

## 📝 What to Update for Your Resume

1. **Personal Info** (lines 200-210)
   - Name, title, certifications

2. **Experience** (lines 450-550)
   - Add/remove jobs
   - Update dates and responsibilities

3. **Education** (lines 560-650)
   - Degrees and certifications

4. **Projects** (lines 660-900)
   - Add your projects with links
   - Update descriptions and impact metrics

5. **Skills** (lines 910-1000)
   - Adjust skill levels (0-100%)
   - Add/remove technologies

6. **Contact** (lines 950-1000)
   - Email, LinkedIn, GitHub links

---

## 🐛 Troubleshooting

### "Command not found: streamlit"
```bash
pip install streamlit
```

### "Port already in use"
```bash
streamlit run app.py --server.port 8502
```

### "Module not found"
```bash
pip install -r requirements.txt --upgrade
```

### Styling not showing
- Clear browser cache (Ctrl + Shift + R)
- Check CSS is uncommented in `app.py`

---

## 📱 Test on Mobile

After running locally:
1. Find your computer's IP address
   - Windows: `ipconfig`
   - Mac/Linux: `ifconfig`
2. On mobile browser: `http://YOUR_IP:8501`

---

## 🎯 Next Steps

- [ ] Customize colors to match your brand
- [ ] Add your actual photo
- [ ] Update all personal information
- [ ] Add your projects with live links
- [ ] Deploy to Streamlit Cloud
- [ ] Share your live URL on LinkedIn!

---

## 💡 Pro Tips

1. **Use Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

2. **Auto-reload Changes**
   - Streamlit auto-reloads when you save `app.py`
   - Keep the app running while editing

3. **Check Mobile View**
   - Click hamburger menu → Settings → "Wide mode"
   - Test on actual mobile device

4. **Backup Your Work**
   - Commit changes regularly
   - Push to GitHub frequently

---

## 🆘 Need Help?

- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **Community Forum**: [discuss.streamlit.io](https://discuss.streamlit.io)
- **GitHub Issues**: Create an issue in your repository

---

## 🎉 You're Ready!

Your resume app is now running. Share it with the world! 🚀

**Live URL Format**: `https://YOUR_USERNAME-resume-streamlit-app.streamlit.app`

---

**Built by Farai Mupfuti** | [LinkedIn](https://linkedin.com/in/faraimupfuti) | [GitHub](https://github.com/faraimupfuti)
