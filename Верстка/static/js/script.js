jQuery(document).ready(function() {
	jQuery('.srv_slider ul').jcarousel({
		visible: 1,
		scroll: 1,
		wrap: 'circular'
	});
	jQuery('.galery ul').jcarousel({
		visible: 3,
		scroll: 1,
		wrap: 'circular'
	});
	jQuery('input[placeholder], textarea[placeholder]').placeholder();
});
	$(function() {
		$('.menu_arr').click(function(){
            if ($(this).parent().is('.menu_lvl_1_click')) {
                $(this).parent().removeClass('menu_lvl_1_click');
            } else {
                $(this).parent().addClass('menu_lvl_1_click');
            }
            return false;
        });
	});