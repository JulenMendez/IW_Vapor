$(document).ready(function() {
    console.log("Price-formater");
    $('.format-price').each(format2);
});



// function format() {
//     var text = $(this).text();
//     var price = parseInt(text.substring(text.length -  1)) / 100;
//     $(this).text(price + "€");
// };


function format2() {
    var text = $(this).text();
    console.log(text);
    var text_obj = new String(text);
    var limit = text_obj.lenght - 3;
    console.log(text_obj.lenght);
    console.log(limit);
    var newText = text_obj.substring(0, limit) + "." + text_obj.substring(limit);
    $(this).text(newText);
};



// function() {
//         var text = $(this).text();
//         console.log(text)
//         var newText = text.substring(0, text.lenght - 3) + "." + text.substring(text.lenght - 3, text.lenght);
//         $(this).text(newText);