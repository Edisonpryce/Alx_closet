
    document.querySelectorAll('.slider').forEach(function(slider, index) {
        const priceDisplay = document.querySelector(`#price-display-${index + 1}`);
        const sliderThumb = slider.parentElement.querySelector('.slider-thumb');

        slider.addEventListener('input', function() {
            priceDisplay.textContent = `$${this.value}`;
            sliderThumb.style.left = `${this.value / 20}%`; // Adjust left position based on value
        });

        slider.addEventListener('mousemove', function() {
            sliderThumb.style.left = `${this.value / 20}%`;
        });
    });
