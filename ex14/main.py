from flask import Flask, request, render_template
import openpyxl

book = openpyxl.Workbook()

book.create_sheet('user_info')
user_info = book['user_info']

user_info.append(['Name', 'E-mail', 'Number', 'Password'])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method== 'POST':
        userName = request.form['user_name']
        userEmail = request.form['user_email']
        userNumber = request.form['user_number']
        userPassword = request.form['user_password']
        
        user_info.append([userName, userEmail, userNumber, userPassword])
        
        book.save('Lupo-Forms.xlsx')
        
        return 'deu bom chefe'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    

    

    
