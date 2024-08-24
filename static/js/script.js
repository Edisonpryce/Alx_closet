// The Currency slider functionality (not working for now)
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
