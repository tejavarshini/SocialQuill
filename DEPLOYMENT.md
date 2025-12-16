# SocialQuill Deployment Guide for Render

## Prerequisites
- A Render account (sign up at https://render.com)
- A MongoDB Atlas account for the database (https://www.mongodb.com/cloud/atlas)
- Your GitHub repository should be public or connected to Render

## Deployment Steps

### Option 1: Using render.yaml (Blueprint - Recommended)

1. **Push your code to GitHub** (already done)

2. **Create a New Blueprint on Render**
   - Go to https://dashboard.render.com/
   - Click "New" → "Blueprint"
   - Connect your GitHub repository: `tejavarshini/SocialQuill`
   - Render will detect the `render.yaml` file automatically

3. **Configure Environment Variables**
   
   After creating the blueprint, set these required variables in the Render dashboard:

   **For socialquill-backend:**
   - `MONGODB_URI`: Your MongoDB Atlas connection string (e.g., `mongodb+srv://username:password@cluster.mongodb.net/socialquill`)
   - `EMAIL`: Your email for sending notifications
   - `PASSWORD`: Your email password or app-specific password
   - `EMAIL_SERVICE`: Email service (e.g., `Gmail`, `Zoho`)
   - `PERSPECTIVE_API_KEY`: (Optional) Google Perspective API key
   - `TEXTRAZOR_API_KEY`: (Optional) TextRazor API key
   - `INTERFACE_API_KEY`: (Optional) HuggingFace API key

   Note: `SECRET`, `REFRESH_SECRET`, and `CRYPTO_KEY` will be auto-generated

4. **Deploy**
   - Click "Apply" to deploy all services
   - Wait for all three services to deploy (this may take 10-15 minutes, especially for the classifier which downloads ML models)

### Option 2: Manual Deployment (Alternative)

If you prefer to deploy each service separately:

#### 1. Deploy Flask Classifier Server
- New → Web Service
- Connect repository: `tejavarshini/SocialQuill`
- Name: `socialquill-classifier`
- Runtime: `Python 3`
- Build Command: `cd classifier_server && pip install -r requirements.txt`
- Start Command: `cd classifier_server && python classifier_api.py`
- Free tier is sufficient

#### 2. Deploy Backend Server
- New → Web Service
- Connect repository: `tejavarshini/SocialQuill`
- Name: `socialquill-backend`
- Runtime: `Node`
- Build Command: `cd server && npm install`
- Start Command: `cd server && npm start`
- Add environment variables (see above)
- Set `CLASSIFIER_API_URL` to: `https://socialquill-classifier.onrender.com/classify`
- Set `CLIENT_URL` to: `https://socialquill-frontend.onrender.com`

#### 3. Deploy Frontend
- New → Static Site
- Connect repository: `tejavarshini/SocialQuill`
- Name: `socialquill-frontend`
- Build Command: `cd client && npm install && npm run build`
- Publish Directory: `client/build`
- Add environment variable:
  - `REACT_APP_API_URL`: `https://socialquill-backend.onrender.com`

## MongoDB Atlas Setup

1. Create a free cluster at https://cloud.mongodb.com/
2. Create a database user
3. Whitelist all IP addresses (0.0.0.0/0) for Render access
4. Get your connection string and add it to `MONGODB_URI`

## Post-Deployment

1. **Access your app**: Your frontend will be at `https://socialquill-frontend.onrender.com`
2. **First load may be slow**: Free tier services sleep after inactivity
3. **Test the classifier**: The first request will take longer as the ML model loads

## Important Notes

- **Free Tier Limitations**: Services sleep after 15 minutes of inactivity
- **Cold Starts**: First request after sleep takes 30-60 seconds
- **Classifier Memory**: The Flask classifier needs at least 512MB RAM
- **Build Time**: Initial deployment takes 10-15 minutes due to ML model download

## Updating Your Deployment

After making changes:
```bash
git add .
git commit -m "Your update message"
git push
```

Render will automatically redeploy when you push to the main branch.

## Troubleshooting

1. **Services not connecting**: Check that environment variables are set correctly
2. **Classifier fails**: Upgrade to paid tier (ML models need more memory)
3. **CORS errors**: Ensure `CLIENT_URL` matches your frontend URL exactly
4. **Database connection fails**: Check MongoDB Atlas IP whitelist and connection string

## URLs After Deployment

- **Frontend**: `https://socialquill-frontend.onrender.com`
- **Backend API**: `https://socialquill-backend.onrender.com`
- **Classifier API**: `https://socialquill-classifier.onrender.com`
