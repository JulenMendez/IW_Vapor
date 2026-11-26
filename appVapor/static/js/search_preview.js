$(document).ready(function() {
    $('#search').bind("input", function() {
        if ($(this).val() == "") {
            $('.search-preview').remove();
        } else {
            $.ajax({
                type: "GET",
                async: true,
                url: "ajax/search-preview",
                data: {name: $(this).val()},
                success: successFunc
            });

        }
    });
});



function successFunc(data, textStatus) {
    $('.search-preview').remove();
    $('.search-container').append(data);
    $('.search-preview .format-price').each(formatPrice);
}