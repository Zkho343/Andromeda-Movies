from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class MovieReviewForm(FlaskForm):
    rating = SelectField(label='Please Rate This Movie', choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    review_text = StringField(label='Please Comment For This Movie', validators=[DataRequired()])
    submit = SubmitField(label='Please Submit your Review')
