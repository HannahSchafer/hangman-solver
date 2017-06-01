$(document).ready(function(){


function playGame(event) {
    $.get("/play-game", function(results) {
                        var gameId = results.gameId;
                        var word = results.word;
                        var guessesLeft = results.guessesLeft;
                        var msg = results.msg;
                        $('#word-spot').html('word:' + ' '+ word);
                        // $('#guesses-left').html(guessesLeft);
                        $('#msg').html(msg);
    
    });  
    event.preventDefault();
}




// event listener - calls ajax request 
$('#button').on('click', playGame);




});