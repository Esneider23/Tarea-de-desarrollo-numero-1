from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.document import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
docu = []
names = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/document', methods=['GET'])
def document():
    return render_template('document.html', name=names)


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    nationality = request.form['nationality']
    p = Person(id_person=id_person, name=first_name, last_name=last_name, nationality=nationality)
    model.append(p)
    names.append(first_name)
    return render_template('person_detail.html', value=p)


@app.route('/document_detail', methods=['POST'])
def document_detail():
    isbn = request.form['isbn']
    title = request.form['title']
    type = request.form['type']
    author = request.form['author']
    date_publication = request.form['date_publication']
    number = request.form['number']
    m = Document(isbn=isbn, title=title, author=author, type=type, date_publication=date_publication, number=number)
    docu.append(m)
    return render_template('document_detail.html', value=m)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name, i.nationality) for i in model]
    print(data)
    return render_template('people.html', value=data)


@app.route('/file')
def file():
    dal = [(a.isbn, a.title, a.author, a.type, a.date_publication a.number)for a in docu]
    print(dal)
    return render_template('file.html', value=dal)


if __name__ == '__main__':
    app.run()
