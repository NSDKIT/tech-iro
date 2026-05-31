(function () {
  'use strict';

  /* ── Header scroll ──────────────────────────────────────────────── */
  var header = document.querySelector('.header');
  if (header) {
    window.addEventListener('scroll', function () {
      header.classList.toggle('scrolled', window.scrollY > 0);
    }, { passive: true });
  }

  /* ── Hamburger ──────────────────────────────────────────────────── */
  var hamburger = document.querySelector('.hamburger');
  var mobileNav = document.querySelector('.mobile-nav');
  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', function () {
      var isOpen = mobileNav.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', isOpen);
    });
    mobileNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileNav.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ── Smooth scroll ──────────────────────────────────────────────── */
  document.querySelectorAll('a[href*="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var href = anchor.getAttribute('href');
      var hash = href.indexOf('#') !== -1 ? href.slice(href.indexOf('#')) : null;
      if (!hash || hash === '#') return;
      var target = document.querySelector(hash);
      if (target) {
        e.preventDefault();
        window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 72, behavior: 'smooth' });
      }
    });
  });

  /* ── Contact form ───────────────────────────────────────────────── */
  var form = document.querySelector('.contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('.form-submit');
      btn.textContent = '送信しました。ありがとうございます。';
      btn.disabled = true;
      btn.style.opacity = '0.6';
    });
  }

  /* ── Scroll reveal ──────────────────────────────────────────────── */
  if (!('IntersectionObserver' in window)) return;

  var vh = window.innerHeight;

  /*
   * Groups: observe each child individually.
   * Stagger delay = (column index) × ms, so items in the same row
   * pop in left-to-right when they enter the viewport together.
   */
  var groups = [
    { parent: '.stats-grid',      child: '.stat-item',      cols: 3, ms: 90 },
    { parent: '.works-grid',      child: '.work-card',       cols: 2, ms: 90 },
    { parent: '.works-full-grid', child: '.work-full-card',  cols: 2, ms: 90 },
    { parent: '.services-list',   child: '.service-item',    cols: 1, ms: 0  },
    { parent: '.strengths-grid',  child: '.strength-item',   cols: 2, ms: 90 },
    { parent: '.philosophy-list', child: '.philosophy-item', cols: 1, ms: 0  },
    { parent: '.skills-grid',     child: '.skill-item',      cols: 3, ms: 90 },
    { parent: '.info-grid',       child: '.info-item',       cols: 2, ms: 70 },
  ];

  var groupMeta = new Map(); /* el → { index, cols, ms } */

  groups.forEach(function (g) {
    var parent = document.querySelector(g.parent);
    if (!parent) return;
    parent.querySelectorAll(g.child).forEach(function (el, i) {
      if (el.getBoundingClientRect().top > vh * 0.82) {
        el.setAttribute('data-reveal', '');
        groupMeta.set(el, { index: i, cols: g.cols, ms: g.ms });
      }
    });
  });

  /* Solo elements — each reveals as it individually enters the viewport */
  var soloSelectors = [
    '.section-label', '.section-title', '.divider',
    '.about-lead', '.about-block-title',
    '.profile-inner', '.works-cta', '.contact-intro',
    '.page-hero-label', '.page-hero-title', '.page-hero-sub',
  ];

  soloSelectors.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) {
      if (groupMeta.has(el)) return;
      if (el.getBoundingClientRect().top > vh * 0.82) {
        el.setAttribute('data-reveal', '');
      }
    });
  });

  /* One shared observer for all [data-reveal] elements */
  var revealIO = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      revealIO.unobserve(entry.target);
      var meta = groupMeta.get(entry.target);
      var delay = meta ? (meta.index % meta.cols) * meta.ms : 0;
      setTimeout(function () {
        entry.target.classList.add('is-visible');
      }, delay);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -28px 0px' });

  document.querySelectorAll('[data-reveal]').forEach(function (el) {
    revealIO.observe(el);
  });

  /* ── Stats counter ──────────────────────────────────────────────── */
  var statsSection = document.querySelector('.stats-section');
  if (statsSection) {
    var statsIO = new IntersectionObserver(function (entries) {
      if (!entries[0].isIntersecting) return;
      statsIO.disconnect();
      statsSection.querySelectorAll('.stat-number').forEach(function (numEl) {
        var raw = numEl.textContent.trim();
        var target = parseInt(raw, 10);
        if (isNaN(target)) return;
        var t0 = performance.now();
        var dur = 1500;
        (function tick(now) {
          var p = Math.min((now - t0) / dur, 1);
          numEl.textContent = Math.round((1 - Math.pow(1 - p, 4)) * target); /* ease-out quart */
          if (p < 1) requestAnimationFrame(tick);
          else numEl.textContent = raw;
        })(t0);
      });
    }, { threshold: 0.45 });
    statsIO.observe(statsSection);
  }

}());
