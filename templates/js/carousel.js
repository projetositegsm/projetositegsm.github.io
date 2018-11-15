function makeImageExpanded(img, carouselIdx) {
  var expandedImg = document.getElementById(`expandedImg-${carouselIdx}`);
  expandedImg.src = img.src;
}
