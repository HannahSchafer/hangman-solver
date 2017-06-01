$(document).ready(function(){


function playGame(event) {
    $.get("/play-game", function(results) {
                        var gameId = results.gameId;
                        var word = results.word;
                        var guessesLeft = results.guessesLeft;
                        var msg = results.msg;
                        $('#word-spot').html(word);
                        // $('#guesses-left').html(guessesLeft);
                        $('#msg').html(msg);
    
    });  
    event.preventDefault();
}



// function showQuote(event) {
    
//     $.post("/inspire-process.json", function(results) {
//                                         var quote_content = results.quote;
//                                         typeQuote(quote_content);
//                                         $("#loader").hide();
//                                         $("#give").hide();
//                                         $("#tweet-container").hide();
//                                         $("#fillgauge").hide();

                                       
                            
//     });
// }




// event listener - calls ajax request 
$('#submit-btn').on('click', playGame);

});