from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moodtracker.db'
db = SQLAlchemy(app)

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    uname = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(30), nullable=False)
    dob = db.Column(db.DateTime, nullable=True)
    gender = db.Column(db.String(1), nullable=False)        
    pts = db.Column(db.Integer, nullable=True)     

class Mood(db.Model):
    mid = db.Column(db.Integer, primary_key=True, nullable=False)
    mname = db.Column(db.String(10), nullable=True)
    type = db.Column(db.String(10), nullable=True)
    booster = db.Column(db.Integer, nullable=True)
    activity = db.Column(db.Text, nullable=True)

class Feel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=True)
    mid = db.Column(db.Integer, db.ForeignKey('mood.mid'), nullable=True)
    day = db.Column(db.Date, nullable=False)
    scale = db.Column(db.Integer, nullable=True)
    cause = db.Column(db.Text, nullable=True)

    def __repr__(self) -> str:
        return f"{self.id} - {self.cause}"

@app.route('/')
def index():
    users = User.query.all()
    moods = Mood.query.all()
    feels = Feel.query.all()
    return render_template('index.html', users=users, moods=moods, feels=feels)

# @app.route('/add_user', methods=['POST'])
# def add_user():
#     uname = request.form['uname']
#     email = request.form['email']
#     dob = request.form['dob']
#     gender = request.form['gender']
#     pts = request.form['pts']
#     new_user = User(uname=uname, email=email, dob=dob, gender=gender, pts=pts)
#     db.session.add(new_user)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/add_mood', methods=['POST'])
# def add_mood():
#     mname = request.form['mname']
#     type = request.form['type']
#     booster = request.form['booster']
#     activity = request.form['activity']
#     new_mood = Mood(mname=mname, type=type, booster=booster, activity=activity)
#     db.session.add(new_mood)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/add_feel', methods=['POST'])
# def add_feel():
#     uid = request.form['uid']
#     mid = request.form['mid']
#     day = request.form['day']
#     scale = request.form['scale']
#     cause = request.form['cause']
#     new_feel = Feel(uid=uid, mid=mid, day=day, scale=scale, cause=cause)
#     db.session.add(new_feel)
#     db.session.commit()
#     return redirect(url_for('index'))

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)