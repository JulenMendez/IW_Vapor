$(document).ready(function() {
    $('.desc-tooltip').each(function() {
        var uri = "qtip/game-desc/" +  $(this).children("a").attr("href").substring(8);
        $(this).qtip({
                content: {
                    method: "get",
                    url: uri
                }
            });
    });
});