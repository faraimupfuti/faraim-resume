# 🐳 Docker Deployment Guide

This guide covers deploying your Streamlit Resume App using Docker and Docker Compose.

## 📋 Prerequisites

- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Docker Compose installed (included with Docker Desktop)
- Basic command line knowledge

## 🚀 Quick Start with Docker

### Option 1: Using Docker Compose (Recommended)

**Start the application:**
```bash
docker-compose up -d
```

**View logs:**
```bash
docker-compose logs -f
```

**Stop the application:**
```bash
docker-compose down
```

**Access the app:**
Open browser at `http://localhost:8501`

### Option 2: Using Docker CLI

**Build the image:**
```bash
docker build -t resume-streamlit-app .
```

**Run the container:**
```bash
docker run -d \
  -p 8501:8501 \
  --name resume-app \
  --restart unless-stopped \
  resume-streamlit-app
```

**View logs:**
```bash
docker logs -f resume-app
```

**Stop the container:**
```bash
docker stop resume-app
docker rm resume-app
```

## 🔧 Development Mode

For development with hot-reloading:

```bash
docker-compose up
```

Changes to `app.py` will automatically reload in the browser.

## 📦 Production Deployment

### Build Production Image

```bash
docker build -t resume-app:production .
```

### Run Production Container

```bash
docker run -d \
  -p 80:8501 \
  --name resume-app-prod \
  --restart always \
  --memory="512m" \
  --cpus="1.0" \
  resume-app:production
```

## ☁️ Deploy to Cloud Platforms

### Google Cloud Run

```bash
# Build and tag
docker build -t gcr.io/YOUR_PROJECT_ID/resume-app .

# Push to Container Registry
docker push gcr.io/YOUR_PROJECT_ID/resume-app

# Deploy
gcloud run deploy resume-app \
  --image gcr.io/YOUR_PROJECT_ID/resume-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### AWS ECS (Elastic Container Service)

```bash
# Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

# Build and tag
docker build -t resume-app .
docker tag resume-app:latest YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/resume-app:latest

# Push to ECR
docker push YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/resume-app:latest

# Create ECS task definition and service (use AWS Console or CLI)
```

### Azure Container Instances

```bash
# Login to Azure
az login

# Create resource group
az group create --name resume-app-rg --location eastus

# Create container registry
az acr create --resource-group resume-app-rg --name resumeappregistry --sku Basic

# Build and push
az acr build --registry resumeappregistry --image resume-app:latest .

# Deploy
az container create \
  --resource-group resume-app-rg \
  --name resume-app \
  --image resumeappregistry.azurecr.io/resume-app:latest \
  --dns-name-label resume-app-unique \
  --ports 8501
```

### DigitalOcean App Platform

```bash
# Push to Docker Hub
docker build -t YOUR_USERNAME/resume-app .
docker push YOUR_USERNAME/resume-app

# Deploy via DigitalOcean Console:
# 1. Create App
# 2. Select Docker Hub
# 3. Enter: YOUR_USERNAME/resume-app
# 4. Configure port: 8501
# 5. Deploy
```

## 🔍 Docker Commands Cheat Sheet

### Container Management
```bash
# List running containers
docker ps

# List all containers
docker ps -a

# Start container
docker start resume-app

# Stop container
docker stop resume-app

# Restart container
docker restart resume-app

# Remove container
docker rm resume-app

# Remove container (force)
docker rm -f resume-app
```

### Image Management
```bash
# List images
docker images

# Remove image
docker rmi resume-streamlit-app

# Remove unused images
docker image prune

# Remove all unused images
docker image prune -a
```

### Logs & Debugging
```bash
# View logs
docker logs resume-app

# Follow logs (real-time)
docker logs -f resume-app

# Last 100 lines
docker logs --tail 100 resume-app

# Execute command in running container
docker exec -it resume-app bash

# Inspect container
docker inspect resume-app
```

### Docker Compose Commands
```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose stop

# Stop and remove
docker-compose down

# Rebuild images
docker-compose build

# View logs
docker-compose logs -f

# Restart services
docker-compose restart
```

## ⚙️ Environment Variables

Create `.env` file for environment variables:

```env
# .env
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

Use in docker-compose.yml:
```yaml
services:
  streamlit-app:
    env_file:
      - .env
```

## 🔒 Security Best Practices

### 1. Non-root User
Add to Dockerfile:
```dockerfile
RUN useradd -m -u 1000 streamlit
USER streamlit
```

### 2. Read-only Filesystem
```bash
docker run -d \
  --read-only \
  --tmpfs /tmp \
  -p 8501:8501 \
  resume-streamlit-app
```

### 3. Resource Limits
```bash
docker run -d \
  --memory="512m" \
  --cpus="1.0" \
  --pids-limit=100 \
  resume-streamlit-app
```

### 4. Health Checks
Already included in Dockerfile:
```dockerfile
HEALTHCHECK --interval=30s --timeout=10s \
  CMD curl -f http://localhost:8501/_stcore/health
```

## 📊 Monitoring

### View Container Stats
```bash
docker stats resume-app
```

### Container Resource Usage
```bash
docker container top resume-app
```

## 🐛 Troubleshooting

### Container won't start
```bash
# Check logs
docker logs resume-app

# Check if port is in use
lsof -i :8501  # macOS/Linux
netstat -ano | findstr :8501  # Windows
```

### App not accessible
```bash
# Verify container is running
docker ps

# Check container health
docker inspect resume-app | grep -A 5 Health

# Test from inside container
docker exec resume-app curl http://localhost:8501/_stcore/health
```

### Build failures
```bash
# Clear build cache
docker builder prune

# Build without cache
docker build --no-cache -t resume-streamlit-app .
```

### Performance issues
```bash
# Check resource usage
docker stats

# Increase memory limit
docker update --memory="1g" resume-app

# Increase CPU limit
docker update --cpus="2.0" resume-app
```

## 🔄 Updates & Maintenance

### Update Application
```bash
# Pull latest code
git pull

# Rebuild and restart
docker-compose down
docker-compose build
docker-compose up -d
```

### Backup Container Data
```bash
# Create backup
docker commit resume-app resume-app-backup

# Save to file
docker save resume-app-backup > resume-app-backup.tar

# Load from file
docker load < resume-app-backup.tar
```

## 📝 Multi-stage Build (Advanced)

For smaller production images, create multi-stage Dockerfile:

```dockerfile
# Build stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Production stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["streamlit", "run", "app.py"]
```

## 🌐 Reverse Proxy (Nginx)

To run behind Nginx:

**nginx.conf:**
```nginx
server {
    listen 80;
    server_name resume.yourdomain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

**docker-compose.yml with Nginx:**
```yaml
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - streamlit-app
```

## ✅ Verification Checklist

After deployment:
- [ ] Container is running: `docker ps`
- [ ] Health check passes: `docker inspect resume-app | grep Health`
- [ ] App is accessible at `http://localhost:8501`
- [ ] All pages load correctly
- [ ] Project links work
- [ ] Mobile view works
- [ ] No console errors

---

**Need help?** Open an issue on GitHub!

**Built with 🐳 and ❤️ by Farai Mupfuti**
