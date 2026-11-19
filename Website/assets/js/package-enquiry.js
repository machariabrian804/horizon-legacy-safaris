(function () {
  'use strict';

  function init() {
    const form = document.getElementById('pkgEnquiryForm');
    if (!form) return;

    const dateInput = document.getElementById('pe-travelDate');
    if (dateInput) {
      const tomorrow = new Date();
      tomorrow.setDate(tomorrow.getDate() + 1);
      const minDate = tomorrow.toISOString().split('T')[0];
      dateInput.min = minDate;
      if (!dateInput.value) dateInput.value = minDate;
    }

    const btn = document.getElementById('pe-submitBtn');
    if (btn) {
      btn.addEventListener('click', function () {
        submit(form);
      });
    }
  }

  function val(id) {
    const el = document.getElementById(id);
    return el ? el.value.trim() : '';
  }

  function submit(form) {
    const fullName = val('pe-fullName');
    const phoneNumber = val('pe-phoneNumber');
    const emailAddress = val('pe-emailAddress');
    const travelDate = val('pe-travelDate');
    const transportPreference = val('pe-transportPreference');
    const adultsCount = val('pe-adultsCount');
    const childrenCount = val('pe-childrenCount');
    const specialRequests = val('pe-specialRequests');

    if (!fullName || !phoneNumber || !travelDate) {
      alert('Please fill in your name, phone number and preferred travel date.');
      return;
    }

    const packageName = form.getAttribute('data-package') || 'Safari Package';
    const waPhone = form.getAttribute('data-wa') || '254762251566';

    let message = '*NEW BOOKING INQUIRY - ' + packageName.toUpperCase() + '*\n\n';
    message += 'Client Name: ' + fullName + '\n';
    message += 'Phone/WhatsApp: ' + phoneNumber + '\n';
    if (emailAddress) message += 'Email: ' + emailAddress + '\n';
    message += 'Travel Date: ' + travelDate + '\n';
    message += 'Package: ' + packageName + '\n';
    message += 'Travel Style: ' + transportPreference + '\n';
    message += 'Guests: ' + adultsCount + ' adults | ' + childrenCount + ' children\n';
    if (specialRequests) message += 'Notes/Requests: ' + specialRequests + '\n';
    message += '\n_Sent via Horizon Legacy Safaris Website Inquiry Form_';

    const url = 'https://wa.me/' + waPhone + '?text=' + encodeURIComponent(message);
    window.open(url, '_blank');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();