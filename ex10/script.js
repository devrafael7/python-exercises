const { table } = require('console');
const { type } = require('os');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function ask(question){
    return new Promise(resolve => rl.question(question, resolve));
}

async function evenOrOdd() {
    let number = await ask("Enter a number: ");

    number = number.replace(",", ".");

    try {
        number = parseFloat(number);

        if (Number.isInteger(number)) {
            if (number % 2 === 0) {
                console.log(`${number} is even`);
            } else {
                console.log(`${number} is odd`);
            }
        } else {
            console.log("Please enter an integer.");
        }

    } catch (error) {
        console.log("An error occurred:", error.message);
    }
}

//evenOrOdd();

async function calculator(){
    number = await ask("enter a first number: ")
    number2 = await ask("enter a second number: ")

    number = parseInt(number)
    number2 = parseInt(number2)

    if (isNaN(number) || isNaN(number2)){
        console.log("enter a number please")
        return rl.close()
    }

    operator = await ask("choose one of these options: + | - | * | /: ")

    if (operator === "+"){
        console.log(`the sum of the numbers is equals: ${number + number2}`) 
    } else if (operator === "-"){
        console.log(`the subtraction of the numbers is equals: ${number - number2}`) 
    } else if (operator === "*"){
        console.log(`the multiplication of the numbers is equals: ${number * number2}`) 
    } else if (operator === "/"){
        console.log(`the division of the number is equals: ${number / number2}`) 
    } else {
        console.log("choose one of those options please") 
    }

    rl.close()

}

//calculator()

function loop(){
    for (let i = 0;i < 11; i = i + 1) {
        console.log(i)
    }
}

//loop()

function fruitsIndex(){
    const fruits = ['apple', 'banana', 'cherry', 'strawberry', 'mango', 'grape'];

    for (let i = 0; i < fruits.length; i = i + 1){
        console.log(fruits[i])
    }
}

//fruitsIndex()

async function tableOfNumber(){
    let number = await ask("enter a number: ")
    number = parseInt(number)

    for (let i = 0; i < 11; i = i + 1){
        console.log(`${number} x ${i} = ${number * i}`)
    };
}

//tableOfNumber()