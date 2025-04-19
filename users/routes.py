from flask import (Blueprint,
                   request,
                   render_template,
                   redirect,
                   url_for,
                   session, flash)

from models import Users, db

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    #TODO: The action depedens if it's going to register like a company or a worker. JMN
    if request.method == 'POST':
        name = request.form.get('name', '')
        last_name = request.form.get('last_name', '')
        password = request.form.get('password', '')
        email = request.form.get('email', '')
        role = request.form.get('role', '')

        user = Users(name, last_name, password, email, role)

        db.session.add(user)
        db.session.commit()


        return redirect(url_for('users.login', role = role))

    return render_template('auth/register.html'), 200

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form.get('email')
        user_password = request.form.get('password')
        user = Users.get_by_email(user_email)

        if user is not None and user_password == user.password:
            session['email'] = user.email
            session['password'] = user.password
            session['role'] = user.role
            session['name'] = user.name
            session['user_id'] = user.id

            return redirect(url_for('hire.redirect_home'))
    return render_template('auth/login.html')

@users_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('users.login'))