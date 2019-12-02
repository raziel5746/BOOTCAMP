from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.jinja', 'r') as f:
        html = f.read()
        today = datetime.today()
        my_date = today.strftime('%B %-d, %Y')
        return render_template_string(html, date=my_date)

if __name__ == "__main__":
    app.run()

