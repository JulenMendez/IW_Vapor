$(document).ready(function() {
    $('#search').bind("input", function() {
        // let text = $(this).value;
        if (document.getElementById('search').value == "") {
            //No mostramos nada
            $('.search-preview').remove();
        } else {
            //Llamada ajax
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