from flask import Flask, render_template
import threading
import webview  # pywebview

app = Flask(__name__)

@app.route('/')
def home():
    nome = "Rafael"
    return render_template('index.html', nome=nome)

def start_flask():
    app.run(debug=False, use_reloader=False) 

if __name__ == '__main__':
    threading.Thread(target=start_flask).start()
    webview.create_window("Meu App", "http://127.0.0.1:5000", width=600, height=800)
