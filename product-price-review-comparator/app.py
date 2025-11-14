from flask import Flask, render_template, request, send_file, redirect, url_for
import os
from modules.compare import compare_product

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    query = ''
    if request.method == 'POST':
        query = request.form.get('product').strip()
        if query:
            result = compare_product(query)
    return render_template('index.html', result=result, query=query)

if __name__ == '__main__':
    # For development only. Use a proper WSGI server for production.
    app.run(host='0.0.0.0', port=5000, debug=True)
