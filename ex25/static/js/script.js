const readmoreBtns = document.querySelectorAll('.readmoreBtn');

readmoreBtns.forEach(readmoreBtn => {
    readmoreBtn.addEventListener('click', () => {
        const card = readmoreBtn.closest('.card'); 
        const cardImgSrc = card.querySelector('.cardImg').src; 

     
    });
});