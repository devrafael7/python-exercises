from flask import Flask, request, render_template
import openpyxl

app = Flask(__name__)

book = openpyxl.Workbook()
book.create_sheet('Form')

form_page = book['Form']
form_page.append(['Purchaser Name', 'Gender', 'Locatioon', 'Product', 'Price', 'Quantity'])
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name_value']
        gender = request.form['gender_type']
        location = request.form['location']
        product = request.form['product_name']
        price = request.form['price_value']
        quantity = request.form['quantity']
        
        form_page.append([name, gender, location, product, price, quantity])
        book.save('form_py.xlsx')

        return 'deu bom mermo'
    return render_template('index.html')
        
if __name__ == '__main__':
    app.run(debug=True)


