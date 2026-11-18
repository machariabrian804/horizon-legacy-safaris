/**
 * HORIZON LEGACY SAFARIS - DESTINATION DISCOVERY APPLICATION
 * Handles instant search, regional filters, category tags, pagination (12/page),
 * interactive Leaflet map integration, and responsive card rendering.
 */

(function () {
  'use strict';

  // State Management
  const state = {
    searchQuery: '',
    activeRegion: 'all',
    activeCategory: 'all',
    currentPage: 1,
    perPage: 12,
    mapVisible: false,
    leafletMap: null,
    markersLayer: null
  };

  // Respect the OS motion preference for programmatic scrolling
  const reducedMotionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  const scrollBehavior = () => (reducedMotionQuery.matches ? 'auto' : 'smooth');

  // DOM Elements cache
  let elements = {};

  document.addEventListener('DOMContentLoaded', initDestinationsApp);

  function initDestinationsApp() {
    cacheElements();
    readUrlParams();
    bindEvents();
    renderRegionalCounts();
    applyFiltersAndRender();
  }

  function cacheElements() {
    elements = {
      searchInput: document.getElementById('destSearchInput'),
      searchForm: document.getElementById('destSearchForm'),
      searchClearBtn: document.getElementById('destSearchClear'),
      regionPills: document.querySelectorAll('.region-pill'),
      categoryChips: document.querySelectorAll('.category-chip'),
      grid: document.getElementById('destinationsGrid'),
      pagination: document.getElementById('destPagination'),
      resultsCount: document.getElementById('resultsCountText'),
      clearFiltersBtn: document.getElementById('clearFiltersBtn'),
      toggleMapBtn: document.getElementById('toggleMapBtn'),
      mapSection: document.getElementById('destinationMapSection'),
      mapContainer: document.getElementById('destinationMapContainer'),
      noResults: document.getElementById('noResultsBox')
    };
  }

  function readUrlParams() {
    try {
      const params = new URLSearchParams(window.location.search);
      const regionParam = params.get('region');
      const catParam = params.get('category');
      const searchParam = params.get('q');
      const pageParam = parseInt(params.get('page'), 10);

      if (regionParam) state.activeRegion = regionParam.toLowerCase();
      if (catParam) state.activeCategory = catParam;
      if (searchParam) {
        state.searchQuery = searchParam;
        if (elements.searchInput) elements.searchInput.value = searchParam;
        if (elements.searchClearBtn) elements.searchClearBtn.classList.add('visible');
      }
      if (pageParam && !isNaN(pageParam) && pageParam > 0) {
        state.currentPage = pageParam;
      }
    } catch (e) {
      console.warn('Could not parse URL query parameters', e);
    }
  }

  function syncUrlParams() {
    try {
      const url = new URL(window.location);
      if (state.activeRegion && state.activeRegion !== 'all') {
        url.searchParams.set('region', state.activeRegion);
      } else {
        url.searchParams.delete('region');
      }

      if (state.activeCategory && state.activeCategory !== 'all') {
        url.searchParams.set('category', state.activeCategory);
      } else {
        url.searchParams.delete('category');
      }

      if (state.searchQuery.trim()) {
        url.searchParams.set('q', state.searchQuery.trim());
      } else {
        url.searchParams.delete('q');
      }

      if (state.currentPage > 1) {
        url.searchParams.set('page', state.currentPage);
      } else {
        url.searchParams.delete('page');
      }

      window.history.replaceState({}, '', url.toString());
    } catch (e) {
      // Ignore if history state fails
    }
  }

  function bindEvents() {
    // Instant Search Input
    if (elements.searchInput) {
      elements.searchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value;
        state.currentPage = 1;
        if (elements.searchClearBtn) {
          elements.searchClearBtn.classList.toggle('visible', state.searchQuery.length > 0);
        }
        applyFiltersAndRender();
      });
    }

    if (elements.searchForm) {
      elements.searchForm.addEventListener('submit', (e) => {
        e.preventDefault();
        // Scroll smoothly to discovery grid
        const target = document.getElementById('discoveryGridAnchor');
        if (target) {
          target.scrollIntoView({ behavior: scrollBehavior() });
        }
      });
    }

    if (elements.searchClearBtn) {
      elements.searchClearBtn.addEventListener('click', () => {
        if (elements.searchInput) elements.searchInput.value = '';
        state.searchQuery = '';
        state.currentPage = 1;
        elements.searchClearBtn.classList.remove('visible');
        applyFiltersAndRender();
      });
    }

    // Regional Filter Pills
    if (elements.regionPills) {
      elements.regionPills.forEach((pill) => {
        pill.addEventListener('click', () => {
          const region = pill.getAttribute('data-region') || 'all';
          elements.regionPills.forEach((p) => p.classList.remove('active'));
          pill.classList.add('active');
          state.activeRegion = region.toLowerCase();
          state.currentPage = 1;
          applyFiltersAndRender();
        });
      });
    }

    // Category Filter Chips
    if (elements.categoryChips) {
      elements.categoryChips.forEach((chip) => {
        chip.addEventListener('click', () => {
          const category = chip.getAttribute('data-category') || 'all';
          if (state.activeCategory === category && category !== 'all') {
            // Toggle off
            state.activeCategory = 'all';
            chip.classList.remove('active');
            const allChip = document.querySelector('.category-chip[data-category="all"]');
            if (allChip) allChip.classList.add('active');
          } else {
            elements.categoryChips.forEach((c) => c.classList.remove('active'));
            chip.classList.add('active');
            state.activeCategory = category;
          }
          state.currentPage = 1;
          applyFiltersAndRender();
        });
      });
    }

    // Clear Filters Button
    if (elements.clearFiltersBtn) {
      elements.clearFiltersBtn.addEventListener('click', resetAllFilters);
    }

    // Toggle Map Button
    if (elements.toggleMapBtn) {
      elements.toggleMapBtn.addEventListener('click', toggleMapVisibility);
    }
  }

  function resetAllFilters() {
    state.searchQuery = '';
    state.activeRegion = 'all';
    state.activeCategory = 'all';
    state.currentPage = 1;

    if (elements.searchInput) elements.searchInput.value = '';
    if (elements.searchClearBtn) elements.searchClearBtn.classList.remove('visible');

    if (elements.regionPills) {
      elements.regionPills.forEach((p) => {
        const isAll = (p.getAttribute('data-region') || '').toLowerCase() === 'all';
        p.classList.toggle('active', isAll);
      });
    }

    if (elements.categoryChips) {
      elements.categoryChips.forEach((c) => {
        const isAll = (c.getAttribute('data-category') || '').toLowerCase() === 'all';
        c.classList.toggle('active', isAll);
      });
    }

    applyFiltersAndRender();
  }

  function renderRegionalCounts() {
    if (!window.DESTINATIONS_DATA || !Array.isArray(window.DESTINATIONS_DATA)) return;
    const all = window.DESTINATIONS_DATA;

    if (elements.regionPills) {
      elements.regionPills.forEach((pill) => {
        const region = (pill.getAttribute('data-region') || '').toLowerCase();
        let count = 0;
        if (region === 'all') {
          count = all.length;
        } else if (region === 'kenya') {
          count = all.filter((d) => d.region.toLowerCase() === 'kenya' || (d.regions && d.regions.includes('Kenya'))).length;
        } else if (region === 'africa') {
          count = all.filter((d) => (d.regions && d.regions.includes('Africa')) || d.region.toLowerCase() === 'africa').length;
        } else if (region === 'east africa') {
          count = all.filter((d) => (d.regions && d.regions.includes('East Africa')) || d.region.toLowerCase() === 'east africa').length;
        } else if (region === 'middle east') {
          count = all.filter((d) => (d.regions && d.regions.includes('Middle East')) || d.region.toLowerCase() === 'middle east').length;
        } else {
          count = all.filter((d) => d.region.toLowerCase() === region).length;
        }

        const countEl = pill.querySelector('.pill-count');
        if (countEl) countEl.textContent = count;
      });
    }
  }

  function filterDestinations() {
    if (!window.DESTINATIONS_DATA || !Array.isArray(window.DESTINATIONS_DATA)) return [];
    const all = window.DESTINATIONS_DATA;

    const query = state.searchQuery.trim().toLowerCase();
    const region = state.activeRegion;
    const category = state.activeCategory;

    return all.filter((dest) => {
      // 1. Regional Filter Check
      if (region !== 'all') {
        if (region === 'kenya') {
          // Dedicated Kenya filter
          const isKenya = dest.region.toLowerCase() === 'kenya' ||
                          (dest.regions && dest.regions.map(r => r.toLowerCase()).includes('kenya'));
          if (!isKenya) return false;
        } else if (region === 'africa') {
          // Matches Africa, East Africa, and Kenya
          const isAfrica = dest.region.toLowerCase() === 'africa' ||
                           (dest.regions && dest.regions.map(r => r.toLowerCase()).includes('africa'));
          if (!isAfrica) return false;
        } else if (region === 'east africa') {
          const isEastAfrica = dest.region.toLowerCase() === 'east africa' ||
                               (dest.regions && dest.regions.map(r => r.toLowerCase()).includes('east africa'));
          if (!isEastAfrica) return false;
        } else if (region === 'middle east') {
          const isME = dest.region.toLowerCase() === 'middle east' ||
                       (dest.regions && dest.regions.map(r => r.toLowerCase()).includes('middle east'));
          if (!isME) return false;
        } else if (region === 'australia and oceania') {
          const isOceania = dest.region.toLowerCase() === 'australia and oceania' ||
                            (dest.regions && dest.regions.map(r => r.toLowerCase()).includes('australia and oceania'));
          if (!isOceania) return false;
        } else {
          const matchesDirect = dest.region.toLowerCase() === region ||
                                (dest.regions && dest.regions.map(r => r.toLowerCase()).includes(region));
          if (!matchesDirect) return false;
        }
      }

      // 2. Category Filter Check
      if (category !== 'all') {
        const matchesCategory = dest.categories && dest.categories.some(
          (c) => c.toLowerCase() === category.toLowerCase()
        );
        if (!matchesCategory) return false;
      }

      // 3. Search Query Check
      if (query) {
        const nameMatch = dest.name && dest.name.toLowerCase().includes(query);
        const countryMatch = dest.country && dest.country.toLowerCase().includes(query);
        const regionMatch = dest.region && dest.region.toLowerCase().includes(query);
        const catMatch = dest.categories && dest.categories.some((c) => c.toLowerCase().includes(query));
        const actMatch = dest.activities && dest.activities.some((a) => a.toLowerCase().includes(query));
        const highlightMatch = dest.highlights && dest.highlights.some((h) => h.toLowerCase().includes(query));
        const descMatch = dest.shortDescription && dest.shortDescription.toLowerCase().includes(query);

        if (!nameMatch && !countryMatch && !regionMatch && !catMatch && !actMatch && !highlightMatch && !descMatch) {
          return false;
        }
      }

      return true;
    });
  }

  function applyFiltersAndRender() {
    const filtered = filterDestinations();
    const total = filtered.length;

    // Update active state in UI pills if loaded via URL params
    if (elements.regionPills) {
      elements.regionPills.forEach((p) => {
        const pRegion = (p.getAttribute('data-region') || '').toLowerCase();
        p.classList.toggle('active', pRegion === state.activeRegion);
      });
    }

    if (elements.categoryChips) {
      elements.categoryChips.forEach((c) => {
        const cCat = c.getAttribute('data-category') || 'all';
        c.classList.toggle('active', cCat === state.activeCategory);
      });
    }

    // Results count & clear filters visibility
    const isFiltered = state.activeRegion !== 'all' || state.activeCategory !== 'all' || state.searchQuery.trim().length > 0;
    if (elements.clearFiltersBtn) {
      elements.clearFiltersBtn.style.display = isFiltered ? 'inline-flex' : 'none';
    }

    // Calculate Pagination
    const totalPages = Math.ceil(total / state.perPage) || 1;
    if (state.currentPage > totalPages) {
      state.currentPage = totalPages;
    }

    const startIdx = (state.currentPage - 1) * state.perPage;
    const endIdx = Math.min(startIdx + state.perPage, total);
    const paginatedItems = filtered.slice(startIdx, endIdx);

    // Update Results Count Text
    if (elements.resultsCount) {
      if (total === 0) {
        elements.resultsCount.innerHTML = `No matching destinations found`;
      } else {
        elements.resultsCount.innerHTML = `Showing <strong>${startIdx + 1}–${endIdx}</strong> of <strong>${total}</strong> destinations`;
      }
    }

    // Render Cards
    renderCards(paginatedItems);

    // Render Pagination Controls
    renderPagination(totalPages);

    // Update or Sync Leaflet Map
    updateMapMarkers(filtered);

    // Sync URL query params
    syncUrlParams();
  }

  function renderCards(destinations) {
    if (!elements.grid) return;

    if (destinations.length === 0) {
      elements.grid.style.display = 'none';
      if (elements.noResults) {
        elements.noResults.classList.add('visible');
        const queryDisplay = elements.noResults.querySelector('.no-results-query');
        if (queryDisplay) {
          queryDisplay.textContent = state.searchQuery ? `"${state.searchQuery}"` : 'current filters';
        }
      }
      return;
    }

    elements.grid.style.display = 'grid';
    if (elements.noResults) {
      elements.noResults.classList.remove('visible');
    }

    elements.grid.innerHTML = destinations
      .map((dest) => {
        const hasLivePackage = dest.packageIds && dest.packageIds.length > 0;
        const categoriesHtml = (dest.categories || [])
          .slice(0, 2)
          .map((cat) => `<span class="dest-category-pill">${escapeHtml(cat)}</span>`)
          .join('');

        // Dedicated detail page URL
        const detailUrl = `${dest.slug}/`;

        return `
          <article class="dest-card" data-id="${escapeHtml(dest.id)}">
            <div class="dest-card-media">
              <img 
                src="${escapeHtml(dest.cardImage || dest.heroImage)}" 
                alt="${escapeHtml(dest.name)}" 
                class="dest-card-img" 
                loading="lazy"
                onerror="this.src='https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=800&q=80'"
              >
              <div class="dest-card-badges">
                <span class="dest-badge-region">${escapeHtml(dest.region)}</span>
                <span class="dest-badge-country">${escapeHtml(dest.country)}</span>
              </div>
            </div>
            <div class="dest-card-body">
              <div class="dest-card-categories">
                ${categoriesHtml}
              </div>
              <h3 class="dest-card-title">${escapeHtml(dest.name)}</h3>
              <p class="dest-card-desc">${escapeHtml(dest.shortDescription || dest.tagline || '')}</p>
              <div class="dest-card-footer">
                <a href="${detailUrl}" class="dest-btn-explore" aria-label="Explore ${escapeHtml(dest.name)}">
                  <span>Explore Destination</span>
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </a>
                ${hasLivePackage ? '<span class="dest-active-package-tag">Package Available</span>' : ''}
              </div>
            </div>
          </article>
        `;
      })
      .join('');
  }

  function renderPagination(totalPages) {
    if (!elements.pagination) return;

    if (totalPages <= 1) {
      elements.pagination.innerHTML = '';
      return;
    }

    let html = '';

    // Previous Button
    const prevDisabled = state.currentPage === 1 ? 'disabled' : '';
    html += `
      <button class="pagination-btn" ${prevDisabled} data-page="${state.currentPage - 1}" aria-label="Previous Page">
        &larr; Prev
      </button>
    `;

    // Page Numbers
    const cur = state.currentPage;
    for (let p = 1; p <= totalPages; p++) {
      if (p === 1 || p === totalPages || (p >= cur - 1 && p <= cur + 1)) {
        const activeClass = p === cur ? 'active' : '';
        html += `<button class="pagination-btn ${activeClass}" data-page="${p}">${p}</button>`;
      } else if (p === cur - 2 || p === cur + 2) {
        html += `<span class="pagination-ellipsis">&hellip;</span>`;
      }
    }

    // Next Button
    const nextDisabled = state.currentPage === totalPages ? 'disabled' : '';
    html += `
      <button class="pagination-btn" ${nextDisabled} data-page="${state.currentPage + 1}" aria-label="Next Page">
        Next &rarr;
      </button>
    `;

    elements.pagination.innerHTML = html;

    // Bind click events on buttons
    const btns = elements.pagination.querySelectorAll('.pagination-btn:not(:disabled)');
    btns.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        const page = parseInt(btn.getAttribute('data-page'), 10);
        if (page && page > 0 && page <= totalPages && page !== state.currentPage) {
          state.currentPage = page;
          applyFiltersAndRender();
          // Scroll back up to grid smoothly
          const anchor = document.getElementById('discoveryGridAnchor');
          if (anchor) {
            anchor.scrollIntoView({ behavior: scrollBehavior(), block: 'start' });
          }
        }
      });
    });
  }

  // --------------------------------------------------------------------------
  // LEAFLET INTERACTIVE DESTINATION MAP
  // --------------------------------------------------------------------------
  function toggleMapVisibility() {
    state.mapVisible = !state.mapVisible;
    if (elements.mapSection) {
      elements.mapSection.classList.toggle('visible', state.mapVisible);
    }
    if (elements.toggleMapBtn) {
      elements.toggleMapBtn.classList.toggle('active', state.mapVisible);
      elements.toggleMapBtn.innerHTML = state.mapVisible
        ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg> Hide Map`
        : `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon><line x1="8" y1="2" x2="8" y2="18"></line><line x1="16" y1="6" x2="16" y2="22"></line></svg> View on Map`;
    }

    if (state.mapVisible) {
      initOrRefreshLeafletMap();
    }
  }

  function initOrRefreshLeafletMap() {
    if (typeof L === 'undefined') {
      console.warn('Leaflet library is not available yet');
      return;
    }

    if (!state.leafletMap && elements.mapContainer) {
      try {
        state.leafletMap = L.map(elements.mapContainer, {
          center: [5.0, 30.0],
          zoom: 3,
          minZoom: 2,
          maxZoom: 16,
          scrollWheelZoom: false
        });

        // Add clean OpenStreetMap tiles
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
          maxZoom: 19
        }).addTo(state.leafletMap);

        state.markersLayer = L.featureGroup().addTo(state.leafletMap);
      } catch (err) {
        console.error('Failed to initialize Leaflet map', err);
      }
    }

    if (state.leafletMap) {
      setTimeout(() => {
        state.leafletMap.invalidateSize();
        const filtered = filterDestinations();
        updateMapMarkers(filtered);
      }, 200);
    }
  }

  function updateMapMarkers(destinations) {
    if (!state.leafletMap || !state.markersLayer || typeof L === 'undefined') return;

    state.markersLayer.clearLayers();

    const validDestinations = destinations.filter(
      (d) => d.coordinates && Array.isArray(d.coordinates) && d.coordinates.length === 2
    );

    if (validDestinations.length === 0) return;

    validDestinations.forEach((dest) => {
      const customIcon = L.divIcon({
        className: 'custom-dest-marker-wrapper',
        html: `
          <div class="custom-dest-marker" title="${escapeHtml(dest.name)}">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
            </svg>
          </div>
        `,
        iconSize: [28, 28],
        iconAnchor: [14, 28],
        popupAnchor: [0, -28]
      });

      const popupHtml = `
        <div class="map-popup-card">
          <img src="${escapeHtml(dest.cardImage || dest.heroImage)}" alt="${escapeHtml(dest.name)}" class="map-popup-img">
          <span class="map-popup-region">${escapeHtml(dest.region)} • ${escapeHtml(dest.country)}</span>
          <h4 class="map-popup-title">${escapeHtml(dest.name)}</h4>
          <a href="${dest.slug}/" class="map-popup-btn">Explore &rarr;</a>
        </div>
      `;

      const marker = L.marker(dest.coordinates, { icon: customIcon });
      marker.bindPopup(popupHtml, { maxWidth: 260 });
      state.markersLayer.addLayer(marker);
    });

    try {
      if (validDestinations.length > 0 && state.markersLayer.getBounds().isValid()) {
        state.leafletMap.fitBounds(state.markersLayer.getBounds(), {
          padding: [50, 50],
          maxZoom: 9
        });
      }
    } catch (e) {
      // Ignore fitting errors if bounds are tiny
    }
  }

  // Utility to escape HTML strings safely
  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Expose to window for inline triggers or external access
  window.destinationsApp = {
    state,
    resetAllFilters,
    applyFiltersAndRender
  };
})();
