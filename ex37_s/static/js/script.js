
// Loguin button variables

const divLoginBtns = document.querySelector('.divLoginBtns')
const whiteLoguinBtn = document.querySelector('.whiteLoguinBtn')
const signUpBtn = document.querySelector('.signUpBtn')
const signInBtn = document.querySelector('.signInBtn')

const signInText = document.querySelector('.signInText')
const signUpText = document.querySelector('.signUpText')

// Loguin Button Funcionality

signUpBtn.addEventListener('click', ()=>{
    whiteLoguinBtn.classList.add('WLB_left_transition')
    signUpText.classList.remove('text-white')
    signUpText.classList.add('text-black')

    signInText.classList.remove('text-black')
    signInText.classList.add('text-white')
})

signInBtn.addEventListener('click', ()=>{
    whiteLoguinBtn.classList.remove('WLB_left_transition')
    signInText.classList.remove('text-white')
    signInText.classList.add('text-black')

    signUpText.classList.remove('text-black')
    signUpText.classList.add('text-white')
})

// Page navigation delay

signUpBtn.addEventListener('click', function(event){
    event.preventDefault();

    setTimeout(function(){
        window.location.href = event.target.href;   
    }, 400);
});

signInBtn.addEventListener('click', function(event){
    event.preventDefault();

    setTimeout(function(){
        window.location.href = event.target.href;   
    }, 400);
});








