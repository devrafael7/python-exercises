from flask import Flask, request, render_template
from datetime import datetime
import os
import openpyxl

app = Flask(__name__)

register_db = 'register_db.xlsx'

book = openpyxl.load_workbook(register_db)
register_page = book.active

@app.route('/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        register_date = datetime.now().strftime('%Y-%m-%d')
        register_time = datetime.now().strftime('%H:%M:%S')
        
        email_exists = False
        
        for row in register_page.iter_rows(values_only=True):
            if row[0] == email:
                email_exists = True
        
        if email_exists:
            print('Already have an accout was called')
        
        else:
            register_page.append([email, password, register_date, register_time])
            book.save(register_db)
            return render_template('index.html')
        
    return render_template('sign_up.html')




if __name__ == '__main__':
    app.run(debug=True)
