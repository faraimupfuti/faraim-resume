# 📁 Assets Folder

This folder contains static assets used by the resume application.

## 📂 Folder Structure

```
assets/
├── images/         # Images and photos
├── fonts/          # Custom fonts (if needed)
└── data/           # Data files (JSON, CSV, etc.)
```

## 🖼️ Images

### Profile Photo
Place your profile photo here and update the path in `app.py`:

**Recommended specifications:**
- Format: JPG or PNG
- Size: 400x400px to 800x800px
- File size: < 500KB
- Aspect ratio: 1:1 (square)

**Example filename:** `profile.jpg`

**Update in app.py (line ~207):**
```python
# Change from:
st.image("https://via.placeholder.com/150", caption="Farai Mupfuti")

# To:
st.image("assets/images/profile.jpg", caption="Your Name", width=150)
```

### Project Screenshots
Add screenshots of your projects:
- `project1.png`
- `project2.png`
- etc.

### Icons & Logos
If you need custom icons or company logos:
- `company-logo.png`
- `certification-badge.png`

## 🎨 Fonts

If you want to use custom fonts instead of Google Fonts:

1. Place font files here (.ttf, .woff, .woff2)
2. Update CSS in `app.py` to load them

**Example:**
```css
@font-face {
    font-family: 'CustomFont';
    src: url('assets/fonts/custom-font.woff2') format('woff2');
}
```

## 📊 Data Files

Store any data files your app might need:
- `skills.json` - Skills data
- `projects.json` - Projects metadata
- `experience.csv` - Work experience data

**Example: skills.json**
```json
{
  "machine_learning": {
    "name": "Machine Learning",
    "level": 90,
    "category": "AI"
  }
}
```

## 🔧 Usage in Streamlit

### Loading Images
```python
from PIL import Image

# Load local image
image = Image.open("assets/images/profile.jpg")
st.image(image, caption="My Photo", width=200)
```

### Loading Data
```python
import json
import pandas as pd

# Load JSON
with open("assets/data/projects.json") as f:
    projects = json.load(f)

# Load CSV
df = pd.read_csv("assets/data/experience.csv")
```

## 📝 Best Practices

### Image Optimization
- Compress images before adding (use [TinyPNG](https://tinypng.com/))
- Use WebP format for better compression
- Keep total assets folder < 10MB

### File Naming
- Use lowercase
- Use hyphens instead of spaces: `my-project.jpg`
- Be descriptive: `profile-photo-2025.jpg`

### Organization
- Group related images in subfolders if needed
- Keep file names consistent
- Document any custom assets in this README

## 🚀 Deployment Notes

### Streamlit Cloud
- Assets folder is automatically included
- Keep total app size under 1GB

### Docker
- Assets are copied into container
- Consider using CDN for large files

### Git
- Large files (>5MB) should use Git LFS
- Or host on external CDN and link

## 📦 External Assets (CDN)

For better performance, consider hosting large assets externally:

**Cloudinary:**
```python
st.image("https://res.cloudinary.com/YOUR_CLOUD/image/upload/v1234567890/profile.jpg")
```

**ImgBB:**
```python
st.image("https://i.ibb.co/xxxxxxxxx/profile.jpg")
```

**GitHub:**
```python
st.image("https://raw.githubusercontent.com/username/repo/main/assets/profile.jpg")
```

## 🔍 Current Assets

None yet! Add your assets here.

**To add assets:**
1. Place files in appropriate subfolder
2. Update file paths in `app.py`
3. Test locally before deploying
4. Commit and push to GitHub

---

**Need help?** Check the [Streamlit documentation](https://docs.streamlit.io/) for more on working with assets.
