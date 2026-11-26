$(document).ready(function() {
    $('.format-price').each(format);
});




function format() {
    var text = $(this).text();
    var limit = text.length - 3;
    var newText = text.substring(0, limit) + "." + text.substring(limit);
    $(this).text(newText);
};

