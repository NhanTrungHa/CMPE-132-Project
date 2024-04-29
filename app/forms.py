from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    securityQuestion = StringField('SecurityQuestion', validators=[DataRequired()])
    securityQuestionAnswer = PasswordField('SecurityQuestionAnswer', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me', validators=[DataRequired()])
    submit = SubmitField('Login')


class forgotPassForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Confirm')


class changePassForm(FlaskForm):
    securityQuestionAnswer = PasswordField('SecurityQuestionAnswer', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Confirm')


class updateForm(FlaskForm):
    firstname = StringField('firstname')
    lastname = StringField('lastname')
    username = StringField('username')
    role = SelectField('Role', choices=[
        ('registered_user', 'Registered User'),
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('professor', 'Professor'),
        ('student', 'Student')
    ])
    email = StringField('Email', validators=[Email()])
    password1 = PasswordField('Password')
    password2 = PasswordField('Confirm Password', validators=[EqualTo('password1')])
    securityQuestion = StringField('SecurityQuestion')
    securityQuestionAnswer = PasswordField('SecurityQuestionAnswer')
    submit = SubmitField('Submit')


class CreateItemForm(FlaskForm):
    product_name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    condition = SelectField('Item Condition',
                            choices=[('New', 'New'),
                                     ('Used - Like New', 'Used - Like New'),
                                     ('Used - Good', 'Used - Good'),
                                     ('Used - Acceptable', 'Used - Acceptable')],
                            validators=[DataRequired()])
    category = SelectField('Category',
                           choices=[('0', 'Horror'),
                                    ('1', 'Romance'),
                                    ('2', 'Mystery'),
                                    ('3', 'Thriller'),
                                    ('4', 'Science Fiction'),
                                    ('5', 'Fantasy'),
                                    ('6', 'Biography'),
                                    ('7', 'Historical Fiction'),
                                    ('8', 'Literary Fiction'),
                                    ('9', 'Young Adult'),
                                    ('10', 'Children\'s'),
                                    ('11', 'Self-Help'),
                                    ('12', 'Reference'),
                                    ('13', 'Cookbooks'),
                                    ('14', 'Poetry'),
                                    ('15', 'Travel'),
                                    ('16', 'Religion'),
                                    ('17', 'Art & Photography')],
                           validators=[DataRequired()])
    submit = SubmitField('Create Item')


class DeleteItemForm(FlaskForm):
    delete = SubmitField('Delete Item')


class ViewCategoryForm(FlaskForm):
    category = SelectField('Category',
                           choices=[('18', 'All Items'),
                                    ('0', 'Horror'),
                                    ('1', 'Romance'),
                                    ('2', 'Mystery'),
                                    ('3', 'Thriller'),
                                    ('4', 'Science Fiction'),
                                    ('5', 'Fantasy'),
                                    ('6', 'Biography'),
                                    ('7', 'Historical Fiction'),
                                    ('8', 'Literary Fiction'),
                                    ('9', 'Young Adult'),
                                    ('10', 'Children\'s'),
                                    ('11', 'Self-Help'),
                                    ('12', 'Reference'),
                                    ('13', 'Cookbooks'),
                                    ('14', 'Poetry'),
                                    ('15', 'Travel'),
                                    ('16', 'Religion'),
                                    ('17', 'Art & Photography')],
                           validators=[DataRequired()])
    submit = SubmitField('Display Items in Category')


class CreateCheckoutForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    payment = StringField('Credit or Debit Card Number', validators=[DataRequired()])
    cvv = StringField('CVV',
                      validators=[DataRequired(), Length(max=3, message='Length must be %(max)d number characters')])
    submit = SubmitField('Checkout From Cart')
