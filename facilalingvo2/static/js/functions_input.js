$(document).ready(function(){
	
	$('#select_all').change(function() {
	    var checkboxes = $(this).parent().find(':checkbox');
	    if($(this).is(':checked')) {
	        checkboxes.prop('checked', true);
	    } else {
	        checkboxes.prop('checked', false);
	    }
	});

});
