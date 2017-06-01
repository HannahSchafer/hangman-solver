$(document).ready(function(){


function playGame(event) {
    $.get("/play-game", function(results) {
                        var word = results.word;
                        var msg = results.msg;
                        $('#word-spot').html('word:' + ' '+ word);
                        $('#msg').html(msg);
    
    });  
    event.preventDefault();
}




// event listener - calls ajax request 
$('#button').on('click', playGame);




});