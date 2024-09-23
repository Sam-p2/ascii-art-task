from flask import Flask, render_template
import pyfiglet

app = Flask(__name__)

@app.route('/')
def index():
    name = "Samuel"  # Set the name to "Samuel"
    ascii_art = pyfiglet.figlet_format(name)
    return render_template('index.html', ascii_art=ascii_art)

if __name__ == "__main__":
    app.run(debug=True)
git add app.py

