$(document).ready(function() {
    $("button.carousel-previous").bind("click", () => moveCarousel("previous"));
    $("button.carousel-next").bind("click", () => moveCarousel("next"));
    _initCarousel();
});


function _initCarousel() {
    var carousel = $(".carousel");
    
    var firstImage = carousel.children(".carousel-slide").filter(":first");
    console.log(firstImage);
    firstImage.addClass("visible");
    carousel.css("height", firstImage.offsetHeight + "px");
    
    var otherImages = carousel.children(".carousel-slide").not(":first");
    otherImages.addClass("hidden");
};


function moveCarousel(direction) {
    var images = $(".carousel > .carousel-slide");
    var active = images.index(images.filter(".visible"));
    console.log(active);

    var nextImg;

    if (direction == "previous") {
        if (active == 0) return;
        
        var newActive = active - 1;
        console.log(newActive);
        nextImg = $(images.get(newActive));
    } 
    else if (direction == "next") {
        if (active + 1 == images.length) return;
        
        var newActive = active + 1;
        console.log(newActive);
        nextImg = $(images.get(newActive));
        console.log(nextImg)
    }
    else return;

    nextImg.addClass("visible");
    nextImg.removeClass("hidden");
    $(".carousel").css("height", nextImg.offsetHeight + "px");

    $(images.get(active)).addClass("hidden").removeClass("visible");
};

