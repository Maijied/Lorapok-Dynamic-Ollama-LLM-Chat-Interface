# Lorapok Dynamic Ollama LLM Chat Interface - Website

Professional GitHub Pages website for the Lorapok Dynamic Ollama LLM Chat Interface project.

## Features

- 🎨 Modern dark theme design
- 📱 Fully responsive layout
- ⚡ Interactive terminal demo
- 🚀 Smooth animations and transitions
- 📋 Copy-to-clipboard functionality
- 🔗 Smooth scrolling navigation
- 📊 Performance monitoring display
- 🌐 Cross-browser compatibility

## Local Development

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Navigate to the website directory:
   ```bash
   cd docs/website
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

4. Open your browser and visit `http://localhost:3000`

### Development Commands

- `npm start` - Start development server on port 3000
- `npm run dev` - Start development server on localhost only
- `npm run build` - No build required (static site)
- `npm run validate` - Validate HTML anchor links and metadata

## Project Structure

```
docs/website/
├── index.html          # Main website file
├── styles.css          # Professional styling
├── script.js           # Interactive features
├── package.json        # Dependencies and scripts
└── README.md          # This file
```

## Features Overview

### Navigation
- Fixed header with smooth scroll navigation
- Active section highlighting
- Mobile-responsive hamburger menu

### Hero Section
- Gradient text effects
- Interactive terminal demo
- Call-to-action buttons

### Features Section
- Grid layout of key features
- Hover animations
- Icon-based design

### Demo Section
- Live terminal simulation
- Typing animation effects
- Feature highlights

### Requirements Section
- System requirements display
- Version information
- Installation prerequisites

### Commands Section
- Available command reference
- Categorized command groups
- Code syntax highlighting

### Download Section
- Multiple installation methods
- Copy-to-clipboard functionality
- Platform-specific instructions

### API Section
- Code examples
- Feature documentation
- Integration guides

## Customization

### Colors
The website uses CSS custom properties (variables) for easy theming:

```css
:root {
    --primary-color: #6366f1;
    --secondary-color: #8b5cf6;
    --accent-color: #06b6d4;
    --dark-bg: #0a0a0a;
    --text-primary: #ffffff;
    /* ... more variables */
}
```

### Content
Edit the `index.html` file to update:
- Project description
- Feature lists
- Requirements
- Commands
- Download links

### Styling
Modify `styles.css` to:
- Change color scheme
- Adjust layout and spacing
- Add new animations
- Customize responsive breakpoints

### Interactivity
Update `script.js` to:
- Add new animations
- Modify terminal demo
- Enhance user interactions
- Add new features

## Deployment

The website is automatically deployed to GitHub Pages using GitHub Actions when changes are pushed to the main branch.

### Manual Deployment

1. Enable GitHub Pages in repository settings
2. Set source to "Deploy from a branch"
3. Select "gh-pages" branch
4. The CI/CD workflow will handle the rest

## Browser Support

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## Performance

- Optimized CSS and JavaScript
- Minimal dependencies
- Fast loading times
- Efficient animations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## License

This website is part of the Lorapok Dynamic Ollama LLM Chat Interface project, licensed under MIT.

## Support

For questions or issues with the website:
- Open an issue on GitHub
- Check the main project documentation
- Review the CI/CD workflow logs