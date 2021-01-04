from flask import render_template, redirect, request, url_for, flash, current_app
from flask_login import login_manager, login_required, login_user, logout_user, current_user
from user_management.forms import UserForm, LoginForm
from user_management.models import User
from user_management import app, db, bcrypt
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
              return current_app.login_manager.unauthorized()
            if((current_user.user_role != role) and (role != "ANY")):
                return current_app.login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated and current_user.user_role == 'Administrator':
        return redirect(url_for('admin_dashboard'))
    if current_user.is_authenticated and current_user.user_role == 'User':
        return redirect(url_for('user_dashboard'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data) and user.user_role == 'Administrator':
            login_user(user, remember=form.remember.data)
            return redirect(url_for('admin_dashboard'))
        elif user and bcrypt.check_password_hash(user.password, form.password.data) and user.user_role == 'User':
            login_user(user, remember=form.remember.data)
            return redirect(url_for('user_dashboard'))
        else:
            flash('Login failed, your email or password is incorrect!', 'danger')
    return render_template('pages/login.html', form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
    
@app.route('/user/dashboard')
@login_required(role='User')
def user_dashboard():
    return render_template('pages/user/dashboard.html')
    
@app.route('/admin/dashboard')
@login_required(role='Administrator')
def admin_dashboard():
    return render_template('pages/admin/dashboard.html')
    
@app.route('/admin/create_user', methods=['GET', 'POST'])
@login_required(role='Administrator')
def create_user():
    form = UserForm()
    users = User.query.all()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password, user_role=form.userRole.data)
        db.session.add(user)
        db.session.commit()
        flash('User has been saved successfully!', 'success')
        return redirect(url_for('create_user'))
    return render_template('pages/admin/create_user.html', form=form, users=users)
    
@app.route('/admin/delete_user/<int:id>', methods=['GET', 'POST'])
@login_required(role='Administrator')
def delete_user(id):
    if request.method == 'POST':
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        flash('User data has been deleted successfully!', 'success')
        return redirect(url_for('create_user'))
    return redirect(url_for('create_user'))