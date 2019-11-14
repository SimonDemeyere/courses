

$('button').click(function(e) {
    e.preventDefault();
    let value = $('#todo-list-item').val();
    console.log(value);
    $('#list-items').append("<li><input class='clickbox' name='check' type='checkbox'>" + value + '<img src="img/clear.svg"></li>');
});


$(document).on("change",".clickbox", function() {
    $('.clickbox').click(function(e) {
    })
});

$('document');