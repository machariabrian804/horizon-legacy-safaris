(function () {
  'use strict';

  const state = {
    country: 'all',
    destination: 'all',
    type: 'all',
    duration: 'all',
    luxury: 'all',
    query: ''
  };

  function init() {
    const search = document.getElementById('catalogueSearch');
    if (search) {
      search.addEventListener('input', function (e) {
        state.query = e.target.value || '';
        apply();
      });
    }

    document.querySelectorAll('.pkg-chip[data-filter-country]').forEach(function (chip) {
      chip.addEventListener('click', function () {
        document.querySelectorAll('.pkg-chip[data-filter-country]').forEach(function (c) {
          c.classList.remove('is-active');
        });
        chip.classList.add('is-active');
        state.country = chip.getAttribute('data-filter-country') || 'all';
        apply();
      });
    });

    bindSelect('filterDestination', 'destination');
    bindSelect('filterType', 'type');
    bindSelect('filterDuration', 'duration');
    bindSelect('filterLuxury', 'luxury');

    const reset = document.getElementById('catalogueReset');
    if (reset) reset.addEventListener('click', resetAll);
    const emptyReset = document.getElementById('catalogueEmptyReset');
    if (emptyReset) emptyReset.addEventListener('click', resetAll);

    apply();
  }

  function bindSelect(id, key) {
    const el = document.getElementById(id);
    if (!el) return;
    el.addEventListener('change', function () {
      state[key] = el.value || 'all';
      apply();
    });
  }

  function resetAll() {
    state.country = 'all';
    state.destination = 'all';
    state.type = 'all';
    state.duration = 'all';
    state.luxury = 'all';
    state.query = '';

    const search = document.getElementById('catalogueSearch');
    if (search) search.value = '';

    document.querySelectorAll('.pkg-chip[data-filter-country]').forEach(function (c, i) {
      c.classList.toggle('is-active', i === 0);
    });

    ['filterDestination', 'filterType', 'filterDuration', 'filterLuxury'].forEach(function (id) {
      const el = document.getElementById(id);
      if (el) el.value = 'all';
    });

    apply();
  }

  function cardMatches(card) {
    if (state.country !== 'all' && card.getAttribute('data-country') !== state.country) return false;
    if (state.destination !== 'all') {
      const dests = (card.getAttribute('data-destinations') || '').split('|');
      if (dests.indexOf(state.destination) === -1) return false;
    }
    if (state.type !== 'all' && card.getAttribute('data-type') !== state.type) return false;
    if (state.duration !== 'all' && card.getAttribute('data-duration') !== state.duration) return false;
    if (state.luxury !== 'all' && card.getAttribute('data-luxury') !== state.luxury) return false;
    const q = state.query.trim().toLowerCase();
    if (q) {
      const blob = (card.getAttribute('data-search') || '').toLowerCase();
      if (blob.indexOf(q) === -1) return false;
    }
    return true;
  }

  function apply() {
    const cards = document.querySelectorAll('.pkg-card');
    let visibleCount = 0;
    const groups = {};

    cards.forEach(function (card) {
      const ok = cardMatches(card);
      card.style.display = ok ? '' : 'none';
      if (ok) visibleCount++;

      const group = card.closest('.pkg-group');
      if (group) {
        if (!groups[group.id]) groups[group.id] = { el: group, any: false };
        if (ok) groups[group.id].any = true;
      }
    });

    Object.keys(groups).forEach(function (id) {
      const g = groups[id];
      g.el.style.display = g.any ? '' : 'none';
    });

    const countEl = document.getElementById('catalogueCount');
    const total = cards.length;
    if (countEl) {
      if (visibleCount === total) {
        countEl.textContent = 'Showing ' + total + ' packages';
      } else {
        countEl.textContent = 'Showing ' + visibleCount + ' of ' + total + ' packages';
      }
    }

    const empty = document.getElementById('catalogueEmpty');
    if (empty) {
      empty.hidden = visibleCount !== 0;
    }

    const resetBtn = document.getElementById('catalogueReset');
    if (resetBtn) {
      const filtered = state.country !== 'all' || state.destination !== 'all' ||
        state.type !== 'all' || state.duration !== 'all' || state.luxury !== 'all' ||
        state.query.trim() !== '';
      resetBtn.hidden = !filtered;
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();