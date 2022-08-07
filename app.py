from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///COURSES_PEXON.db'
db = SQLAlchemy(app)

## Datenbank-Model definieren ##
class Courses(db.Model):
        id =db.Column(db.Integer, primary_key=True)
        content = db.Column(db.String(200), nullable=False)
        date_created = db.Column(db.DateTime, default=datetime.now)

        def __repr__(self):
                return '<Course %r>' % self.id

## Funktionalität der Starsteite definieren ##
@app.route('/', methods=['POST', 'GET'])
def index():
        if request.method == 'POST':
                course_content = request.form['content']
                new_course_record= Courses(content=course_content)

                try:
                        db.session.add(new_course_record)

                        ## neuen Eintrag in Datenbank committen ##
                        db.session.commit()
                        return redirect('/')

                        
                except:
                        return 'There was an issue adding your record'
        else:
                records = Courses.query.order_by(Courses.date_created).all()
                return render_template('index.html', records=records)

## Funktionalität der Lösch-Funktion definieren ##
@app.route('/delete/<int:id>')  
def delete(id):
        record_to_delete = Courses.query.get_or_404(id)

        try: 
                db.session.delete(record_to_delete)

                 ## gelöschten Eintrag in Datenbank committen ##
                db.session.commit()
                return redirect('/')
        except: 
                return 'There was a Problem deleting that record '

## Funktionalität der Update-Funktion definieren ##
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
        record = Courses.query.get_or_404(id)

        if request.method == 'POST':
                record.content = request.form['content']

                try:
                         ## veränderten Eintrag in Datenbank committen ##
                        db.session.commit()
                        return redirect('/')
                except:
                        return 'There was a Problem updating that record '
        else:
                return render_template ('update.html', record=record)


if __name__ == "__main__":
    app.run(debug=True)