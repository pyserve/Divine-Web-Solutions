$(function (e) {
	$(".preloader-container").fadeOut("slow");
	document.onscroll=function (e) {
	    if (window.pageYOffset > 235) {
	      $(".navbar-menu").addClass("fixed-top");
	    }else{
	      $(".navbar-menu").removeClass("fixed-top");
	    }
	    if (window.pageYOffset > 150) {
	      $(".scrolltopbtn").css({'display': 'block'});
	    }else{
	      $(".scrolltopbtn").css({'display': 'none'});
	    }
	   if ($(window).width() < 768) {
	   		if (window.pageYOffset > 235) {
		   		$(".navbar-menu").removeClass("fixed-top");
		   		$(".navbar-container").addClass("fixed-top");
		   	}else{
		      $(".navbar-container").removeClass("fixed-top");
		    }
	   }else{
	   		$(".navbar-container").removeClass("fixed-top");
	   }
	}
	$("#explorebtn").click(function (e) {
		let aboutus=$("#aboutus").offset();
		$('html, body').animate({
	        scrollTop: (aboutus.top/2)
	    }, 1000);
	});

	$(".scrolltopbtn").click(function (e) {
		$('html, body').animate({
	        scrollTop: 0
	    }, 600);
	});

	$(".openchatbtn button").click(function (e) {
		$(".chat-popup").css({'display':'block'});
		$(".openchatbtn").css({'display':'none'});
	});
	$(".closechatbtn").click(function (e) {
		$(".chat-popup").css({'display':'none'});
		$(".openchatbtn").css({'display':'block'});
	});

	$(".contactform").submit(function (e) {
		e.preventDefault();
		$.ajax({
			url: '/contact/',
			method: 'POST',
			data: new FormData(this),
	  		cache: false,
	      	contentType: false,
      		processData: false,
			success: function (data) {
				if (data['success']=='1') {
					window.open('/contact/','_self');
				}
				if (data['success']=='0') {

				}
			},
			error: function (error_data) {
				console.log(error_data);
			}
		});
	});
	$(".mediapreview span").click(function (e) {
		let postid=$(this).attr('id');
		window.open('/blog/'+postid+'/','_self');
	});
	$(".likepost").click(function (e) {
		let likepost=$(this);
		let postid=$(this).attr('class').split(" ")[0];
		let likecount=$(this).find(".likecount");
		$.ajax({
			url: '/blog/like/',
			method: 'get',
			data: {
				'postid': postid,
			},
			success: function (data) {
				if(data['liked']=='yes'){
					likecount.html(data['likescount']);
					likepost.addClass('text-primary');
				}else if(data['liked']=='no'){
					likecount.html(data['likescount']);
					likepost.removeClass('text-primary');
				}else{
					window.open('/accounts/login/?next=/blog/'+postid+'/','_self');
				}
			},
			error: function (error_data) {
				console.log(error_data);
			},
		});
	});

	$(".commentbtn").attr('disabled',"");
	$(".comment").keyup(function () {
		if (/\S/.test($(this).val())) {
			$(".commentbtn").removeAttr('disabled');
		}else{
			$(".commentbtn").attr('disabled',"");
		}
	});

	$(".commentform").submit(function (e) {
		e.preventDefault();
		let formdata=new FormData(this);
		let commentform=$(this);
		let commentinput=$(this).find(".comment");
		let commentbtn=$(this).find("span button");
		commentbtn.attr('disabled',"");
		$.ajax({
			url: '/blog/comment/',
			method: 'POST',
			data: formdata,
	  		cache: false,
	      	contentType: false,
      		processData: false,
			success: function (data) {
				document.getElementById("commentsound").play();
				$(".showblogcomment").append(data);
				commentinput.val('');
				commentbtn.removeAttr('disabled');
				$(".nocommentyet").remove();
			},
			error: function (error_data) {
				console.log(error_data);
			}
		});
	});
});