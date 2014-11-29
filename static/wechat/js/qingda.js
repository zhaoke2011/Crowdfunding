$(document).on("pageinit", "#index", function() {
	/*进度条*/
	if ($(".progressbar").length > 0) {
		$(".progressbar").each(function() {
			var pb = $(this).attr("data");
			if (pb <= 50) {
				$(this).addClass("less");

			} else {
				$(this).addClass("more");
			}
			$(this).find(".num").text(pb + '%');
			$(this).find(".bar").css("width", pb + '%');
		})
	}

	/*轮播*/
	if ($("#carousel").length > 0) {
		$('#carousel').slideBox({
			duration: 0.5, //滚动持续时间，单位：秒
			easing: 'linear', //swing,linear//滚动特效
			delay: 5, //滚动延迟时间，单位：秒
			hideClickBar: false, //不自动隐藏点选按键
			clickBarRadius: 10
		});
	}

});

var co_cover = $('.co_covers');
$(document).on("pageshow", "#pro_detail", function() {

	$.mobile.buttonMarkup.hoverDelay = "false";
	//alert(co_cover.height());
	//alert(co_cover.find('img').height());
	if (co_cover.length > 0) {

		$('#base_info').css('margin-top', co_cover.height() );
		$(".progress .bar").css("width", $(".progressbar").attr("data") + '%');
	}

});

$(".pro_detail #detailtabs").delegate(".ui-tabs-anchor", "click", function() {

	if ($(this).attr('id') == "ui-id-1") {
		$('#base_info').css('margin-top', co_cover.height() );
		$(".progress .bar").css("width", $(".progressbar").attr("data") + '%');
		co_cover.css('display', 'block');
	} else {
		$('#base_info').css('margin-top', 0);
		co_cover.css('display', 'none');
	}
});

$(".follow").delegate(".follow-heart", "click", function() {
	$(this).toggleClass('active');
});
