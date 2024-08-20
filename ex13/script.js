const graphic = document.querySelector('.graphic');
graphic.classList.toggle('yellow-graphic');

graphic.addEventListener('click', ()=>{
    graphic.classList.toggle('blue-graphic');
    graphic.classList.toggle('yellow-graphic');
})