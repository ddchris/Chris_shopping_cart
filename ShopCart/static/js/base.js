$(document).ready(function() {

	var signin_account_is_ok = 'false';
	var signin_email_is_ok = 'false';
	var signin_password_is_ok = 'false';
	var el_submit = document.querySelector('#signinbox_submit');
	// 送出註冊資料 element


	var el_loginbox_open = document.querySelector('#loginbox_open');
	var el_signinbox_open = document.querySelector('#signinbox_open');
	var el_signinBox_close = document.querySelector('#signinBox_close');
	var el_loginbox_close = document.querySelector('#loginbox_close');

	el_loginbox_open.addEventListener('click', function(event) {
		/* Act on the event */
		event.preventDefault();
		$('#signinBox').fadeOut(200);
		$('#loginbox').fadeIn(200);
	}, false)

	el_loginbox_close.addEventListener('click', function(event) {
		/* Act on the event */
		event.preventDefault();
		$('#loginbox').fadeOut(200);
	}, false)

	el_signinbox_open.addEventListener('click', function(event) {

		event.preventDefault();
		$('#loginbox').fadeOut(200);
		$('#signinBox').fadeIn(200);

		$('#signinbox_email').completer({
		  source: [
		    'gmail.com',
		    'yahoo.com',
		    'hotmail.com',
		  ],
		  separator: '@'
		});

	}, false)

	$(window).scroll(function(){
		    $(".completer-container").css("position","fixed", "top","43%","left","42%");
		});

	el_signinBox_close.addEventListener('click', function(event) {
		/* Act on the event */
		event.preventDefault();
		$('#signinBox').fadeOut(200);
	}, false)

//______________Ajax-Account_check______________

	$('#signinbox_account').on('keyup',function(event) {
		/* Act on the event */
		var current_account = $('input:text').val();
		$.ajax({
			type: 'GET',
			url: '/account_ckeck/',
			data: {'current_account': current_account },
			success: function (status) {
				if (status == 'ok'){
					$('.account_not_ok_img').hide();
					$('#account_illegal').hide();
					$('#account_duplicate').hide();
					$('.account_ok_img').show();
					$('#account_ok').show();
					signin_account_is_ok = 'true';
				}
				else if (status == 'illegal') {
					$('.account_ok_img').hide();
					$('#account_ok').hide();
					$('#account_duplicate').hide();
					$('.account_not_ok_img').show();
					$('#account_illegal').show();
					signin_account_is_ok = 'false';
					console.log('illegal')
				}
				else if (status == 'duplicate'){
					$('.account_ok_img').hide();
					$('#account_ok').hide();
					$('#account_illegal').hide();
					$('.account_not_ok_img').show();
					$('#account_duplicate').show();
					signin_account_is_ok = 'false';
					console.log('duplicate')
				}
				else {
				}
			}
		});
	});

//_______________Ajax-Email_check________________

	var el_signinbox_email = document.querySelector('#signinbox_email');
	el_signinbox_email.addEventListener('blur', function (e) {
		var current_email = e.target.value;
		$.ajax({
			type: 'GET',
			url: '/email_ckeck/',
			data: {'current_email': current_email },
			success: function (status) {
				if (status == 'ok'){
					$('.email_not_ok_img').hide();
					$('#email_illegal').hide();
					$('.email_ok_img').show();
					$('#email_ok').show();
					signin_email_is_ok = 'true';
				}
				else {
					$('.email_ok_img').hide();
					$('#email_ok').hide();
					$('.email_not_ok_img').show();
					$('#email_illegal').show();
					signin_email_is_ok = 'false';
				}
			}
		});
	}, false);

//_____________Password_check____________

	var el_signin_password = document.getElementById('signin_password');
	var el_check_password = document.getElementById('check_password');

	el_signin_password.addEventListener('keyup', function(e){
		var first_password = el_signin_password.value;
		var second_password = el_check_password.value;
		if ( first_password !== '' && (first_password == second_password) )
			{
				$('.password_not_ok_img').hide();
				$('#password_not_ok').hide();
				$('.password_ok_img').show();
				$('#password_ok').show();
				signin_password_is_ok = 'true';
			}
			else {
				$('.password_ok_img').hide();
				$('#password_ok').hide();
				$('.password_not_ok_img').show();
				$('#password_not_ok').show();
				signin_password_is_ok = 'false';
			}
		}	
	, false);

	el_check_password.addEventListener('keyup', function(e) {
		var first_password = el_signin_password.value;
		var second_password = el_check_password.value;
		if ( first_password !== '' && (first_password == second_password) ) 
			{
				$('.password_not_ok_img').hide();
				$('#password_not_ok').hide();
				$('.password_ok_img').show();
				$('#password_ok').show();
				signin_password_is_ok = 'true';
			}
		else {
				$('.password_ok_img').hide();
				$('#password_ok').hide();
				$('.password_not_ok_img').show();
				$('#password_not_ok').show();
				signin_password_is_ok = 'false';
		}
	}
	, false);

//______________ signform 格式錯誤禁止送出資料 _________________________

	el_submit.addEventListener('click', function (e) {
		if ( signin_account_is_ok != 'true' || signin_email_is_ok  != 'true' 
			|| signin_password_is_ok != 'true')
		{	console.log('not to be sent')
			e.preventDefault();    //取消默認事件
		}
		else{
			e.returnValue = true;  //恢復默認事件
		}
	}, false);

});











