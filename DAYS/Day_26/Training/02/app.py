from flask import Flask, render_template_string, render_template
import database_manager

app = Flask(__name__)
app = Flask(__name__, template_folder='templates')
database_manager.create_database()

@app.route('/')
@app.route('/products')
def products_page():
    data = database_manager.load_database()
    with open('style.css', 'r') as f:
        css = f.read()
    return render_template('my_template.jinja', products=data, css=css)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
