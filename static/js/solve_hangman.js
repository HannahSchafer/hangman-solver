$(document).ready(function(){


function startGame(event) {
    var email = "schafer.hannah@gmail.com";
    $.post("http://int-sys.usr.space/hangman/games", {'email':email}, 
                                function(results) {
                                var gameId = results.gameId;
                                var word = results.word;
                                var guessesLeft = results.guessesLeft;
                                $('#word-spot').html(word);
                                $('#guesses-left').html(guessesLeft);
    
    }); 
    event.preventDefault(); 
}




function checkStatus(event) {
    $.get("http://int-sys.usr.space/hangman/games/{gameId}", {"gameID" : game_ID}, 
                                function(results) {
                                var gameID = results.gameId;
                                var word = results.word;
                                var guessesLeft = results.guessesLeft;
                                var active = results.active;
                                $('#word-spot').html(word);
                                $('#guesses-left').html(guessesLeft);
                                $('#active').html(active);

    
    });  
    event.preventDefault();
}


function playGame(event) {
    $.post("http://int-sys.usr.space/hangman/games/{gameId}/guesses", 
                                {"gameId" : gameID, "char" : letter}, 
                                function(results) {
                                var gameID = results.gameId;
                                var word = results.word;
                                var guessesLeft = results.guessesLeft;
                                var active = results.active;
                                var msg = results.msg;
                                $('#word-spot').html(word);
                                $('#guesses-left').html(guessesLeft);
                                $('#msg').html(msg);
    
    });  
    event.preventDefault();
}


// event listener - calls ajax request 
$('#submit-btn').on('click', startGame);












});