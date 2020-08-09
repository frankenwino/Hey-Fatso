from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, FloatField
from wtforms.validators import DataRequired, Optional, InputRequired


class TDCEForm(FlaskForm):
    activity_levels = [
        ('1', 'Sedentary (little or no exercise)'),
        ('2', 'Lightly active (light exercise or sports 1-3 days/week)'),
        ('3', 'Moderately active (moderate exercise 3-5 days/week)'),
        ('4', 'Very active (hard exercise 6-7 days/week)'),
        ('5', 'Super active (very hard exercise and a physical job)')
        ]

    sex = SelectField('Sex', choices=[('m', 'Male'), ('f', 'Female')], validators=[InputRequired()])
    weight_kg = FloatField('Weight in kg',validators=[DataRequired()])
    height_cm = FloatField('Height in cm',validators=[DataRequired()])
    age = FloatField('Age',validators=[DataRequired()])
    activity_level = SelectField('Activity Level', choices=activity_levels,  validators=[InputRequired()])
    body_fat_percentage = FloatField('Body Fat Percentage (Optional)', validators=[Optional()])
    calculate = SubmitField('Calculate')


class IdealBodyWeightForm(FlaskForm):
    sex = SelectField('Sex', choices=[('m', 'Male'), ('f', 'Female')], validators=[InputRequired()])
    height_cm = FloatField('Height in cm',validators=[DataRequired()])
    calculate = SubmitField('Calculate')


class BodyFatForm(FlaskForm):
    sex = SelectField('Sex', choices=[('m', 'Male'), ('f', 'Female')], validators=[InputRequired()])
    height_cm = FloatField('Height in cm',validators=[DataRequired()])
    weight_kg = FloatField('Weight in kg',validators=[DataRequired()])
    waist_cm = FloatField('Waist circumference in cm',validators=[DataRequired()])
    neck_cm = FloatField('Neck circumference in cm',validators=[DataRequired()])
    hip_cm = FloatField('Hip circumference in cm (Females only)',validators=[DataRequired()])
    calculate = SubmitField('Calculate')


class BodyFatFormTabs(FlaskForm):
    age = IntegerField('Age',validators=[DataRequired()])
    height_cm = FloatField('Height in cm',validators=[DataRequired()])
    weight_kg = FloatField('Weight in kg',validators=[DataRequired()])
    waist_cm = FloatField('Waist circumference in cm',validators=[DataRequired()])
    neck_cm = FloatField('Neck circumference in cm',validators=[DataRequired()])
    calculate = SubmitField('Calculate')


class BodyFatFormMale(BodyFatFormTabs):
    sex = 'm'

class BodyFatFormFemale(BodyFatFormTabs):
    sex = 'f'
    hip_cm = FloatField('Hip circumference in cm',validators=[DataRequired()])
