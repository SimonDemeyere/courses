$('document').ready(function() {
    $('button').click(function() {
        $('.box:odd').html("<h2>Deze tekst komt van Jacascript-JQuery</h2>");
    });
});

$('document').ready(function() {
    $('button').click(function() {
        $('.box:first').css("color", "red").css("border", "2px solid red").hide(5000);
    });
});
