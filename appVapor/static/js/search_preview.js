$(document).ready(function() {
    $('#search').bind("input", function() {
        if (document.getElementById('search').value == "") {
            $('.search-preview').remove();
        } else {
            $.ajax({
                type: "GET",
                async: true,
                url: "ajax/search-preview",
                data: {name: document.getElementById('search').value},
                success: successFunc
            });

        }
    });
});



function successFunc(data, textStatus) {
    $('.search-preview').remove();
    $('.search-container').append(data)
}