from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Email, Length

class Contact(FlaskForm):
    """Contact form."""

    name = StringField("Name", [DataRequired()])
    email = StringField(
        "Email", [Email(message="This is not a valid email address."), DataRequired()]
    )
    body = TextAreaField(
        "Message", [DataRequired(), Length(min=4, message="This message is too short. Please write something longer :)")]
    )
    submit = SubmitField("Submit")
