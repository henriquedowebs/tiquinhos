/**
 * Espaço Tiquinho's Pet — Interatividade e UX
 * Apex Lead Standard (Emil Kowalski)
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Header scroll elevation
    const header = document.getElementById('header');
    const handleScroll = () => {
        if (window.scrollY > 20) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });

    // 2. Mobile Menu Drawer
    const mobileToggle = document.getElementById('mobileToggle');
    const mobileDrawer = document.getElementById('mobileDrawer');
    const mobileOverlay = document.getElementById('mobileOverlay');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

    const toggleMenu = (open) => {
        const isOpen = open !== undefined ? open : !mobileDrawer.classList.contains('open');
        mobileToggle.classList.toggle('active', isOpen);
        mobileDrawer.classList.toggle('open', isOpen);
        mobileOverlay.classList.toggle('active', isOpen);
        mobileToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        mobileDrawer.setAttribute('aria-hidden', isOpen ? 'false' : 'true');

        if (isOpen) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    };

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => toggleMenu());
    }

    if (mobileOverlay) {
        mobileOverlay.addEventListener('click', () => toggleMenu(false));
    }

    mobileNavLinks.forEach(link => {
        link.addEventListener('click', () => toggleMenu(false));
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && mobileDrawer.classList.contains('open')) {
            toggleMenu(false);
        }
    });

    // 3. Category Chips Filtering (Inspirado na Referência)
    const categoryChips = document.querySelectorAll('.chip-btn');
    const serviceCards = document.querySelectorAll('.service-card');

    categoryChips.forEach(chip => {
        chip.addEventListener('click', () => {
            categoryChips.forEach(c => c.classList.remove('active'));
            chip.classList.add('active');

            const selectedCategory = chip.getAttribute('data-category');

            serviceCards.forEach(card => {
                const cardCategories = card.getAttribute('data-category') || '';
                if (selectedCategory === 'all' || cardCategories.includes(selectedCategory)) {
                    card.style.display = 'flex';
                    card.style.opacity = '0';
                    setTimeout(() => {
                        card.style.transition = 'opacity 0.3s ease';
                        card.style.opacity = '1';
                    }, 20);
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

    // 4. Quick Booking Form (WhatsApp Generator)
    const bookingForm = document.getElementById('bookingForm');
    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const tutorName = document.getElementById('tutorName').value.trim();
            const petName = document.getElementById('petName').value.trim();
            const serviceSelect = document.getElementById('serviceSelect').value;
            const preferredDate = document.getElementById('preferredDate').value.trim();

            let message = `Olá! Me chamo ${tutorName} e gostaria de agendar ${serviceSelect} para o meu pet ${petName}`;
            if (preferredDate) {
                message += ` (preferência: ${preferredDate})`;
            }
            message += ` no Espaço Tiquinho's Pet.`;

            const encodedMessage = encodeURIComponent(message);
            const whatsappUrl = `https://wa.me/5511978728736?text=${encodedMessage}`;

            window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
        });
    }

    // 5. FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const questionBtn = item.querySelector('.faq-question');
        questionBtn.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            faqItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                    const otherBtn = otherItem.querySelector('.faq-question');
                    if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
                }
            });

            item.classList.toggle('active', !isActive);
            questionBtn.setAttribute('aria-expanded', !isActive ? 'true' : 'false');
        });
    });

    // 6. Smooth Anchor Scrolling with Header Offset
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const headerHeight = header ? header.offsetHeight : 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerHeight - 16;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});
