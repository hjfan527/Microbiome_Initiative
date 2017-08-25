$('.carousel.carousel-slider').carousel({ fullWidth: true });

function autoplay() {
    $('.carousel').carousel('next');
    setTimeout(autoplay, 4500);
}

$(function() {
    autoplay();
})
