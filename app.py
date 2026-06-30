from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the main Cash Counter UI."""
    return render_template('index.html')

if __name__ == '__main__':
    # Running on port 5000 with debug mode enabled for easy development
    app.run(host='0.0.0.0', port=5000, debug=True)
