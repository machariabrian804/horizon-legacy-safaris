/**
 * HORIZON LEGACY - LUXURY SAFARIS & BESPOKE TRAVEL
 * Package Page Interactive Scripts
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initFaqAccordion();
  initStickyHeader();
  initDatePicker();
});

/* --------------------------------------------------------------------------
   1. MOBILE NAVIGATION TOGGLE
   -------------------------------------------------------------------------- */
function initMobileNav() {
  const toggleBtn = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');

  if (!toggleBtn || !navMenu) return;

  toggleBtn.addEventListener('click', () => {
    navMenu.classList.toggle('open');
    const isExpanded = navMenu.classList.contains('open');
    toggleBtn.setAttribute('aria-expanded', isExpanded);
  });

  // Close menu when a link is clicked
  const navLinks = navMenu.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('open');
    });
  });
}

/* --------------------------------------------------------------------------
   2. STICKY HEADER SCROLL SHADOW
   -------------------------------------------------------------------------- */
function initStickyHeader() {
  const header = document.getElementById('header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.08)';
    } else {
      header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.03)';
    }
  });
}

/* --------------------------------------------------------------------------
   3. PRICING & CURRENCY SWITCHER (Self-Drive vs Cruiser & KES vs USD)
   -------------------------------------------------------------------------- */
let currentPricingMode = 'self-drive';
let currentCurrency = 'kes';

function updateAllPrices() {
  const currencyLabels = document.querySelectorAll('.cell-currency, .cur');
  const currencySymbol = currentCurrency === 'usd' ? 'USD $' : 'Ksh';

  currencyLabels.forEach(el => {
    el.textContent = currencySymbol;
  });

  // Table and mobile cards
  const amountElements = document.querySelectorAll('[data-sd-kes]');
  amountElements.forEach(el => {
    let price = '';
    if (currentPricingMode === 'self-drive') {
      price = currentCurrency === 'usd' ? el.getAttribute('data-sd-usd') : el.getAttribute('data-sd-kes');
    } else {
      price = currentCurrency === 'usd' ? el.getAttribute('data-tr-usd') : el.getAttribute('data-tr-kes');
    }
    if (price) el.textContent = price;
  });

  // Hero section price highlight
  const heroAmount = document.querySelector('.hero-pricing-box .price-amount');
  const heroCurr = document.querySelector('.hero-pricing-box .price-currency');
  if (heroAmount && heroCurr) {
    if (currentCurrency === 'usd') {
      heroCurr.textContent = 'USD $';
      heroAmount.textContent = currentPricingMode === 'self-drive' ? '195' : '255';
    } else {
      heroCurr.textContent = 'Ksh';
      heroAmount.textContent = currentPricingMode === 'self-drive' ? '20,900' : '27,500';
    }
  }

  // Mobile sticky bar price
  const stickyPrice = document.querySelector('.mobile-sticky-inner .price-val strong');
  if (stickyPrice) {
    if (currentCurrency === 'usd') {
      stickyPrice.textContent = currentPricingMode === 'self-drive' ? 'USD $195' : 'USD $255';
    } else {
      stickyPrice.textContent = currentPricingMode === 'self-drive' ? 'Ksh 20,900' : 'Ksh 27,500';
    }
  }
}

function switchPricing(mode) {
  currentPricingMode = mode;
  const switcherBtns = document.querySelectorAll('.switcher-btn');
  const pricingNote = document.getElementById('pricingModeNote');

  switcherBtns.forEach(btn => {
    if (btn.getAttribute('data-pricing-mode') === mode) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  if (pricingNote) {
    if (mode === 'transport') {
      pricingNote.textContent = 'Includes roundtrip transport from Nairobi in a luxury 4x4 Safari Tour Cruiser + professional driver guide.';
    } else {
      pricingNote.textContent = 'Rates valid for self-drive guests arriving directly at the hotel.';
    }
  }

  // Pre-select transport mode in booking modal if opened later
  const transportSelect = document.getElementById('transportPreference');
  if (transportSelect) {
    transportSelect.value = mode === 'transport' ? '4x4 Safari Tour Cruiser' : 'Self Drive';
  }

  updateAllPrices();
}

function switchCurrency(curr) {
  currentCurrency = curr;
  const currBtns = document.querySelectorAll('.curr-btn');
  currBtns.forEach(btn => {
    if (btn.getAttribute('data-currency') === curr) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  updateAllPrices();
}

// Make accessible to inline onclick
window.switchPricing = switchPricing;
window.switchCurrency = switchCurrency;

/* --------------------------------------------------------------------------
   4. FAQ ACCORDION INTERACTIVITY
   -------------------------------------------------------------------------- */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    if (!questionBtn) return;

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all other items for clean accordion UX
      faqItems.forEach(otherItem => {
        if (otherItem !== item) {
          otherItem.classList.remove('active');
          const otherBtn = otherItem.querySelector('.faq-question');
          if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
        }
      });

      // Toggle current item
      if (isActive) {
        item.classList.remove('active');
        questionBtn.setAttribute('aria-expanded', 'false');
      } else {
        item.classList.add('active');
        questionBtn.setAttribute('aria-expanded', 'true');
      }
    });
  });
}

/* --------------------------------------------------------------------------
   5. BOOKING MODAL LOGIC
   -------------------------------------------------------------------------- */
function openBookingModal(preselectedRoom = '') {
  const modal = document.getElementById('bookingModal');
  if (!modal) return;

  if (preselectedRoom) {
    const roomSelect = document.getElementById('roomCategory');
    if (roomSelect) {
      // Find matching option or closest match
      for (let i = 0; i < roomSelect.options.length; i++) {
        if (roomSelect.options[i].value.toLowerCase().includes(preselectedRoom.toLowerCase()) ||
            preselectedRoom.toLowerCase().includes(roomSelect.options[i].value.toLowerCase())) {
          roomSelect.selectedIndex = i;
          break;
        }
      }
    }
  }

  modal.classList.add('open');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden'; // Prevent background scrolling
}

function closeBookingModal() {
  const modal = document.getElementById('bookingModal');
  if (!modal) return;

  modal.classList.remove('open');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}

// Make accessible to inline onclick
window.openBookingModal = openBookingModal;
window.closeBookingModal = closeBookingModal;

// Close on backdrop click
document.addEventListener('click', (e) => {
  const modal = document.getElementById('bookingModal');
  if (modal && e.target === modal) {
    closeBookingModal();
  }
});

// Close on Escape key press
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeBookingModal();
    closeLightbox();
  }
});

/* --------------------------------------------------------------------------
   6. IMAGE LIGHTBOX MODAL
   -------------------------------------------------------------------------- */
function openLightbox(triggerElement) {
  const modal = document.getElementById('imageLightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCaption = document.getElementById('lightboxCaption');
  if (!modal || !lightboxImg) return;

  const img = triggerElement.tagName === 'IMG' ? triggerElement : triggerElement.querySelector('img');
  if (!img) return;

  lightboxImg.src = img.src;
  lightboxImg.alt = img.alt || 'Enlarged photo';

  const captionElement = triggerElement.querySelector('.image-caption span, span');
  const captionText = captionElement ? captionElement.textContent.replace('(Click to enlarge)', '').trim() : img.alt;
  if (lightboxCaption) {
    lightboxCaption.textContent = captionText || 'The Encore Hotel Nakuru Getaway';
  }

  modal.classList.add('open');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}

function closeLightbox(event) {
  if (event && event.target && event.target.tagName === 'IMG') return;
  const modal = document.getElementById('imageLightbox');
  if (!modal) return;
  modal.classList.remove('open');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}

window.openLightbox = openLightbox;
window.closeLightbox = closeLightbox;

/* --------------------------------------------------------------------------
   6. TRAVEL DATE PICKER DEFAULT
   -------------------------------------------------------------------------- */
function initDatePicker() {
  const dateInput = document.getElementById('travelDate');
  if (!dateInput) return;

  // Set min date to tomorrow
  const tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1);
  const minDate = tomorrow.toISOString().split('T')[0];
  dateInput.min = minDate;
  dateInput.value = minDate;
}

/* --------------------------------------------------------------------------
   7. FORM SUBMIT & INSTANT WHATSAPP INQUIRY GENERATOR
   -------------------------------------------------------------------------- */
function handleBookingSubmit(event) {
  event.preventDefault();

  const fullName = document.getElementById('fullName').value.trim();
  const phoneNumber = document.getElementById('phoneNumber').value.trim();
  const emailAddress = document.getElementById('emailAddress').value.trim();
  const travelDate = document.getElementById('travelDate').value;
  const roomCategory = document.getElementById('roomCategory').value;
  const transportPreference = document.getElementById('transportPreference').value;
  const adultsCount = document.getElementById('adultsCount').value;
  const childrenCount = document.getElementById('childrenCount').value;
  const specialRequests = document.getElementById('specialRequests').value.trim();

  // Create formatted WhatsApp inquiry message
  let message = `*NEW BOOKING INQUIRY - THE ENCORE HOTEL NAKURU (2D1N)*\n\n`;
  message += `👤 *Client Name:* ${fullName}\n`;
  message += `📞 *Phone/WhatsApp:* ${phoneNumber}\n`;
  if (emailAddress) message += `📧 *Email:* ${emailAddress}\n`;
  message += `📅 *Travel Date:* ${travelDate}\n`;
  message += `🏨 *Room Selected:* ${roomCategory}\n`;
  message += `🚗 *Transport:* ${transportPreference}\n`;
  message += `👥 *Guests:* ${adultsCount} adults | ${childrenCount} children\n`;
  if (specialRequests) {
    message += `📝 *Notes/Requests:* ${specialRequests}\n`;
  }
  message += `\n_Sent via Horizon Legacy Safaris Website Inquiry Form_`;

  const whatsappPhone = '254712345678';
  const whatsappUrl = `https://wa.me/${whatsappPhone}?text=${encodeURIComponent(message)}`;

  // Close modal and redirect to WhatsApp
  closeBookingModal();
  window.open(whatsappUrl, '_blank');
}

window.handleBookingSubmit = handleBookingSubmit;
