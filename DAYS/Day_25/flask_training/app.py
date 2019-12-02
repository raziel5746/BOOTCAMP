from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html = 'Bazinga'
    return html


@app.route('/home/<my_name>')
def personal_index(my_name):
    html = f'''
    <html>
        <head>
            <title>MyTitle</title>
        </head>
        <body>
            <h1>Bazinga {my_name}!</h1>
        </body>
    </html>
    '''

    return html

@app.route('/home2/<my_name>')
def template_index(my_name):
    with open('index.jinja','r') as f:
        html = f.read()
    length = len(my_name)
    return render_template_string(html, name=my_name, length=length)

if __name__ == "__main__":
    app.run()