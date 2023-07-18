$(function(){
   	
   	'use strict';

    // slider
    $("#slider-home").owlCarousel({

        navigation: true,
        slideSpeed: 300,
        paginationSpeed: 400,
        singleItem: true,
        dots: true
    });

    // SMOOTH SCROLL
    $("a").on('click', function(event) {

      if (this.hash !== "") {
        event.preventDefault();

        var hash = this.hash;

        $('html, body').animate({

          scrollTop: $(hash).offset().top

        }, 850, function(){

          window.location.hash = hash;

        });

      }

    });

    // NAVBAR COLLAPSE HIDE ON CLICK
    $('.nav a').click(function(){
        $('.navbar-collapse').collapse('hide');
    });

    // menu filter container
    $('.filtr-container').filterizr();

    // menu filter
    $('.simplefilter li').click(function() {
        $('.simplefilter li').removeClass('active');
        $(this).addClass('active');
    });

    // MENU IMAGE POPUP
    $('.image-popup').magnificPopup({
    
        type: 'image',
        removalDelay: 300,
        mainClass: 'mfp-fade'
        
    });

    // NAVBAR ON SCROLL
    $(window).scroll(function() {
      
      if ($(document).scrollTop() > 50) { 
        $(".navbar-fixed-top").css({"background-color": "#222985", "box-shadow": "0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2)", "transition": ".5s ease-out"});
      } else { 
        $(".navbar-fixed-top").css({"background-color": "transparent", "box-shadow": "none"});
      }

    });

    // TESTIMONIALS
    $("#owl-testimonial").owlCarousel({

      items: 1,
      slideSpeed: 350,
      itemsMobile : [640,1],
      singleItem: true,
      dots: false
    });
    
     // loader
    $('#fakeLoader').fakeLoader({
      
      zIndex: 999,
      spinner: "spinner5",
      bgColor: "#222985"

    });
});

//Footer btn

document.getElementById('contact-btn').addEventListener('click', function(){
  window.location.href = "/" + "#contact-us";
})