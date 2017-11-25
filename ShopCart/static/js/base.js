$(document).ready(function() {

	$('#login_submit').click(function(event) {
		/* Act on the event */
		event.preventDefault();
		$('#signinBox').fadeOut(200);
		$('#loginbox').fadeIn(200);
	});

	$('.loginbox-close').click(function(event) {
		/* Act on the event */
		event.preventDefault();
		$('#loginbox').fadeOut(200);
	});

//-------------------------------------------------

	$('#signin').click(function(event) {
		/* Act on the event */
		event.preventDefault();
		$('#signinBox').fadeIn(200);
		$('#loginbox').fadeOut(200);

		$('#signinbox_email').completer({
		  source: [
		    'gmail.com',
		    'yahoo.com',
		    'hotmail.com',
		  ],
		  separator: '@'
		});
	});

	$(window).scroll(function(){
	    $(".completer-container").css("position","fixed", "top","43%","left","42%");
	});

	$('.signinBox-close').click(function(event) {
		/* Act on the event */
		event.preventDefault();
		$('#signinBox').fadeOut(200);
	});

//______________Ajax-Account_check______________

	$('#signinbox_account').on('change',function(event) {
		/* Act on the event */
		var current_account = $('input:text').val();
		console.log(current_account);
		$.ajax({
			type: 'GET',
			url: '/account_ckeck/',
			data: {'current_account': current_account },
			success: function (status) {
				console.log(status);
				if (status == 'ok'){
					$('.account_not_ok_img').hide();
					$('#account_illegal').hide();
					$('#account_duplicate').hide();
					$('.account_ok_img').show();
					$('#account_ok').show();
				}
				else if (status == 'illegal') {
					$('.account_ok_img').hide();
					$('#account_ok').hide();
					$('#account_duplicate').hide();
					$('.account_not_ok_img').show();
					$('#account_illegal').show();
				}
				else if (status == 'duplicate'){
					$('.account_ok_img').hide();
					$('#account_ok').hide();
					$('#account_illegal').hide();
					$('.account_not_ok_img').show();
					$('#account_duplicate').show();
				}
				else {
				}
			}
		});
	});

//_______________Ajax-Email_check________________


	$('#signinbox_email').on('change',function(event) {

			var current_email = $('input[type="email"]').val();
			console.log(current_email);
			$.ajax({
				type: 'GET',
				url: '/email_ckeck/',
				data: {'current_email': current_email },
				success: function (status) {
					console.log(status);
					if (status == 'ok'){
						$('.email_not_ok_img').hide();
						$('#email_illegal').hide();
						$('.email_ok_img').show();
						$('#email_ok').show();
					}
					else {
						$('.email_ok_img').hide();
						$('#email_ok').hide();
						$('.email_not_ok_img').show();
						$('#email_illegal').show();
					}
				}
			});
		});

//_____________Ajax_password_check____________

	$('#check_password').on('blur',function(event) {

			var first_password = $('input[id="password"]').val();
			var second_password = $('input[id="check_password"]').val();
			console.log(second_password);

			if ( first_password !== '' && (first_password == second_password) ) {
				$('.password_not_ok_img').hide();
				$('#password_not_ok').hide();
				$('.password_ok_img').show();
				$('#password_ok').show();
			}
			else {
				$('.password_ok_img').hide();
				$('#password_ok').hide();
				$('.password_not_ok_img').show();
				$('#password_not_ok').show();
			}
		});

	$('#password').on('blur',function(event) {

			var first_password = $('input[id="password"]').val();
			var second_password = $('input[id="check_password"]').val();
			console.log(second_password);

			if ( first_password !== '' && (first_password == second_password) ) {
				$('.password_not_ok_img').hide();
				$('#password_not_ok').hide();
				$('.password_ok_img').show();
				$('#password_ok').show();
			}
			else {
				$('.password_ok_img').hide();
				$('#password_ok').hide();
				$('.password_not_ok_img').show();
				$('#password_not_ok').show();
			}
		});


});
