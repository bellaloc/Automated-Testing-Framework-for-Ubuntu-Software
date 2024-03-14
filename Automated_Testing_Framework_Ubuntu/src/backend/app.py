from flask import Flask, render_template
import os

app = Flask(__name__)

# Set the template directory explicitly
template_dir = os.path.abspath('../frontend')
app.template_folder = template_dir

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
