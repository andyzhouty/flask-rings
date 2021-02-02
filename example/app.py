from flask import Flask, render_template
from flask_rings import Rings
from wtforms import StringField, PasswordField, TextAreaField, DateField, SubmitField
from flask_wtf import FlaskForm


app = Flask(__name__)
rings = Rings(app)
app.secret_key = 'dev'


class HelloForm(FlaskForm):
    username = StringField("Type anything")
    password = PasswordField("TOP SECRET!!!")
    textarea = TextAreaField("A large textarea!")
    date = DateField("Date Input")
    submit = SubmitField()


@app.route("/", methods=["GET", "POST"])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        username = form.username.data
        textarea = form.textarea.data
        date = form.date.data
        return render_template("result.html", username=username, textarea=textarea, date=date)
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run()
