from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Bem-vindo ao Flask!</h1>"
if __name__ == '__main__':
    app.run(debug=True)