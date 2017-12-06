$(document).ready(function() {

//_____________Product-effect______________

	var prod_number = 50;

	for (var i = 1; i <  prod_number; i++) {
		$('.food'+ i).mouseenter(function(event) {
			$(this).addClass('animated infinite pulse');
		});

		$('.food'+ i).mouseleave(function(event) {
			$(this).removeClass('animated infinite pulse');
		});
	}


	var el_foods = document.querySelector('.content.food')
	var el_stationeries = document.querySelector('.content.stationery')
	var el_computers = document.querySelector('.content.computer')
	var el_necessities = document.querySelector('.content.necessity')

	$('.menu_list.stationery').mouseenter(function(event) {
		$('.content.food').css('display', 'none');
		$('.content.computer').css('display', 'none');
		$('.content.necessity').css('display', 'none');		
		$('.content.stationery').css('display', 'block');
		$(this).addClass('animated infinite shake');
	});

	$('.menu_list.necessity').mouseenter(function(event) {
		$('.content.computer').css('display', 'none');
		$('.content.food').css('display', 'none');
		$('.content.stationery').css('display', 'none'); 
		$('.content.necessity').css('display', 'block');
		$(this).addClass('animated infinite shake');
	});

	$('.menu_list.food').mouseenter(function(event) {
		$('.content.computer').css('display', 'none');
		$('.content.necessity').css('display', 'none');
		$('.content.stationery').css('display', 'none'); 
		$('.content.food').css('display', 'block');
		$(this).addClass('animated infinite shake');
	});

	$('.menu_list.computer').mouseenter(function(event) {
		$('.content.food').css('display', 'none');
		$('.content.necessity').css('display', 'none');
		$('.content.stationery').css('display', 'none'); 
		$('.content.computer').css('display', 'block');
		$(this).addClass('animated infinite shake');
	});




	$('.menu_list.stationery').mouseleave(function(event) {
		$(this).removeClass('animated infinite shake');
	});


	$('.menu_list.food').mouseleave(function(event) {
		$(this).removeClass('animated infinite shake');
	});

	$('.menu_list.computer').mouseleave(function(event) {
		$(this).removeClass('animated infinite shake');
	});

	$('.menu_list.necessity').mouseleave(function(event) {
		$(this).removeClass('animated infinite shake');
	});






	$('#original_cartlogo').mouseenter(function(event) {
		$(this).addClass('animated infinite bounce');
	});

	$('#original_cartlogo').mouseleave(function(event) {
		$(this).removeClass('animated infinite bounce');
	});

	$('#after_cartlogo').mouseenter(function(event) {
		$(this).addClass('animated infinite bounce');
	});

	$('#after_cartlogo').mouseleave(function(event) {
		$(this).removeClass('animated infinite bounce');
	});
	

//_____________________________________________________________


	function add_to_cart (e) {
		prod_id = this.getAttribute('id');
		var quantity = 1;

		$.ajax({
				type: 'GET',
				url: '/add_item/'+ prod_id +'/'+ quantity,
				data: {'product_id': prod_id,'quantity': quantity },
				success: function (quantity_count) {

					console.log( quantity_count) ;

					if (el_quantity) {
						el_quantity.textContent = quantity_count;
					}

					var el_quantity_be4 = document.querySelector('#quantity_be4_login');
					var el_quantity = document.querySelector('#quantity_login');
					var el_quantity_soci = document.querySelector('#quantity_social_login');

					if (el_quantity_be4){
						el_quantity_be4.textContent = quantity_count;
					}
					else if (el_quantity){
						el_quantity.textContent = quantity_count;
					}
					else{
						el_quantity_soci.textContent = quantity_count;
					}
				}
		});
	}

	var el_add_to_cart = document.querySelectorAll('.btn.add_to_cart');
	console.log(el_add_to_cart.length);

	for (var i = 0; i < el_add_to_cart.length; i++) {
		el_add_to_cart[i].addEventListener('click', add_to_cart , false);
	}

});