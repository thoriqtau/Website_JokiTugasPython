from app.model.user import Users
from flask import render_template, request,session,url_for,redirect
from config import Config
from app import db, app
from datetime import timedelta, datetime

# Atur waktu sesi menjadi 30 menit
app.permanent_session_lifetime = timedelta(minutes=1)

def index():
    if 'username' in session:
        session_start_time = datetime.now()
        time_remaining = app.permanent_session_lifetime.total_seconds() - \
        (datetime.now() - session_start_time).total_seconds()
        if time_remaining > 0:
            return render_template('index.html')
        else:
            session.pop('username', None)
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


def login():
    # return render_template('login.html')
    if 'username'in session :
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # cursor koneksi mysql
            # eksekusi kueri
            user = Users.query.filter_by(username=username,password=password).first()
            print(user)
            # fetch hasil kueri
            if user:
                # jika login valid buat data session
                    session["username"] = username
                # redirect ke halaman home
                    return redirect(url_for("home"))
            else:
                eror = "username tau password tidak terdaftar"
                # jika login invalid kembalikan ke login form
                return render_template("login.html",eror = eror)
        else:
            # " jika method selain POST tampilkan form login"
            return render_template('login.html')

def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = Users(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    else:
        return render_template('register.html')

