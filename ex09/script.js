const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function ask(query){
    return new Promise (resolve => rl.question(query, resolve));
}

async function test(){
    const name =  await ask("type ur name: ")
    let age = await ask("enter ur age: ")
    let weight = await ask("enter ur weight: ")

    console.log(name, age, weight)

    rl.close();
}

test()

const { resolve } = require('path');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function askName(query){
    return new Promise (resolve => rl.question(query, resolve));
}

async function askNameLoop() {
    const name = "rafa";
    let askNamePrompt = await askName("enter ur name: ")

    while (askNamePrompt != name){
        askNamePrompt = await askName("enter ur name again: ");
        console.log(`incorrect name, ${askNamePrompt}`)
    }

    console.log(`correct name, ${name}`);
    rl.close();
}

askNameLoop()

