from flask import Flask, request, render_template
from datetime import datetime
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
        
        # Verificar se o email já existe
        email_exists = any(row[0] == email for row in register_page.iter_rows(values_only=True))
        
        if email_exists:
            return render_template('sign_up.html', email_exists_on_db=True)
        else:
            # Adicionar o novo registro
            register_page.append([email, password, register_date, register_time])
            book.save(register_db)
            return render_template('index.html')
        
    return render_template('sign_up.html', email_exists_on_db=False)

if __name__ == '__main__':
    app.run(debug=True)

