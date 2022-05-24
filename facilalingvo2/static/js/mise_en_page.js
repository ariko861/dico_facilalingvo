$(document).ready(function(){
	
	var miseEnPage = $("#mise_en_page");
	var p = $("p");
	var B = $(".B");
	var I = $(".I");
	var A = $(".A");
	
	colorB = B.css("color");
	colorI = I.css("color");
	colorA = A.css("color");
	
	var lttrspc = "Letter spacing";
	
	miseEnPage.prepend('</br><button id="print">Print</button>');
	miseEnPage.prepend('</br>Colors <input type=checkbox id="colors" checked>');
	miseEnPage.prepend('&nbsp; '+lttrspc+':<input id="letter_spacing" type=number style="width:35px" val=0 step=0.5>px   ');
	miseEnPage.prepend('&nbsp; Word spacing:<input id="word_spacing" type=number style="width:35px" val=0 step=0.5>px   ');
	miseEnPage.prepend('&nbsp; Line height:<input id="line_height" type=number style="width:35px" val=0 step=0.5>px   ');
	miseEnPage.prepend('&nbsp; Font size:<input id="police" type=number style="width:30px" val=0 step=1 min=0>px   ');
	miseEnPage.prepend('Font family:<select id="font_family"><option style="font-family:Arial;">Arial</option><option style="font-family:Arial Black;">Arial Black</option><option style="font-family:Comic sans MS;">Comic sans MS</option><option style="font-family:Courier;">Courier</option><option style="font-family:Courier New;">Courier New</option><option style="font-family:Impact;">Impact</option><option style="font-family:Times New Roman;">Times New Roman</option><option style="font-family:Trebuchet MS;">Trebuchet MS</option><option selected style="font-family:Verdana;">Verdana</option></select>    ');
	
	var police = p.css("font-size");
	police = parseInt(police);
	$("#police").val(police);
	
	var letter_spacing = p.css("letter-spacing");
	letter_spacing = parseInt(letter_spacing);
	$("#letter_spacing").val(letter_spacing);
	
	var word_spacing = p.css("word-spacing");
	word_spacing = parseInt(word_spacing);
	$("#word_spacing").val(word_spacing);
	
	var line_height = p.css("line-height");
	line_height = parseInt(line_height);
	$("#line_height").val(line_height);
	
	$("#print").click(function(){
		window.print();
	});
	
	miseEnPage.change(function(){
		var new_police = $("#police").val();
		new_police = new_police + "px";
		
		var new_letter_spacing = $("#letter_spacing").val();
		new_letter_spacing = new_letter_spacing + "px";
		
		var new_word_spacing = $("#word_spacing").val();
		new_word_spacing = new_word_spacing + "px";
		
		var new_line_height = $("#line_height").val();
		new_line_height = new_line_height + "px";
		
		var new_font_family = $("#font_family option:selected").text();
		
		if ($("#colors").prop("checked")){
			B.css("color",colorB);
			I.css("color",colorI);
			A.css("color",colorA);
			
		}else{
			B.css("color","black");
			I.css("color","black");
			A.css("color","black");
			
		}
		p.css({"font-size":new_police,"letter-spacing":new_letter_spacing,"word-spacing":new_word_spacing,"line-height":new_line_height,"font-family":new_font_family});
		$("#tablenumber").css({"font-size":new_police,"letter-spacing":new_letter_spacing,"word-spacing":new_word_spacing,"line-height":new_line_height,"font-family":new_font_family});
		$("#bignumbers").css({"font-size":new_police,"letter-spacing":new_letter_spacing,"word-spacing":new_word_spacing,"line-height":new_line_height,"font-family":new_font_family});
	});
	
});
