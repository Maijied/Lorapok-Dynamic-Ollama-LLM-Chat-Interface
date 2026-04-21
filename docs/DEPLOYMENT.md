# GitHub Pages Deployment Guide

This guide will help you deploy the professional website for the Lorapok Dynamic Ollama LLM Chat Interface to GitHub Pages.

## Prerequisites

- GitHub repository created and configured
- All website files committed and pushed to the main branch
- GitHub Pages enabled in repository settings

## Step-by-Step Deployment

### 1. Enable GitHub Pages

1. Go to your GitHub repository
2. Click on **Settings** tab
3. Scroll down to **Pages** section in the left sidebar
4. Under **Source**, select **"Deploy from a branch"**
5. Select **main** branch and **"/docs"** folder
6. Click **Save**

### 2. Configure Repository Settings

The repository should have the following structure:
```
your-repo/
├── docs/
│   ├── .nojekyll          # Prevents Jekyll processing
│   └── website/           # Your website files
│       ├── index.html
│       ├── styles.css
│       ├── script.js
│       └── package.json
├── .github/
│   └── workflows/
│       └── deploy.yml     # CI/CD workflow
└── [other project files]
```

### 3. Automated Deployment

Once the GitHub Actions workflow is active, it will automatically:
- Validate HTML, CSS, and JavaScript
- Deploy the website to GitHub Pages
- Publish the site from the `docs/website` artifact
- Make it available at: `https://maijied.github.io/Lorapok-Dynamic-Ollama-LLM-Chat-Interface`

### 4. Custom Domain (Optional)

To use a custom domain:

1. Go to repository **Settings** > **Pages**
2. Under **Custom domain**, enter your domain
3. Configure DNS records as instructed
4. Add SSL certificate if needed

## Troubleshooting

### Website Not Loading

1. **Check repository structure**: Ensure files are in `docs/website/`
2. **Verify GitHub Pages settings**: Confirm source is set to `/docs` folder
3. **Check build status**: Look at Actions tab for workflow status
4. **Wait for deployment**: It may take a few minutes for changes to appear

### 404 Errors

1. **Missing .nojekyll file**: Ensure `.nojekyll` exists in `docs/` folder
2. **Incorrect paths**: Verify all asset paths in HTML are correct
3. **Case sensitivity**: Check file and folder name casing

### Build Failures

1. **Check workflow logs**: Go to Actions tab and click on failed workflow
2. **Validate files**: Ensure HTML, CSS, and JS are syntactically correct
3. **Dependencies**: Check if all required files are committed

## Local Testing

Before deploying, test locally:

```bash
cd docs/website
npm install
npm start
```

Visit `http://localhost:3000` to preview the site.

## Performance Optimization

The website is optimized for:
- Fast loading times
- Mobile responsiveness
- SEO best practices
- Accessibility standards

## Security Considerations

- All external links use `rel="noopener noreferrer"`
- No sensitive data exposed
- HTTPS enforced by GitHub Pages
- Content Security Policy headers applied

## Analytics (Optional)

To add analytics:

1. Sign up for Google Analytics or similar service
2. Add tracking code to `index.html`
3. Update the CI/CD workflow if needed

## Support

If you encounter issues:
1. Check GitHub Actions logs
2. Verify file structure matches this guide
3. Test locally first
4. Open an issue in the repository

## URL Structure

Once deployed, your website will be available at:
- `https://maijied.github.io/Lorapok-Dynamic-Ollama-LLM-Chat-Interface/`

All internal links are configured for this URL structure.