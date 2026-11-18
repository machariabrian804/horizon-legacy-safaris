/**
 * HORIZON LEGACY - 3D DEPTH FOR THE DESTINATION LISTING
 *
 * Card tilt follows the pointer in 3D, released with a spring. The hero gains
 * a scroll-linked depth shift. Everything is skipped when the visitor asks for
 * reduced motion, and the grid is only marked interactive once JS has run.
 */

(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (reduceMotion.matches) return;
  if (!window.Motion || typeof window.Motion.animate !== 'function') return;

  var Motion = window.Motion;
  var MAX_TILT = 7;

  /* ---------------------------------------------------------------- cards */
  function initCardTilt() {
    var grid = document.getElementById('destinationsGrid');
    if (!grid) return;

    grid.classList.add('tilt-enabled');

    grid.addEventListener('pointermove', function (event) {
      if (event.pointerType === 'touch') return;
      var card = event.target.closest('.dest-card');
      if (!card) return;

      var rect = card.getBoundingClientRect();
      var x = (event.clientX - rect.left) / rect.width - 0.5;
      var y = (event.clientY - rect.top) / rect.height - 0.5;

      card.style.transform =
        'rotateX(' + (-y * MAX_TILT).toFixed(2) + 'deg) ' +
        'rotateY(' + (x * MAX_TILT).toFixed(2) + 'deg) ' +
        'translateY(-6px) translateZ(0)';
      card.style.setProperty('--glare-x', (x * 100 + 50).toFixed(0) + '%');
      card.style.setProperty('--glare-y', (y * 100 + 50).toFixed(0) + '%');
    });

    // The reset is a CSS transition rather than a spring so it still settles
    // when the page is in a background tab and requestAnimationFrame is paused.
    function release(card) {
      if (!card.style.transform) return;
      card.classList.add('is-untilt');
      card.style.transform = '';

      var done = function () {
        card.classList.remove('is-untilt');
        card.removeEventListener('transitionend', done);
      };
      card.addEventListener('transitionend', done);
      window.setTimeout(done, 600);
    }

    grid.addEventListener('pointerout', function (event) {
      var card = event.target.closest('.dest-card');
      if (!card) return;
      if (card.contains(event.relatedTarget)) return;
      release(card);
    });

    // Cards are re-rendered on filter/pagination, so clear any leftover tilt.
    grid.addEventListener('pointerleave', function () {
      Array.prototype.forEach.call(grid.querySelectorAll('.dest-card'), release);
    });
  }

  /* ----------------------------------------------------------------- hero */
  function initHeroDepth() {
    var hero = document.querySelector('.destinations-hero');
    var content = hero && hero.querySelector('.destinations-hero-content');
    if (!hero || !content) return;

    Motion.scroll(function (progress) {
      content.style.transform =
        'perspective(1200px) translateY(' + (progress * -26).toFixed(1) + 'px) ' +
        'scale(' + (1 - progress * 0.02).toFixed(3) + ')';
      content.style.opacity = String(Math.max(0, 1 - progress * 0.85));
    }, { target: hero, offset: ['start start', 'end start'] });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initCardTilt();
      initHeroDepth();
    });
  } else {
    initCardTilt();
    initHeroDepth();
  }
})();
