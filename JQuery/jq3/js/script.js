/*
$(document).ready(function() {
    $('button').click(function() {
        $('.box:odd').hide();
    });
});*/

$('document').ready(function() {
    $('button').click(function() {
        $('.box:odd').html("<h2>html injectie vanuit javascript</h2>");
    })
})