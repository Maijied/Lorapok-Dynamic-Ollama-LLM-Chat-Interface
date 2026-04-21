// Lorapok Dynamic Ollama LLM Chat Interface - Interactive Features

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all features
    initNavigation();
    initScrollAnimations();
    initTerminalDemo();
    initSmoothScrolling();
    initCopyToClipboard();
    initMobileMenu();
});

// Navigation functionality
function initNavigation() {
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.nav-links a');

    // Navbar background on scroll
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(10, 10, 10, 0.98)';
        } else {
            navbar.style.background = 'rgba(10, 10, 10, 0.95)';
        }
    });

    // Active link highlighting
    window.addEventListener('scroll', function() {
        const sections = document.querySelectorAll('section');
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

// Scroll animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);

    // Observe all feature cards, requirement cards, etc.
    document.querySelectorAll('.feature-card, .requirement-card, .command-category, .download-card, .api-code, .api-features').forEach(card => {
        observer.observe(card);
    });
}

// Terminal demo animation
function initTerminalDemo() {
    const terminalLines = [
        { type: 'prompt', text: 'ollama-chat> ' },
        { type: 'command', text: 'list-models' },
        { type: 'response', text: 'Available models:' },
        { type: 'response', text: '  • llama2:7b' },
        { type: 'response', text: '  • codellama:7b' },
        { type: 'response', text: '  • mistral:7b' },
        { type: 'prompt', text: 'ollama-chat> ' },
        { type: 'command', text: 'switch llama2:7b' },
        { type: 'response', text: 'Switched to model: llama2:7b' },
        { type: 'prompt', text: 'ollama-chat> ' },
        { type: 'command', text: 'chat' },
        { type: 'response', text: 'Starting interactive chat session...' },
        { type: 'ai', text: 'AI: Hello! How can I help you today?' },
        { type: 'prompt', text: 'You> ' },
        { type: 'input', text: 'Tell me about Python programming' },
        { type: 'ai', text: 'AI: Python is a high-level programming language known for its simplicity and readability...' },
        { type: 'prompt', text: 'ollama-chat> ' },
        { type: 'command', text: 'benchmark' },
        { type: 'response', text: 'Running performance benchmark...' },
        { type: 'response', text: 'Response time: 2.3s | Memory usage: 1.2GB | CPU: 45%' },
        { type: 'prompt', text: 'ollama-chat> ' },
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

        terminalContent.appendChild(lineElement);

        function typeChar() {
            if (currentChar < line.text.length) {
                lineElement.textContent += line.text[currentChar];
                currentChar++;
                setTimeout(typeChar, 50 + Math.random() * 50);
            } else {
                currentChar = 0;
                currentLine++;
                isTyping = false;

                // Auto-scroll to bottom
                terminalContent.scrollTop = terminalContent.scrollHeight;

                // Continue to next line after a delay
                setTimeout(typeWriter, 800 + Math.random() * 1200);
            }
        }

        typeChar();
    }

    // Start typing animation after a delay
    setTimeout(typeWriter, 1000);
}

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

// Add mobile menu styles dynamically
const mobileMenuStyles = `
@media (max-width: 768px) {
    .nav-links.mobile-menu {
        position: absolute;
        top: 70px;
        left: 0;
        right: 0;
        background: var(--darker-bg);
        border: 1px solid var(--border-color);
        border-top: none;
        flex-direction: column;
        gap: 0;
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.3s ease;
    }

    .nav-links.mobile-menu.mobile-menu-open {
        max-height: 300px;
    }

    .nav-links.mobile-menu a {
        padding: 15px 20px;
        border-bottom: 1px solid var(--border-color);
    }

    .nav-links.mobile-menu a:last-child {
        border-bottom: none;
    }
}
`;

const styleSheet = document.createElement('style');
styleSheet.textContent = mobileMenuStyles;
document.head.appendChild(styleSheet);

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