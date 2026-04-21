// Lorapok Dynamic Ollama LLM Chat Interface - Professional Interactive Features

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all features
    initLoadingScreen();
    initNavigation();
    initScrollAnimations();
    initHeroAnimations();
    initTerminalDemo();
    initGuideTabs();
    initDownloadTabs();
    initCopyToClipboard();
    initCounterAnimations();
    initSmoothScrolling();
    initMobileMenu();
    initParticleEffects();
});

// Loading Screen
function initLoadingScreen() {
    const loadingScreen = document.querySelector('.loading-screen');
    const loadingProgress = document.querySelector('.loading-progress');

    let progress = 0;
    const interval = setInterval(() => {
        progress += Math.random() * 15;
        if (progress >= 100) {
            progress = 100;
            clearInterval(interval);
            setTimeout(() => {
                loadingScreen.classList.add('hidden');
                document.body.style.overflow = 'auto';
            }, 500);
        }
        loadingProgress.style.width = progress + '%';
    }, 200);

    // Prevent scrolling during loading
    document.body.style.overflow = 'hidden';
}

// Navigation functionality
function initNavigation() {
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.nav-links a');

    // Navbar background on scroll
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Active link highlighting
    window.addEventListener('scroll', function() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPosition = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    });
}

// Hero animations and effects
function initHeroAnimations() {
    // Animate hero stats on scroll
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats();
            }
        });
    }, { threshold: 0.5 });

    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) {
        statsObserver.observe(heroStats);
    }
}

// Counter animations for stats
function initCounterAnimations() {
    // This will be called when hero stats come into view
}

function animateStats() {
    const statNumbers = document.querySelectorAll('.stat-number');

    statNumbers.forEach(stat => {
        const target = parseInt(stat.textContent.replace(/[^\d]/g, ''));
        let current = 0;
        const increment = target / 50;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            stat.textContent = Math.floor(current).toLocaleString();
        }, 50);
    });
}

// Scroll animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, observerOptions);

    // Observe all elements with data-scroll attribute
    document.querySelectorAll('[data-scroll]').forEach(element => {
        observer.observe(element);
    });

    // Also observe feature cards and other animated elements
    document.querySelectorAll('.feature-card, .guide-card, .req-item').forEach(card => {
        card.setAttribute('data-scroll', '');
        observer.observe(card);
    });
}

// Terminal demo animation
function initTerminalDemo() {
    const terminalLines = [
        { type: 'prompt', text: 'lorapok-chat> ' },
        { type: 'command', text: 'list-models' },
        { type: 'response', text: 'Available models:' },
        { type: 'response', text: '  • llama2:7b (7.2GB)' },
        { type: 'response', text: '  • codellama:7b (3.8GB)' },
        { type: 'response', text: '  • mistral:7b (4.1GB)' },
        { type: 'response', text: '  • llama2:13b (7.3GB)' },
        { type: 'prompt', text: 'lorapok-chat> ' },
        { type: 'command', text: 'switch llama2:7b' },
        { type: 'success', text: '✓ Switched to model: llama2:7b' },
        { type: 'prompt', text: 'lorapok-chat> ' },
        { type: 'command', text: 'chat' },
        { type: 'response', text: 'Starting interactive chat session...' },
        { type: 'response', text: 'Type your message or "help" for commands.' },
        { type: 'prompt', text: 'You> ' },
        { type: 'input', text: 'Hello, can you help me with Python?' },
        { type: 'ai', text: 'AI: Hello! I\'d be happy to help you with Python programming.' },
        { type: 'ai', text: 'AI: Python is a versatile, high-level programming language known for its' },
        { type: 'ai', text: 'AI: simplicity and readability. What specific aspect would you like to learn?' },
        { type: 'prompt', text: 'lorapok-chat> ' },
        { type: 'command', text: 'benchmark' },
        { type: 'response', text: 'Running performance benchmark...' },
        { type: 'response', text: 'Response time: 1.8s | Memory: 2.1GB | CPU: 67%' },
        { type: 'response', text: 'Tokens/sec: 45.2 | Quality score: 9.2/10' },
        { type: 'prompt', text: 'lorapok-chat> ' },
        { type: 'cursor', text: '' }
    ];

    const terminalContent = document.querySelector('.terminal-content');
    if (!terminalContent) return;

    let currentLine = 0;
    let currentChar = 0;
    let isTyping = false;

    function typeWriter() {
        if (isTyping) return;
        isTyping = true;

        const line = terminalLines[currentLine];
        if (!line) {
            isTyping = false;
            return;
        }

        const lineElement = document.createElement('div');
        lineElement.className = `terminal-line terminal-${line.type}`;

        if (line.type === 'cursor') {
            lineElement.innerHTML = '<span class="terminal-cursor">▊</span>';
            terminalContent.appendChild(lineElement);
            currentLine++;
            isTyping = false;
            return;
        }

        const promptSpan = document.createElement('span');
        promptSpan.className = 'terminal-prompt';
        const textSpan = document.createElement('span');
        textSpan.className = 'terminal-text';

        if (line.type === 'prompt') {
            promptSpan.textContent = line.text;
            lineElement.appendChild(promptSpan);
        } else {
            if (line.type === 'command') {
                promptSpan.textContent = '> ';
                textSpan.textContent = line.text;
                textSpan.classList.add('terminal-command');
            } else if (line.type === 'success') {
                textSpan.textContent = line.text;
                textSpan.classList.add('terminal-success');
            } else if (line.type === 'error') {
                textSpan.textContent = line.text;
                textSpan.classList.add('terminal-error');
            } else if (line.type === 'ai') {
                textSpan.textContent = line.text;
                textSpan.classList.add('terminal-ai');
            } else {
                textSpan.textContent = line.text;
            }
            lineElement.appendChild(promptSpan);
            lineElement.appendChild(textSpan);
        }

        terminalContent.appendChild(lineElement);

        function typeChar() {
            if (currentChar < line.text.length) {
                if (line.type === 'prompt') {
                    promptSpan.textContent += line.text[currentChar];
                } else {
                    textSpan.textContent += line.text[currentChar];
                }
                currentChar++;
                setTimeout(typeChar, 30 + Math.random() * 40);
            } else {
                currentChar = 0;
                currentLine++;
                isTyping = false;

                // Auto-scroll to bottom
                terminalContent.scrollTop = terminalContent.scrollHeight;

                // Continue to next line after a delay
                const delay = line.type === 'ai' ? 1000 : 500;
                setTimeout(typeWriter, delay + Math.random() * 800);
            }
        }

        if (line.type !== 'cursor') {
            typeChar();
        }
    }

    // Start typing animation after a delay
    setTimeout(typeWriter, 1500);
}

// Guide tabs functionality
function initGuideTabs() {
    const tabButtons = document.querySelectorAll('.guide-tab');
    const tabPanels = document.querySelectorAll('.guide-panel');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all tabs
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabPanels.forEach(panel => panel.classList.remove('active'));

            // Add active class to clicked tab
            button.classList.add('active');

            // Show corresponding panel
            const targetPanel = document.getElementById(button.dataset.method + '-guide');
            if (targetPanel) {
                targetPanel.classList.add('active');
            }
        });
    });
}

// Download tabs functionality
function initDownloadTabs() {
    const methodTabs = document.querySelectorAll('.method-tab');
    const methodPanels = document.querySelectorAll('.method-panel');

    methodTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs
            methodTabs.forEach(t => t.classList.remove('active'));
            methodPanels.forEach(panel => panel.classList.remove('active'));

            // Add active class to clicked tab
            tab.classList.add('active');

            // Show corresponding panel
            const targetPanel = document.getElementById(tab.dataset.method + '-method');
            if (targetPanel) {
                targetPanel.classList.add('active');
            }
        });
    });
}

// Copy to clipboard functionality
function initCopyToClipboard() {
    document.addEventListener('click', function(e) {
        if (e.target.closest('.copy-snippet')) {
            const button = e.target.closest('.copy-snippet');
            const codeElement = button.previousElementSibling;
            const code = codeElement.textContent || codeElement.innerText;

            navigator.clipboard.writeText(code).then(function() {
                const originalIcon = button.innerHTML;
                button.innerHTML = '<i class="fas fa-check"></i>';
                button.style.background = 'var(--success-color)';

                setTimeout(() => {
                    button.innerHTML = originalIcon;
                    button.style.background = '';
                }, 2000);
            }).catch(function(err) {
                console.error('Failed to copy: ', err);
            });
        }
    });
}

// Smooth scrolling for navigation links
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 70; // Account for fixed navbar
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Mobile menu functionality
function initMobileMenu() {
    const navLinks = document.querySelector('.nav-links');
    const menuToggle = document.createElement('button');
    menuToggle.className = 'menu-toggle';
    menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
    menuToggle.style.display = 'none';
    menuToggle.style.background = 'none';
    menuToggle.style.border = 'none';
    menuToggle.style.color = 'var(--text-secondary)';
    menuToggle.style.fontSize = '1.2rem';
    menuToggle.style.cursor = 'pointer';
    menuToggle.style.padding = '10px';

    document.querySelector('.nav-container').appendChild(menuToggle);

    menuToggle.addEventListener('click', function() {
        navLinks.classList.toggle('mobile-menu-open');
    });

    // Show/hide mobile menu based on screen size
    function checkScreenSize() {
        if (window.innerWidth <= 768) {
            menuToggle.style.display = 'block';
            navLinks.classList.add('mobile-menu');
        } else {
            menuToggle.style.display = 'none';
            navLinks.classList.remove('mobile-menu', 'mobile-menu-open');
        }
    }

    window.addEventListener('resize', checkScreenSize);
    checkScreenSize();
}

// Particle effects
function initParticleEffects() {
    // Create floating particles in background sections
    const sectionsWithParticles = ['.hero', '.features', '.download', '.footer'];

    sectionsWithParticles.forEach(selector => {
        const section = document.querySelector(selector);
        if (!section) return;

        const particleContainer = section.querySelector('.hero-particles, .features-particles, .download-particles, .footer-particles');
        if (!particleContainer) return;

        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.className = 'floating-particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 10 + 's';
            particle.style.animationDuration = (Math.random() * 10 + 15) + 's';
            particleContainer.appendChild(particle);
        }
    });
}

// Add mobile menu styles dynamically
const mobileMenuStyles = `
@media (max-width: 768px) {
    .nav-links.mobile-menu {
        position: absolute;
        top: 70px;
        left: 0;
        right: 0;
        background: rgba(10, 10, 10, 0.98);
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-top: none;
        flex-direction: column;
        gap: 0;
        max-height: 0;
        overflow: hidden;
        transition: var(--transition);
        box-shadow: var(--shadow);
    }

    .nav-links.mobile-menu.mobile-menu-open {
        max-height: 400px;
    }

    .nav-links.mobile-menu a {
        padding: 15px 20px;
        border-bottom: 1px solid var(--glass-border);
        transition: var(--transition);
    }

    .nav-links.mobile-menu a:hover {
        background: var(--glass-bg);
    }

    .nav-links.mobile-menu a:last-child {
        border-bottom: none;
    }
}

.floating-particle {
    position: absolute;
    width: 2px;
    height: 2px;
    background: var(--glass-border);
    border-radius: 50%;
    opacity: 0.6;
    animation: floatParticle 20s infinite linear;
    pointer-events: none;
}

@keyframes floatParticle {
    0% {
        transform: translateY(0px) translateX(0px) rotate(0deg);
        opacity: 0;
    }
    10% {
        opacity: 0.6;
    }
    90% {
        opacity: 0.6;
    }
    100% {
        transform: translateY(-100vh) translateX(50px) rotate(360deg);
        opacity: 0;
    }
}
`;

const styleSheet = document.createElement('style');
styleSheet.textContent = mobileMenuStyles;
document.head.appendChild(styleSheet);

// Performance monitoring (demo)
function initPerformanceDemo() {
    // Simulate real-time performance metrics
    setInterval(() => {
        const metrics = document.querySelectorAll('.performance-metric');
        metrics.forEach(metric => {
            const baseValue = parseFloat(metric.dataset.base || metric.textContent);
            const variation = (Math.random() - 0.5) * 0.1; // ±5% variation
            const newValue = baseValue * (1 + variation);
            metric.textContent = newValue.toFixed(1) + (metric.dataset.unit || '');
        });
    }, 3000);
}

// Initialize performance demo if elements exist
if (document.querySelector('.performance-metric')) {
    initPerformanceDemo();
}

// Add interactive hover effects
document.addEventListener('mouseover', function(e) {
    if (e.target.closest('.feature-card')) {
        const card = e.target.closest('.feature-card');
        card.style.transform = 'translateY(-10px) scale(1.02)';
    }
});

document.addEventListener('mouseout', function(e) {
    if (e.target.closest('.feature-card')) {
        const card = e.target.closest('.feature-card');
        card.style.transform = '';
    }
});

// Add click effects for buttons
document.addEventListener('mousedown', function(e) {
    if (e.target.closest('.btn')) {
        const btn = e.target.closest('.btn');
        btn.style.transform = 'scale(0.98)';
    }
});

document.addEventListener('mouseup', function(e) {
    if (e.target.closest('.btn')) {
        const btn = e.target.closest('.btn');
        btn.style.transform = '';
    }
});

// Export functions for potential external use
window.LorapokChatInterface = {
    initLoadingScreen,
    initNavigation,
    initScrollAnimations,
    initHeroAnimations,
    initTerminalDemo,
    initGuideTabs,
    initDownloadTabs,
    initCopyToClipboard,
    initCounterAnimations,
    initSmoothScrolling,
    initMobileMenu,
    initParticleEffects
};

// Smooth scrolling for navigation links
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Copy to clipboard functionality
function initCopyToClipboard() {
    document.querySelectorAll('.download-code').forEach(codeBlock => {
        const copyButton = document.createElement('button');
        copyButton.innerHTML = '<i class="fas fa-copy"></i> Copy';
        copyButton.className = 'btn btn-secondary copy-btn';
        copyButton.style.marginTop = '10px';

        codeBlock.appendChild(copyButton);

        copyButton.addEventListener('click', function() {
            const code = codeBlock.querySelector('code').textContent;
            navigator.clipboard.writeText(code).then(function() {
                const originalText = copyButton.innerHTML;
                copyButton.innerHTML = '<i class="fas fa-check"></i> Copied!';
                copyButton.classList.add('copied');

                setTimeout(() => {
                    copyButton.innerHTML = originalText;
                    copyButton.classList.remove('copied');
                }, 2000);
            });
        });
    });
}

// Mobile menu functionality
function initMobileMenu() {
    const navLinks = document.querySelector('.nav-links');
    const menuToggle = document.createElement('button');
    menuToggle.className = 'menu-toggle';
    menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
    menuToggle.style.display = 'none';
    menuToggle.style.background = 'none';
    menuToggle.style.border = 'none';
    menuToggle.style.color = 'var(--text-secondary)';
    menuToggle.style.fontSize = '1.2rem';
    menuToggle.style.cursor = 'pointer';

    document.querySelector('.nav-container').appendChild(menuToggle);

    menuToggle.addEventListener('click', function() {
        navLinks.classList.toggle('mobile-menu-open');
    });

    // Show/hide mobile menu based on screen size
    function checkScreenSize() {
        if (window.innerWidth <= 768) {
            menuToggle.style.display = 'block';
            navLinks.classList.add('mobile-menu');
        } else {
            menuToggle.style.display = 'none';
            navLinks.classList.remove('mobile-menu', 'mobile-menu-open');
        }
    }

    window.addEventListener('resize', checkScreenSize);
    checkScreenSize();
}

// Performance monitoring demo
function initPerformanceDemo() {
    const performanceElements = document.querySelectorAll('.performance-metric');

    performanceElements.forEach(element => {
        const targetValue = parseFloat(element.dataset.value);
        const suffix = element.dataset.suffix || '';
        let currentValue = 0;

        const interval = setInterval(() => {
            currentValue += targetValue / 50;
            if (currentValue >= targetValue) {
                currentValue = targetValue;
                clearInterval(interval);
            }
            element.textContent = currentValue.toFixed(1) + suffix;
        }, 50);
    });
}

// Initialize performance demo if elements exist
if (document.querySelector('.performance-metric')) {
    initPerformanceDemo();
}

// Add loading animation for demo terminal
function addLoadingAnimation() {
    const demoContent = document.querySelector('.demo-content');
    if (!demoContent) return;

    const loadingLines = [
        'Loading Ollama models...',
        'Initializing chat interface...',
        'Connecting to local server...',
        'Ready for interaction!'
    ];

    let lineIndex = 0;

    function showNextLine() {
        if (lineIndex < loadingLines.length) {
            const lineElement = document.createElement('div');
            lineElement.className = 'demo-line';
            lineElement.textContent = loadingLines[lineIndex];
            demoContent.appendChild(lineElement);
            lineIndex++;
            setTimeout(showNextLine, 500);
        }
    }

    setTimeout(showNextLine, 1000);
}

// Initialize demo loading animation
addLoadingAnimation();

// Add particle effect to hero background (optional)
function initParticleEffect() {
    const hero = document.querySelector('.hero');
    if (!hero) return;

    for (let i = 0; i < 50; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 20 + 's';
        particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
        hero.appendChild(particle);
    }
}

// Add particle styles
const particleStyles = `
.particle {
    position: absolute;
    width: 2px;
    height: 2px;
    background: var(--primary-color);
    border-radius: 50%;
    opacity: 0.3;
    animation: float 20s infinite linear;
}

@keyframes float {
    0% {
        transform: translateY(0px) rotate(0deg);
        opacity: 0;
    }
    10% {
        opacity: 0.3;
    }
    90% {
        opacity: 0.3;
    }
    100% {
        transform: translateY(-100vh) rotate(360deg);
        opacity: 0;
    }
}
`;

// Uncomment to enable particle effect
// const particleStyleSheet = document.createElement('style');
// particleStyleSheet.textContent = particleStyles;
// document.head.appendChild(particleStyleSheet);
// initParticleEffect();

// Export functions for potential external use
window.LorapokChatInterface = {
    initNavigation,
    initScrollAnimations,
    initTerminalDemo,
    initSmoothScrolling,
    initCopyToClipboard,
    initMobileMenu
};