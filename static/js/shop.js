document.querySelectorAll('.slider').forEach(function (slider, index) {
    const priceDisplay = document.querySelector(`#price-display-${index + 1}`);

    slider.addEventListener('input', function () {
        priceDisplay.textContent = `$${this.value}`;
    });
});


document.addEventListener('DOMContentLoaded', function () {
  const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
  const cartCountElement = document.getElementById('cart-count');
  const modal = document.getElementById('impact-modal');
  const closeModalButton = document.querySelector('.modal .close');
  const impactMessage = document.getElementById('impact-message');
  const addToCartModalButton = document.getElementById('add-to-cart-btn');
  const cancelModalButton = document.getElementById('cancel-btn');
  let cartCount = 0;




document.addEventListener('DOMContentLoaded', function () {
    const viewProductButtons = document.querySelectorAll('.compare-btn');

    viewProductButtons.forEach(button => {
        button.addEventListener('click', function () {
            const productUrl = this.getAttribute('data-url');
            window.location.href = productUrl;
        });
    });


});


document.addEventListener('DOMContentLoaded', function() {
    const carouselInner = document.querySelector('.carousel-inner');
    const carouselItems = document.querySelectorAll('.carousel-item');
    const prevButton = document.querySelector('.carousel-control-prev');
    const nextButton = document.querySelector('.carousel-control-next');
    let currentIndex = 0;

    function updateCarousel() {
        // Calculate the translateX value for the carousel inner
        const translateX = -currentIndex * 100;
        carouselInner.style.transform = `translateX(${translateX}%)`;
    }

    function showNextSlide() {
        currentIndex = (currentIndex + 1) % carouselItems.length; // Loop back to the first slide
        updateCarousel();
    }

    function showPrevSlide() {
        currentIndex = (currentIndex - 1 + carouselItems.length) % carouselItems.length; // Loop to the last slide
        updateCarousel();
    }

    nextButton.addEventListener('click', showNextSlide);
    prevButton.addEventListener('click', showPrevSlide);

    // Optionally, you can also add auto-slide functionality
    setInterval(showNextSlide, 5000); // Slide every 5 seconds
});

