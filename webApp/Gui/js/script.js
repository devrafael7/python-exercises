const defaultQueryBtn = document.querySelector('.defaultQueryBtn');

const defaultQueryTable = document.querySelector('.defaultQueryTable');
defaultQueryBtn.addEventListener('click', ()=>{
    defaultQueryTable.classList.remove('hidden')
})

const exitBtn = document.querySelector('.exitBtn');
exitBtn.addEventListener('click', ()=>{
    defaultQueryTable.classList.add('hidden');
})