$('.main-carousel').flickity({
  // options
  cellAlign: 'center',
  contain: true,
  accessibility: true,
  autoPlay: false,
  wrapAround: false,
  pageDots: true,
  initialIndex: 1,
  prevNextButtons: false,
  dragThreshold: 10,
  cellSelector: '.carousel-cell',
  setGallerySize: false
});

let dot = document.getElementsByClassName('dot');
dot[0].innerHTML = '<i i class="fas fa-bars"></i>'