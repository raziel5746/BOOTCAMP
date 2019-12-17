from app import app, db
from app.models import Book, Author
from app.forms import AddForm
from flask import redirect, render_template


@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def addbook():
    form = AddForm()

    if form.validate_on_submit():
        title = form.title.data
        author_name = form.author.data
        price = form.price.data

        if author_name.lower() not in [aut.name.lower() for aut in Author.query.all()]:
            author = Author(name=author_name)
            db.session.add(author)
        else:
            author = Author.query.filter_by(name=author_name).first()

        newbook = Book(title=title, author=author, price=price)
        db.session.add(newbook)
        db.session.commit()
        return redirect('/')
    return render_template('add_book.html', form=form)
