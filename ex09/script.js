const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function ask(question) {
    return new Promise(resolve => rl.question(question, resolve));
}

async function collectUserData() {
    const name = await ask("Type your name: ");
    const age = await ask("Enter your age: ");
    const weight = await ask("Enter your weight: ");

    console.log(`Name: ${name}, Age: ${age}, Weight: ${weight}`);

}

async function validateName() {
    const correctName = "rafa";
    let userName = await ask("Enter your name: ");

    while (userName !== correctName) {
        console.log(`Incorrect name, ${userName}`);
        userName = await ask("Enter your name again: ");
    }

    console.log(`Correct name, ${userName}`);
    rl.close(); 
}

collectUserData().then(()=> validateName())


