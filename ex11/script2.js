const XLSX = require('xlsx');
const book = XLSX.readFile('shopping-spreadsheet-js.xlsx');

const ws = book.Sheets['Fruits'];
const wsData = XLSX.utils.sheet_to_json(ws, {header: 1});

for (let row of wsData){
    for (let i = 0; i < row.length; i = i + 1){
        if (row[i] === 'banana'){
            row[i] = 'fruit 1';
        }
    }
}

const newWs = XLSX.utils.aoa_to_sheet(wsData);

book.Sheets['Fruits'] = newWs;
XLSX.writeFile(book, 'shopping-spreadsheet-js.xlsx');


