from flask import Flask, render_template
from flask_rings import Rings
from wtforms import StringField, PasswordField, TextAreaField
from flask_wtf import FlaskForm


app = Flask(__name__)
rings = Rings(app)
app.secret_key = 'dev'


class HelloForm(FlaskForm):
    username = StringField("Type anything")
    password = PasswordField("TOP SECRET!!!")
    textarea = TextAreaField("A large textarea!")


@app.route("/")
def index():
    form = HelloForm()
    # if form.validate_on_submit():
    #     username = form.username.data
    #     password = form.password.data
    #     textarea = form.textarea.data
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run()
