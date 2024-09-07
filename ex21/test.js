const orderBtn = document.querySelector('.orderBtn');

orderBtn.addEventListener('click', ()=>{
    let dataName = document.querySelector('.cardName').getAttribute('data-name')

    let dataPrice = document.querySelector('.cardPrice').getAttribute('data-price')

    let dataPlace = document.querySelector('.cardPlace').getAttribute('data-place')

    let dataQuantity = document.querySelector('.cardQuantity').getAttribute('data-quantity');

    fetch('/get_info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            dataName: dataName,
            dataPrice: dataPrice,
            dataPlace: dataPlace,
            dataQuantity: dataQuantity
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Server response: ', data.message);
    });
})