from flask import Flask, render_template

app = Flask(__name__, template_folder='src/frontend')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/styles.css')
def styles():
    return app.send_static_file('styles.css')

if __name__ == '__main__':
    app.run(debug=True)
