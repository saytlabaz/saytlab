/**
 * Rahat İzle — animasiya və mobil menyu nəzarəti.
 */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  // document.documentElement.classList.add('js-reveal');

  /* --- 1. Scroll-reveal (Performance optimized - One Time) --- */
  function initReveal() {
    var targets = document.querySelectorAll('[data-reveal]');
    if (!targets.length) return;

    if (reduceMotion || !('IntersectionObserver' in window)) {
      for (var i = 0; i < targets.length; i++) targets[i].classList.add('is-revealed');
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
          } else {
            // Advanced mirror logic to prevent Safari flickering on large elements
            var rect = entry.boundingClientRect;
            // Only remove if it's completely scrolled out of view (either above or below)
            if (rect.top > (window.innerHeight || document.documentElement.clientHeight) || rect.bottom < 0) {
              entry.target.classList.remove('is-revealed');
            }
          }
        });
      },
      { threshold: 0, rootMargin: '0px 0px -10% 0px' }
    );

    targets.forEach(function (el) {
      observer.observe(el);
    });
  }

  /* --- 2. Mobil menyu --- */
  function initMobileMenu() {
    var toggle = document.getElementById('mobileMenuToggle');
    var menu = document.getElementById('mobileMenu');
    if (!toggle || !menu) return;

    function setOpen(open) {
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      menu.classList.toggle('is-open', open);
    }

    toggle.addEventListener('click', function (e) {
      e.stopPropagation();
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });

    document.addEventListener('click', function (e) {
      if (menu.classList.contains('is-open') && !menu.contains(e.target)) setOpen(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setOpen(false);
    });

    menu.addEventListener('click', function (e) {
      if (e.target.closest('a, button')) setOpen(false);
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth >= 1024) setOpen(false);
    });
  }

  /* --- 3. Sayğac animasiyası (One Time) --- */
  function initCounters() {
    var targets = document.querySelectorAll('[data-count-to]');
    if (!targets.length) return;

    var duration = 2000;
    var countersData = new Map();

    targets.forEach(el => {
        countersData.set(el, {
            target: parseInt(el.getAttribute('data-count-to'), 10),
            suffix: el.getAttribute('data-count-suffix') || '',
            animating: false
        });
    });

    function animateCount(el) {
      var data = countersData.get(el);
      if(data.animating) return;
      data.animating = true;
      var start = null;

      function step(timestamp) {
        if (start === null) start = timestamp;
        var progress = Math.min((timestamp - start) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(data.target * eased) + data.suffix;
        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          el.textContent = data.target + data.suffix;
          data.animating = false;
        }
      }
      requestAnimationFrame(step);
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animateCount(entry.target);
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1 }
    );

    targets.forEach(function (el) {
      observer.observe(el);
    });
  }

  /* --- 4. Navbar scroll --- */
  function initNavbarScroll() {
      const navbar = document.getElementById('navbar');
      if(!navbar) return;
      window.addEventListener('scroll', () => {
          if (window.scrollY > 20) {
              navbar.classList.add('py-2');
              navbar.classList.remove('py-4');
          } else {
              navbar.classList.add('py-4');
              navbar.classList.remove('py-2');
          }
      }, { passive: true });
  }

  /* --- 6. Magnetic Buttons --- */
  function initMagnetic() {
    if (reduceMotion) return;
    const magnets = document.querySelectorAll('[data-magnetic]');
    magnets.forEach(btn => {
      let isHovering = false;
      let x = 0;
      let y = 0;
      let targetX = 0;
      let targetY = 0;

      btn.addEventListener('mouseenter', () => { isHovering = true; });
      btn.addEventListener('mousemove', (e) => {
        const rect = btn.getBoundingClientRect();
        targetX = (e.clientX - rect.left - rect.width / 2) * 0.4;
        targetY = (e.clientY - rect.top - rect.height / 2) * 0.4;
      });
      btn.addEventListener('mouseleave', () => {
        isHovering = false;
        targetX = 0;
        targetY = 0;
      });

      function animate() {
        x += (targetX - x) * 0.1;
        y += (targetY - y) * 0.1;
        btn.style.transform = `translate(${x}px, ${y}px)`;
        requestAnimationFrame(animate);
      }
      animate();
    });
  }

  /* --- 7. Tilt Effect --- */
  function initTilt() {
    if (reduceMotion) return;
    const cards = document.querySelectorAll('.tilt-card');
    cards.forEach(card => {
      let targetRotateX = 0;
      let targetRotateY = 0;
      let currentRotateX = 0;
      let currentRotateY = 0;
      let isHovering = false;

      card.addEventListener('mouseenter', () => { isHovering = true; });
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        targetRotateX = ((y - centerY) / centerY) * -8;
        targetRotateY = ((x - centerX) / centerX) * 8;
      });
      card.addEventListener('mouseleave', () => {
        isHovering = false;
        targetRotateX = 0;
        targetRotateY = 0;
      });

      function animate() {
        currentRotateX += (targetRotateX - currentRotateX) * 0.1;
        currentRotateY += (targetRotateY - currentRotateY) * 0.1;
        
        if(isHovering || Math.abs(currentRotateX) > 0.01 || Math.abs(currentRotateY) > 0.01) {
            card.style.transform = `perspective(1000px) rotateX(${currentRotateX}deg) rotateY(${currentRotateY}deg) scale3d(${isHovering?1.03:1}, ${isHovering?1.03:1}, ${isHovering?1.03:1})`;
        }
        requestAnimationFrame(animate);
      }
      animate();
    });
  }

  
  /* --- 8. Custom Cursor --- */
  function initCursor() {
    if (reduceMotion) return;
    var matchMedia = window.matchMedia('(pointer: fine)');
    if (!matchMedia.matches) return;

    var dot = document.querySelector('.cursor-dot');
    var ring = document.querySelector('.cursor-ring');
    if (!dot || !ring) return;

    var root = document.documentElement;
    root.classList.add('cursor-custom');

    var pointer = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
    var cursor = { rx: pointer.x, ry: pointer.y };

    window.addEventListener('mousemove', function(e) {
      pointer.x = e.clientX;
      pointer.y = e.clientY;
      if (e.target.closest('a, button, [data-magnetic], [data-cursor-hot], .ig-card')) {
        root.classList.add('cursor-hot');
      } else {
        root.classList.remove('cursor-hot');
      }
    }, { passive: true });

    // mouseleave removed
    // mouseenter removed
    // blur removed

    function lerp(start, end, amt) {
      return (1 - amt) * start + amt * end;
    }

    function renderCursor() {
      dot.style.transform = `translate3d(${pointer.x}px, ${pointer.y}px, 0)`;
      cursor.rx = lerp(cursor.rx, pointer.x, 0.2);
      cursor.ry = lerp(cursor.ry, pointer.y, 0.2);
      ring.style.transform = `translate3d(${cursor.rx.toFixed(2)}px, ${cursor.ry.toFixed(2)}px, 0)`;
      requestAnimationFrame(renderCursor);
    }
    requestAnimationFrame(renderCursor);
  }

  
  /* --- 9. FAQ Accordion --- */
  function initFAQ() {
    const faqBtns = document.querySelectorAll('.faq-btn');
    faqBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const content = btn.nextElementSibling;
        const icon = btn.querySelector('i');
        
        // Close all other accordions
        faqBtns.forEach(otherBtn => {
            if(otherBtn !== btn) {
                otherBtn.nextElementSibling.style.maxHeight = null;
                otherBtn.querySelector('i').style.transform = 'rotate(0deg)';
            }
        });

        if (content.style.maxHeight) {
          content.style.maxHeight = null;
          icon.style.transform = 'rotate(0deg)';
        } else {
          content.style.maxHeight = content.scrollHeight + 'px';
          icon.style.transform = 'rotate(180deg)';
        }
      });
    });
  }

  

  /* --- 10. Lightbox Gallery --- */
  function initLightbox() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.getElementById('lightbox-close');

    if (!lightbox || galleryItems.length === 0) return;

    function openLightbox(src) {
        lightboxImg.src = src;
        lightbox.classList.remove('hidden');
        // Small delay to allow display block to apply before animating opacity
        setTimeout(() => {
            lightbox.classList.remove('opacity-0');
            lightboxImg.classList.remove('scale-95');
            lightboxImg.classList.add('scale-100');
        }, 10);
    }

    function closeLightbox() {
        lightbox.classList.add('opacity-0');
        lightboxImg.classList.remove('scale-100');
        lightboxImg.classList.add('scale-95');
        setTimeout(() => {
            lightbox.classList.add('hidden');
            lightboxImg.src = '';
        }, 300);
    }

    galleryItems.forEach(item => {
        item.addEventListener('click', () => {
            const src = item.getAttribute('data-src');
            if(src) openLightbox(src);
        });
    });

    closeBtn.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !lightbox.classList.contains('hidden')) {
            closeLightbox();
        }
    });
  }


  function init() {
    // initReveal(); removed in favor of AOS
    setTimeout(() => window.dispatchEvent(new Event("scroll")), 100);
    initMobileMenu();
    initCounters();
    initNavbarScroll();
    initMagnetic();
    initTilt();
    initCursor();
    initFAQ();
    initLightbox();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }


})();


  
  /* --- Bulletproof Smooth Scroll (Works on ALL Safari versions) --- */
  function customSmoothScrollTo(targetPosition, duration) {
    const startPosition = window.pageYOffset;
    const distance = targetPosition - startPosition;
    let startTime = null;

    function animation(currentTime) {
      if (startTime === null) startTime = currentTime;
      const timeElapsed = currentTime - startTime;
      const progress = Math.min(timeElapsed / duration, 1);
      
      // Easing function (easeOutQuart - starts fast instantly, slows down at the end)
      const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
        
      window.scrollTo(0, startPosition + distance * ease);
      
      if (timeElapsed < duration) {
        requestAnimationFrame(animation);
      }
    }
    
    requestAnimationFrame(animation);
  }

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      
      // If it's just # or #top, it means scroll to top
      const isTop = (targetId === '#' || targetId === '#top');
      const targetElement = isTop ? null : document.querySelector(targetId);
      
      if (isTop || targetElement) {
        e.preventDefault();
        
        const topPos = isTop ? 0 : targetElement.getBoundingClientRect().top + window.pageYOffset;
        
        // Slower cinematic scroll (1800ms) as requested by user
        customSmoothScrollTo(topPos, 800);
        
        // Close mobile menu if open
        const mobileMenu = document.getElementById('mobileMenu');
        const mobileMenuToggle = document.getElementById('mobileMenuToggle');
        if (mobileMenu && mobileMenu.classList.contains('is-open')) {
            mobileMenu.classList.remove('is-open');
            if (mobileMenuToggle) mobileMenuToggle.setAttribute('aria-expanded', 'false');
        }
      }
    });
  });
