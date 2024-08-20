const XLSX = require('xlsx');

const book = XLSX.utils.book_new();

const bookData = [
    ['Fruits', 'Quantity', 'Price'],
    ['banana', '5', 'R$4,90'],
    ['fruit 2', '2', 'R$6,99'],
    ['fruit 3', '12', 'R$12,29'],
    ['fruit 4', '20', 'R$3,90']
]

const bookDataFruits = XLSX.utils.aoa_to_sheet(bookData);

XLSX.utils.book_append_sheet(book, bookDataFruits, 'Fruits');

XLSX.writeFile(book, 'shopping-spreadsheet-js.xlsx');

