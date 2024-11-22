from flask import Flask, render_template
import os

app = Flask(__name__)

# Debugging information
print("Current directory:", os.getcwd())  # Check Flask's working directory
print("Template search path:", app.jinja_loader.searchpath)  # Check where Flask looks for templates

@app.route('/')
def index():
    return render_template('index.html')  # Flask looks in the templates folder for this file

if __name__ == '__main__':
    app.run(debug=True)
