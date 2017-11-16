$(document).ready(function() {
	$('#email').completer({
	  source: [
	    'gmail.com',
	    'yahoo.com',
	    'hotmail.com',
	  ],
	  separator: '@'
	});

	$('#submit').click(function(event) {
		/* Act on the event */
		$('.message').css('display','block').toggleClass('animated bounce');
	});
});