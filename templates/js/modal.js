let currModalImgIdx = 0;

const caseImages = [];
{% for case in data["cases"] %}
  caseImages.push({
    "src": "imgs/cases/{{ case['img'] }}",
    "description": "{{ case['description'] }}",
  });
{% endfor %}

function openImg(img) {
  var expandImg = document.getElementById("expandedImg");
  expandImg.src = img.src;
}

function closeModalImg() {
  const modal = document.getElementById("imgModal");
  modal.style.display = "none";
}

function goRight() {
  currModalImgIdx = (currModalImgIdx + 1)%(caseImages.length);
  selectImage();
}

function goLeft() {
  currModalImgIdx = (currModalImgIdx - 1 + caseImages.length)%(caseImages.length);
  selectImage();
}

function selectImage() {
  const imgInModal = document.getElementById("imgInModal");
  const projectName = document.getElementById("projectName");
  const counter = document.getElementById("counter");

  imgInModal.src = caseImages[currModalImgIdx].src;
  projectName.textContent = caseImages[currModalImgIdx].description;
  counter.textContent = `${currModalImgIdx+1} de ${caseImages.length}`;
}

function openModalImg(imgIndex) {
  const modal = document.getElementById("imgModal");
  currModalImgIdx = imgIndex - 1;
  selectImage();
  modal.style.display = "block";
}

function checkKey(e) {
  e = e || window.event;
  if (e.keyCode == '37') {
    goLeft();
  }
  else if (e.keyCode == '39') {
    goRight();
  }
}

document.onkeydown = checkKey;
