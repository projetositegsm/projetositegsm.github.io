let currModalImgIdx = 0;
const images = [
  {
    src: 'imgs/products/1.png',
    description: 'Nome do projeto',
  },
  {
    src: 'imgs/cases/02_Alphaville Jacuhy_1.png',
    description: 'Nome do projeto',
  },
  {
    src: 'imgs/cases/03_Alphaville Barra da Tijuca_8.png',
    description: 'Nome do projeto',
  }
];

function openImg(img) {
  var expandImg = document.getElementById("expandedImg");
  expandImg.src = img.src;
}

function closeModalImg() {
  const modal = document.getElementById("imgModal");
  modal.style.display = "none";
}

function goRight() {
  currModalImgIdx = (currModalImgIdx + 1)%(images.length);
  selectImage();
}

function goLeft() {
  currModalImgIdx = (currModalImgIdx - 1 + images.length)%(images.length);
  selectImage();
}

function selectImage() {
  const imgInModal = document.getElementById("imgInModal");
  const projectName = document.getElementById("projectName");
  const counter = document.getElementById("counter");

  imgInModal.src = images[currModalImgIdx].src;
  projectName.textContent = images[currModalImgIdx].description;
  counter.textContent = `${currModalImgIdx+1} de ${images.length}`;
}

function openModalImg(imgIndex) {
  const modal = document.getElementById("imgModal");
  currModalImgIdx = imgIndex;
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
