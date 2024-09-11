const readmoreBtns = document.querySelectorAll('.readmoreBtn');

readmoreBtns.forEach(readmoreBtn => {
    readmoreBtn.addEventListener('click', () => {
        const readMoreCard = document.querySelector('.readMoreCard')
        readMoreCard.classList.toggle('hidden')

     
    });
});

const quantityCard = document.querySelector('.quantityCard')
quantity_total = 0

const addToCartBtn = document.querySelectorAll('.addToCartBtn')
addToCartBtn.forEach(addToCartBtns => {
    addToCartBtns.addEventListener('click', ()=>{
        quantity_total += 1
        quantityCard.textContent = quantity_total
    })
})

