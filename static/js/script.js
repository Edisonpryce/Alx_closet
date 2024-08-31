// Currency slider functionality
document.querySelectorAll('.currency-slider').forEach(function(sliderWrapper) {
    const thumb = sliderWrapper.querySelector('.slider-thumb');
    const slider = sliderWrapper.querySelector('.slider');

    slider.addEventListener('input', function() {
        const value = this.value;
        const max = this.max;
        const percentage = (value / max) * 100;
        thumb.style.left = `calc(${percentage}% + (${8 - percentage * 0.15}px))`;
    });
});

// Handle compare button clicks for color switching
document.querySelectorAll('.compare-btn').forEach(button => {
    button.addEventListener('click', function() {
        const product = this.closest('.product');
        const colors = JSON.parse(product.getAttribute('data-colors'));

        let currentColor = product.getAttribute('data-current-color') || Object.keys(colors)[0];
        let nextColor = Object.keys(colors).find(color => color !== currentColor) || currentColor;

        product.querySelector('img').src = colors[nextColor];
        product.setAttribute('data-current-color', nextColor);
    });
});

// Example of handling other action buttons if necessary
document.querySelectorAll('.action-btn:not(.compare-btn)').forEach(button => {
    button.addEventListener('click', function() {
        alert('Button clicked: ' + this.getAttribute('aria-label'));
    });
});



//extras
'use strict';



/**
 * add event on element
 */

const addEventOnElem = function (elem, type, callback) {
  if (elem.length > 1) {
    for (let i = 0; i < elem.length; i++) {
      elem[i].addEventListener(type, callback);
    }
  } else {
    elem.addEventListener(type, callback);
  }
}



/**
 * navbar toggle
 */

const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const navbar = document.querySelector("[data-navbar]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function () {
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
}

addEventOnElem(navTogglers, "click", toggleNavbar);

const closeNavbar = function () {
  navbar.classList.remove("active");
  overlay.classList.remove("active");
}

addEventOnElem(navbarLinks, "click", closeNavbar);



/**
 * header sticky & back top btn active
 */

const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const headerActive = function () {
  if (window.scrollY > 150) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
}

addEventOnElem(window, "scroll", headerActive);

let lastScrolledPos = 0;

const headerSticky = function () {
  if (lastScrolledPos >= window.scrollY) {
    header.classList.remove("header-hide");
  } else {
    header.classList.add("header-hide");
  }

  lastScrolledPos = window.scrollY;
}

addEventOnElem(window, "scroll", headerSticky);



/**
 * scroll reveal effect
 */

const sections = document.querySelectorAll("[data-section]");

const scrollReveal = function () {
  for (let i = 0; i < sections.length; i++) {
    if (sections[i].getBoundingClientRect().top < window.innerHeight / 2) {
      sections[i].classList.add("active");
    }
  }
}

scrollReveal();

addEventOnElem(window, "scroll", scrollReveal);


document.addEventListener('DOMContentLoaded', function () {
  const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
  const cartCountElement = document.getElementById('cart-count');
  const modal = document.getElementById('impact-modal');
  const closeModalButton = document.querySelector('.modal .close');
  const impactMessage = document.getElementById('impact-message');
  const addToCartModalButton = document.getElementById('add-to-cart-btn');
  const cancelModalButton = document.getElementById('cancel-btn');
  let cartCount = 0;

  addToCartButtons.forEach((button, index) => {
      button.addEventListener('click', function() {
          const priceSlider = document.getElementById(`price-slider-${index + 1}`);
          const selectedPrice = parseInt(priceSlider.value, 10);

          if (selectedPrice > 100) {
              impactMessage.innerHTML = `Woooow $${selectedPrice} 😱 Through your purchase this is going to help us support others💗💗`;
          } else {
              impactMessage.innerHTML = `Thank you for your purchase of $${selectedPrice}!`;
          }

          modal.style.display = "block";

          addToCartModalButton.onclick = function() {
              cartCount++;
              cartCountElement.textContent = cartCount;
              modal.style.display = "none";
          };
      });
  });

  closeModalButton.addEventListener('click', function() {
      modal.style.display = "none";
  });

  cancelModalButton.addEventListener('click', function() {
      modal.style.display = "none";
  });

  window.addEventListener('click', function(event) {
      if (event.target === modal) {
          modal.style.display = "none";
      }
  });
});

