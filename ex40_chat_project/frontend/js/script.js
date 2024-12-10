const login = document.querySelector('.login')
const loginForm = login.querySelector('.loginForm')
const loginInput = login.querySelector('.loginInput')

const user = {id: "", name: "", color: ""}

const handleSubmit = (event) => {
    event.preventDefault()

    user.name = loginInput.value

    console.log(user)
}

loginForm.addEventListener('submit', handleSubmit)
