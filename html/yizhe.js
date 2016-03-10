function updateContent(tar,url){
	$(tar).load(url);			
};
function sizeAdjust(tar) {
	var max_width = document.body.clientWidth-175-$("#sframe").width()-$("#tframe").width();
	// hide QRcode
	if (max_width > 950) {
		max_width = 950;
	}
	//document.body.clientHeight window.screen.availHeight
	var max_height =  document.documentElement.clientHeight -100-$("#menu_container").height();
	$(tar).css("width",max_width);
	$(tar).css("height",max_height);
}
function bodyAdjust() {
	sizeAdjust('#aframe');
}
function refreshIframe(ifr,surl) {
	$(ifr).src=surl;
	alert(surl);
}
$(document).ready(function loadContainers(){
	updateContent('#menu_container','menu.html');
	updateContent('#content_container','pedia.html');
});