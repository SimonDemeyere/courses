/*$('document').ready(function() {
    $('button').click(function() {
        $('.box:first').append("<h1>Aanvulling box 1</h1>");
        $('.box:last').after("<p>After laatste box</p>");
        $('.box').before("<h2>Before everywhere</h2>").css({"background":"yellow","border":"1px solid green"}).addClass('color').removeClass('color');
        $('button').toggleClass('color');
    });
});*/

$('document').ready(function() {
    $('button').click(function() {
        $('.box').addClass('color');
    });
});
