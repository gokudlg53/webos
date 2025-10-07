from flask import Flask, render_template
import os

app = Flask(name)  # Usa 'templates/' por defecto

@app.route('/')
def home():
    return render_template('index.html')

if name == 'main':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
