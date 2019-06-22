from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class EditProfileForm2(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    film1 = RadioField('12 Angry Men (1957)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10<br>'),('6','Yeah'),('3','Meh')])
    film2 = RadioField('2001: a Space Oddysey (1968)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film3 = RadioField('28 Days Later (2002)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film4 = RadioField('A Star is Born (2018)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film5 = RadioField('Adaptation (2002)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film6 = RadioField('All About Eve (1950)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film7 = RadioField('All That Jazz (1979)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film8 = RadioField('An American Werewolf in London (1981)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp'),('6','Yeah'),('3','Meh')])
    film9 = RadioField('Annie Hall (1977)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film10 = RadioField('Blackhawk Down (2001)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film11 = RadioField('Black Narcissus (1947)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film12 = RadioField('Black Panther (2018)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film13 = RadioField('Boys Don\'t Cry (1999)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film14 = RadioField('Braveheart (1995)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film15 = RadioField('Brazil (1985)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film16 = RadioField('Captain America: The Winter Soldier (2014)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film17 = RadioField('Casablanca (1942)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film18 = RadioField('City of God (2002)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film19 = RadioField('Crouching Tiger Hidden Dragon (2000)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 -OR-'),('6','Yeah'),('3','Meh')])
    film20 = RadioField('Die Hard (1988)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 -OR-'),('6','Yeah'),('3','Meh')])
    film21 = RadioField('District 9 (2009)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 -OR-'),('6','Yeah'),('3','Meh')])
    film22 = RadioField('Do the Right Thing (1989)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film23 = RadioField('Doctor Zhivago (1965)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film24 = RadioField('Double Indemnity (1944)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film25 = RadioField('Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb )1955)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film26 = RadioField('Evita (1996)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film27 = RadioField('Ex Machina (2014)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film28 = RadioField('Farewell My Concubine (1993)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film29 = RadioField('Fargo (1996)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film30 = RadioField('Faster Pussycat, Kill Kill! (1965)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film31 = RadioField('Field of Dreams (1989)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film32 = RadioField('Final Destination (2000)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film33 = RadioField('Frozen (2013)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film34 = RadioField('Get Him to the Greek (2010)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film35 = RadioField('Gladiator (2000)', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10'),('6','Yeah'),('3','Meh')])
    film36 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film37 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film38 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film39 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film40 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film41 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film42 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film43 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film44 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film45 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film46 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film47 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film48 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film49 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film50 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film51 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film52 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film53 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film54 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film55 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film56 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film57 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film58 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film59 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film60 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film61 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film62 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film63 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film64 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film65 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film66 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film67 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film68 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film69 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film70 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film71 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film72 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film73 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film74 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film75 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film76 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film77 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film78 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film79 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film80 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film81 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film82 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film83 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film84 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film85 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film86 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film87 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film88 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film89 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film90 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film91 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film92 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film93 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film94 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film95 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film96 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film97 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film98 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film99 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    film100 = RadioField('x', choices = [('1','1'),('2','2'),('4','3'),('5','4'),('7','5'),('8','6'),('9','7'),('10','8'),('11','9'),('12','10 &nbsp &nbsp -OR- &nbsp &nbsp'),('6','Yeah'),('3','Meh')])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm2, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class EditProfileForm3(FlaskForm):
    imdb = TextAreaField(_l('imdb'),
                             validators=[Length(min=0, max=140)])
    poster = TextAreaField(_l('poster'),
                             validators=[Length(min=0, max=280)])
    submit = SubmitField(_l('Submit'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)


class MessageForm(FlaskForm):
    message = TextAreaField(_l('Message'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))
