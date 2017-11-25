$(document).ready(function() {

//_____________Product-effect______________

	for (var i = 1; i < 30; i++) {
		$('.food'+ i).mouseenter(function(event) {
			/* Act on the event */
			$(this).addClass('animated infinite pulse');
		});

		$('.food'+ i).mouseleave(function(event) {
			/* Act on the event */
			$(this).removeClass('animated infinite pulse');
		});
	}


	$('.menu_list').mouseenter(function(event) {
		/* Act on the event */
		$(this).addClass('animated infinite shake');
	});

	$('.menu_list').mouseleave(function(event) {
		/* Act on the event */
		$(this).removeClass('animated infinite shake');
	});


	$('#original_cartlogo').mouseenter(function(event) {
		/* Act on the event */
		$(this).addClass('animated infinite bounce');
	});

	$('#original_cartlogo').mouseleave(function(event) {
		/* Act on the event */
		$(this).removeClass('animated infinite bounce');
	});

	$('#after_cartlogo').mouseenter(function(event) {
		/* Act on the event */
		$(this).addClass('animated infinite bounce');
	});

	$('#after_cartlogo').mouseleave(function(event) {
		/* Act on the event */
		$(this).removeClass('animated infinite bounce');
	});
	

});