from nis import cat
from flask import redirect, render_template, url_for, flash
from market import app
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

# # static routing
# @app.route("/static")
# def about():
#     return "<h2>About</h2>"

# # dynamic routing
# @app.route("/about/<username>")
# def about_page(username):
#     return f"<h3> About {username} </h3>"


@app.route("/market")
@login_required
def market_page():
    items = Item.query.all()
    return render_template("market.html", items = items)
    # the second argument is seen as a placeholder in market.html
    # that is the data we send to the template


@app.route("/register", methods=["POST", "GET"])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        created_user = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password1.data # hashed password
        )
        db.session.add(created_user)
        db.session.commit()

        login_user(created_user)
        flash(
            f"Account created successfully! You are now logged in as {created_user.username}",
            category="success"
        )

        return redirect(url_for('market_page'))

    if form.errors != {}: # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category="danger")

    return render_template("register.html", form = form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()

        if attempted_user and attempted_user.check_password_correction(
            form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as {attempted_user.username}', category='success')

            return redirect(url_for('market_page'))
        else:
            flash('Username and password do not match! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash("You have been logged out", category="info")
    return redirect(url_for("home_page"))