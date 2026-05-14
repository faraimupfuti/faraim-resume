# 🚀 Deployment Guide

This guide covers deploying your Streamlit Resume App to various platforms.

## Table of Contents
1. [Streamlit Cloud (Recommended)](#streamlit-cloud)
2. [Heroku](#heroku)
3. [Railway](#railway)
4. [Google Cloud Run](#google-cloud-run)
5. [AWS EC2](#aws-ec2)
6. [Vercel](#vercel)

---

## Streamlit Cloud (Recommended)

**Pros**: Free, Easy, Streamlit-native, Auto-deploys from GitHub
**Best for**: Quick deployment, Portfolio projects

### Steps:

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/resume-streamlit-app.git
git push -u origin main
```

2. **Deploy**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `YOUR_USERNAME/resume-streamlit-app`
   - Branch: `main`
   - Main file path: `app.py`
   - Click "Deploy"

3. **Access Your App**
   - URL will be: `https://YOUR_USERNAME-resume-streamlit-app-xxxxx.streamlit.app`

### Configuration:
No additional configuration needed! The app will use:
- `requirements.txt` for dependencies
- `.streamlit/config.toml` for theme

---

## Heroku

**Pros**: Free tier, Custom domain support, Easy scaling
**Best for**: Production apps, Custom domains

### Steps:

1. **Install Heroku CLI**
```bash
# macOS
brew tap heroku/brew && brew install heroku

# Windows (download installer)
# https://devcenter.heroku.com/articles/heroku-cli
```

2. **Login to Heroku**
```bash
heroku login
```

3. **Create Heroku App**
```bash
heroku create your-resume-app-name
```

4. **Verify Files**
Ensure these files exist:
- `Procfile` ✅ (already created)
- `requirements.txt` ✅ (already created)
- `runtime.txt` ✅ (already created)

5. **Deploy**
```bash
git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main
```

6. **Open Your App**
```bash
heroku open
```

### Troubleshooting:
```bash
# View logs
heroku logs --tail

# Restart app
heroku restart
```

---

## Railway

**Pros**: Modern UI, GitHub integration, Free tier
**Best for**: Quick deployments, Modern workflow

### Steps:

1. **Visit Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up/Login with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `resume-streamlit-app` repository

3. **Configure**
   - Railway auto-detects Streamlit
   - No additional configuration needed
   - Uses `requirements.txt` automatically

4. **Deploy**
   - Click "Deploy"
   - Railway will build and deploy automatically

5. **Access**
   - Get your deployment URL from Railway dashboard
   - Example: `https://resume-streamlit-app-production.up.railway.app`

---

## Google Cloud Run

**Pros**: Scalable, Pay-per-use, Integrates with GCP
**Best for**: Enterprise deployments, Scalable apps

### Steps:

1. **Install Google Cloud SDK**
```bash
# macOS
brew install --cask google-cloud-sdk

# Or download from: https://cloud.google.com/sdk/docs/install
```

2. **Initialize and Login**
```bash
gcloud init
gcloud auth login
```

3. **Create Dockerfile**
Create `Dockerfile` in your project:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD streamlit run app.py --server.port=8080 --server.address=0.0.0.0
```

4. **Deploy**
```bash
gcloud run deploy resume-app \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

5. **Access**
   - URL will be provided after deployment
   - Example: `https://resume-app-xxxxx-uc.a.run.app`

---

## AWS EC2

**Pros**: Full control, AWS ecosystem, Custom configuration
**Best for**: Production apps needing full control

### Steps:

1. **Launch EC2 Instance**
   - Go to AWS Console → EC2
   - Launch Ubuntu 22.04 instance (t2.micro for free tier)
   - Configure security group: Allow port 8501

2. **Connect to Instance**
```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

3. **Setup Environment**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip python3-venv -y

# Clone your repository
git clone https://github.com/YOUR_USERNAME/resume-streamlit-app.git
cd resume-streamlit-app

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

4. **Run with Screen (keeps running after disconnect)**
```bash
screen -S streamlit
streamlit run app.py --server.port=8501 --server.address=0.0.0.0

# Detach with: Ctrl+A then D
# Reattach with: screen -r streamlit
```

5. **Access**
   - Visit: `http://your-ec2-public-ip:8501`

### Production Setup (Optional):
Use **systemd** for auto-restart:

```bash
# Create service file
sudo nano /etc/systemd/system/streamlit.service
```

Add:
```ini
[Unit]
Description=Streamlit Resume App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/resume-streamlit-app
ExecStart=/home/ubuntu/resume-streamlit-app/venv/bin/streamlit run app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable streamlit
sudo systemctl start streamlit
sudo systemctl status streamlit
```

---

## Vercel

**Pros**: Fast CDN, Easy deployment, GitHub integration
**Note**: Vercel doesn't natively support Streamlit, but you can use custom Docker

### Steps:

1. **Install Vercel CLI**
```bash
npm install -g vercel
```

2. **Create vercel.json**
```json
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

**Note**: For true Streamlit on Vercel, consider containerization or use Streamlit Cloud instead.

---

## Comparison Table

| Platform | Free Tier | Ease of Use | Best For | Custom Domain |
|----------|-----------|-------------|----------|---------------|
| **Streamlit Cloud** | ✅ Yes | ⭐⭐⭐⭐⭐ | Portfolio, Quick deploy | ❌ No |
| **Heroku** | ✅ Yes* | ⭐⭐⭐⭐ | Production apps | ✅ Yes |
| **Railway** | ✅ Yes | ⭐⭐⭐⭐⭐ | Modern workflow | ✅ Yes |
| **Google Cloud Run** | ✅ Yes* | ⭐⭐⭐ | Enterprise, Scale | ✅ Yes |
| **AWS EC2** | ✅ Yes* | ⭐⭐ | Full control | ✅ Yes |
| **Vercel** | ✅ Yes | ⭐⭐ | Static sites (not ideal) | ✅ Yes |

*Free tier with limitations

---

## Recommended Approach

**For Portfolio/Personal Use:**
→ **Streamlit Cloud** (Easiest, Free, Perfect for portfolios)

**For Production/Business:**
→ **Railway** or **Heroku** (Good balance of ease and features)

**For Enterprise:**
→ **Google Cloud Run** or **AWS EC2** (Scalable, Full control)

---

## Post-Deployment Checklist

- [ ] Test all pages and navigation
- [ ] Verify all project links work
- [ ] Check responsive design on mobile
- [ ] Test contact form (if integrated)
- [ ] Set up custom domain (if needed)
- [ ] Configure analytics (optional)
- [ ] Add SSL certificate (most platforms auto-provide)
- [ ] Share your deployed URL!

---

## Environment Variables (If Needed)

If you add features requiring API keys:

**Streamlit Cloud:**
- Add in app settings → Secrets

**Heroku:**
```bash
heroku config:set API_KEY=your_key_here
```

**Railway:**
- Add in project settings → Variables

**Google Cloud Run:**
```bash
gcloud run services update resume-app \
  --set-env-vars=API_KEY=your_key_here
```

---

## Need Help?

- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **Community**: [discuss.streamlit.io](https://discuss.streamlit.io)
- **Issues**: Open an issue on GitHub

---

**Built with ❤️ by Farai Mupfuti**
