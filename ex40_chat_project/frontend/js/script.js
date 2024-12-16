const login = document.querySelector('.login')
const loginForm = login.querySelector('.loginForm')
const loginInput = login.querySelector('.loginInput')

const chatSection = document.querySelector('.chatSection')
const chatForm = chatSection.querySelector('.chatForm')
const chatInput = chatSection.querySelector('.chatInput')
const chatMessages = chatSection.querySelector('.chatMessages')

const colors = [
    "cadetblue",
    "darkgoldenrod",
    "cornflowerblue",
    "darkkhaki",
    "hotpink",
    "gold"
]

const user = {id: "", name: "", color: ""}

let websocket 

const createMessageSelfElement = (content) => {
    const article = document.createElement("article")

    article.classList.add(
        'selfMessage',
        'self-end',
        'bg-green-500',
        'text-white',
        'py-2',
        'px-4',
        'rounded-t-xl',
        'rounded-bl-xl',
        'max-w-xs',
        'break-words',
        'text-lg',
        'shadow-md'
    );

    article.innerHTML = content

    return article
}


const createMessageOtherElement = (content, sender, senderColor) => {
    const article = document.createElement("article")
    const span = document.createElement("span")

    article.classList.add(
        'messageOther',
        'self-start',
        'bg-gray-200',
        'text-black',
        'py-2',
        'px-4',
        'rounded-t-xl',
        'rounded-br-xl',
        'ax-w-xs',
        'break-words',
        'text-lg',
        'shadow-md'
    );

    span.classList.add(
        'messageSender',
        'block',
        'font-bold',
        'mb-1'
    )

    span.style.color = senderColor

    article.appendChild(span)

    span.innerHTML = sender
    article.innerHTML += content

    return article
}

const getRandomColor = ()=>{
    const randomIndex = Math.floor(Math.random() * colors.length)
    return colors[randomIndex]
}

const scrollScreen = () => {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    })
}

const processMessage = ( { data } ) => {
    const { userId, userName, userColor, content } = JSON.parse(data)

    const message = userId == user.id
        ? createMessageSelfElement(content) 
        :createMessageOtherElement(content, userName, userColor)

    chatMessages.appendChild(message)

    scrollScreen()
}

const handleLogin = (event) => {
    event.preventDefault()

    user.id = crypto.randomUUID()
    user.name = loginInput.value
    user.color = getRandomColor()

    login.classList.add('hidden')

    chatSection.classList.remove('hidden')

    websocket = new WebSocket("ws://localhost:8080")
    websocket.onmessage = processMessage

    console.log(user)
}

const sendMessage = (event) => {
    event.preventDefault()

    const message = {
        userId: user.id,
        userName: user.name,
        userColor: user.color,
        content: chatInput.value
    }

    websocket.send(JSON.stringify(message))

    chatInput.value = ""
}

loginForm.addEventListener('submit', handleLogin)
chatForm.addEventListener('submit', sendMessage)











