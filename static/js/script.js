jQuery(document).ready(function() {
	jQuery('.srv_slider ul').jcarousel({
		visible: 1,
		scroll: 1,
		wrap: 'circular'
	});
	jQuery('.galery ul').jcarousel({
		visible: 4,
		scroll: 1,
		wrap: 'circular'
	});
    $('.menu_lvl_1_click').removeClass('menu_lvl_1_click');
});

$(function() {
    $('.menu li a').mouseover(
        function(e){
        // var posX = (e.pageX - $(this).offset().left -$(this).width());
        // if (posX > 0 ) {
            if ($(this).parent().is('.menu_lvl_1') || $(this).parent().parent().parent().is('.menu_lvl_1')) {
                $(this).parent().addClass('menu_lvl_1_click');
            } else {
                $('.menu_lvl_1_click').removeClass('menu_lvl_1_click');
            }
            return false;
        });
    $('.menu_lvl_1').hover(function(){},function() {
        $('.menu_lvl_1_click').removeClass('menu_lvl_1_click');
    });

    $('.fancybox').fancybox();

    $('#send_question').live('click',function(){
        $.ajax({
            url: "/faq/checkform/",
            data: {
                name:$('#id_name').val(),
                question:$('#id_question').val(),
                email:$('#id_email').val()
            },
            type: "POST",
            success: function(data) {
                if (data=='success')
                    {$('.modal_form').replaceWith("Спасибо за вопрос, мы постараемся ответить на него в самое ближайшее время!");}
                else{
                    $('.modal_form').replaceWith(data);
                }
            }
        });

        return false;
    });


});
jQuery('input[placeholder], textarea[placeholder]').placeholder();