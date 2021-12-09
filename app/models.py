from datetime import datetime
from hashlib import md5
import json
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db, login
from app.search import add_to_index, remove_from_index, query_index
import os


class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)), total

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)


db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)


followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

followers2 = db.Table(
    'followers2',
    db.Column('follower2_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed2_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    city = db.Column(db.String(64), index=True)
    state = db.Column(db.String(64), index=True)
    faves = db.Column(db.String(256), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    film1 = db.Column(db.Integer)
    film2 = db.Column(db.Integer)
    film3 = db.Column(db.Integer)
    film4 = db.Column(db.Integer)
    film5 = db.Column(db.Integer)
    film6 = db.Column(db.Integer)
    film7 = db.Column(db.Integer)
    film8 = db.Column(db.Integer)
    film9 = db.Column(db.Integer)
    film10 = db.Column(db.Integer)
    film11 = db.Column(db.Integer)
    film12 = db.Column(db.Integer)
    film13 = db.Column(db.Integer)
    film14 = db.Column(db.Integer)
    film15 = db.Column(db.Integer)
    film16 = db.Column(db.Integer)
    film17 = db.Column(db.Integer)
    film18 = db.Column(db.Integer)
    film19 = db.Column(db.Integer)
    film20 = db.Column(db.Integer)
    film21 = db.Column(db.Integer)
    film22 = db.Column(db.Integer)
    film23 = db.Column(db.Integer)
    film24 = db.Column(db.Integer)
    film25 = db.Column(db.Integer)
    film26 = db.Column(db.Integer)
    film27 = db.Column(db.Integer)
    film28 = db.Column(db.Integer)
    film29 = db.Column(db.Integer)
    film30 = db.Column(db.Integer)
    film31 = db.Column(db.Integer)
    film32 = db.Column(db.Integer)
    film33 = db.Column(db.Integer)
    film34 = db.Column(db.Integer)
    film35 = db.Column(db.Integer)
    film36 = db.Column(db.Integer)
    film37 = db.Column(db.Integer)
    film38 = db.Column(db.Integer)
    film39 = db.Column(db.Integer)
    film40 = db.Column(db.Integer)
    film41 = db.Column(db.Integer)
    film42 = db.Column(db.Integer)
    film43 = db.Column(db.Integer)
    film44 = db.Column(db.Integer)
    film45 = db.Column(db.Integer)
    film46 = db.Column(db.Integer)
    film47 = db.Column(db.Integer)
    film48 = db.Column(db.Integer)
    film49 = db.Column(db.Integer)
    film50 = db.Column(db.Integer)
    film51 = db.Column(db.Integer)
    film52 = db.Column(db.Integer)
    film53 = db.Column(db.Integer)
    film54 = db.Column(db.Integer)
    film55 = db.Column(db.Integer)
    film56 = db.Column(db.Integer)
    film57 = db.Column(db.Integer)
    film58 = db.Column(db.Integer)
    film59 = db.Column(db.Integer)
    film60 = db.Column(db.Integer)
    film61 = db.Column(db.Integer)
    film62 = db.Column(db.Integer)
    film63 = db.Column(db.Integer)
    film64 = db.Column(db.Integer)
    film65 = db.Column(db.Integer)
    film66 = db.Column(db.Integer)
    film67 = db.Column(db.Integer)
    film68 = db.Column(db.Integer)
    film69 = db.Column(db.Integer)
    film70 = db.Column(db.Integer)
    film71 = db.Column(db.Integer)
    film72 = db.Column(db.Integer)
    film73 = db.Column(db.Integer)
    film74 = db.Column(db.Integer)
    film75 = db.Column(db.Integer)
    film76 = db.Column(db.Integer)
    film77 = db.Column(db.Integer)
    film78 = db.Column(db.Integer)
    film79 = db.Column(db.Integer)
    film80 = db.Column(db.Integer)
    film81 = db.Column(db.Integer)
    film82 = db.Column(db.Integer)
    film83 = db.Column(db.Integer)
    film84 = db.Column(db.Integer)
    film85 = db.Column(db.Integer)
    film86 = db.Column(db.Integer)
    film87 = db.Column(db.Integer)
    film88 = db.Column(db.Integer)
    film89 = db.Column(db.Integer)
    film90 = db.Column(db.Integer)
    film91 = db.Column(db.Integer)
    film92 = db.Column(db.Integer)
    film93 = db.Column(db.Integer)
    film94 = db.Column(db.Integer)
    film95 = db.Column(db.Integer)
    film96 = db.Column(db.Integer)
    film97 = db.Column(db.Integer)
    film98 = db.Column(db.Integer)
    film99 = db.Column(db.Integer)
    film100 = db.Column(db.Integer)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    subposts = db.relationship('Subpost', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(1024))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    followed2 = db.relationship(
        'User', secondary=followers2,
        primaryjoin=(followers2.c.follower2_id == id),
        secondaryjoin=(followers2.c.followed2_id == id),
        backref=db.backref('followers2', lazy='dynamic'), lazy='dynamic')
    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)
    notifications = db.relationship('Notification', backref='user',
                                    lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def follow2(self, user):
        if not self.is_following2(user):
            self.followed2.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def unfollow2(self, user):
        if self.is_following2(user):
            self.followed2.remove(user)

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def is_following2(self, user):
        return self.followed2.filter(followers2.c.followed2_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def followed2_posts(self):
        followed2 = Post.query.join(followers2, (followers2.c.followed2_id == Post.user_id)).filter(followers2.c.follower2_id == self.id)
        return followed2.order_by(Post.timestamp.desc())

    def all_posts(self):
        followed = Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        followed2 = Post.query.join(followers2, (followers2.c.followed2_id == Post.user_id)).filter(followers2.c.follower2_id == self.id)
        return followed.union(followed2).union(own).order_by(Post.timestamp.desc())

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()

    def add_notification(self, name, data):
        self.notifications.filter_by(name=name).delete()
        n = Notification(name=name, payload_json=json.dumps(data), user=self)
        db.session.add(n)
        return n

    def moofinity(self, current_user):
        try:
            v = abs(current_user.film1 - self.film1) + abs(current_user.film2 - self.film2) + \
            abs(current_user.film3 - self.film3) + abs(current_user.film4 - self.film4) + \
            abs(current_user.film5 - self.film5) + abs(current_user.film6 - self.film6) + \
            abs(current_user.film7 - self.film7) + abs(current_user.film8 - self.film8) + \
            abs(current_user.film9 - self.film9) + abs(current_user.film10 - self.film10) + \
            abs(current_user.film11 - self.film11) + abs(current_user.film12 - self.film12) + \
            abs(current_user.film13 - self.film13) + abs(current_user.film14 - self.film14) + \
            abs(current_user.film15 - self.film15) + abs(current_user.film16 - self.film16) + \
            abs(current_user.film17 - self.film17) + abs(current_user.film18 - self.film18) + \
            abs(current_user.film19 - self.film19) + abs(current_user.film20 - self.film20) + \
            abs(current_user.film21 - self.film21) + abs(current_user.film22 - self.film22) + \
            abs(current_user.film23 - self.film23) + abs(current_user.film24 - self.film24) + \
            abs(current_user.film25 - self.film25) + abs(current_user.film26 - self.film26) + \
            abs(current_user.film27 - self.film27) + abs(current_user.film28 - self.film28) + \
            abs(current_user.film29 - self.film29) + abs(current_user.film30 - self.film30) + \
            abs(current_user.film31 - self.film31) + abs(current_user.film32 - self.film32) + \
            abs(current_user.film33 - self.film33) + abs(current_user.film34 - self.film34) + \
            abs(current_user.film35 - self.film35) + abs(current_user.film36 - self.film36) + \
            abs(current_user.film37 - self.film37) + abs(current_user.film38 - self.film38) + \
            abs(current_user.film39 - self.film39) + abs(current_user.film40 - self.film40) + \
            abs(current_user.film41 - self.film41) + abs(current_user.film42 - self.film42) + \
            abs(current_user.film43 - self.film43) + abs(current_user.film44 - self.film44) + \
            abs(current_user.film45 - self.film45) + abs(current_user.film46 - self.film46) + \
            abs(current_user.film47 - self.film47) + abs(current_user.film48 - self.film48) + \
            abs(current_user.film49 - self.film49) + abs(current_user.film50 - self.film50) + \
            abs(current_user.film51 - self.film51) + abs(current_user.film52 - self.film52) + \
            abs(current_user.film53 - self.film53) + abs(current_user.film54 - self.film54) + \
            abs(current_user.film55 - self.film55) + abs(current_user.film56 - self.film56) + \
            abs(current_user.film57 - self.film57) + abs(current_user.film58 - self.film58) + \
            abs(current_user.film59 - self.film59) + abs(current_user.film60 - self.film60) + \
            abs(current_user.film61 - self.film61) + abs(current_user.film62 - self.film62) + \
            abs(current_user.film63 - self.film63) + abs(current_user.film64 - self.film64) + \
            abs(current_user.film65 - self.film65) + abs(current_user.film66 - self.film66) + \
            abs(current_user.film67 - self.film67) + abs(current_user.film68 - self.film68) + \
            abs(current_user.film69 - self.film69) + abs(current_user.film70 - self.film70) + \
            abs(current_user.film71 - self.film71) + abs(current_user.film72 - self.film72) + \
            abs(current_user.film73 - self.film73) + abs(current_user.film74 - self.film74) + \
            abs(current_user.film75 - self.film75) + abs(current_user.film76 - self.film76) + \
            abs(current_user.film77 - self.film77) + abs(current_user.film78 - self.film78) + \
            abs(current_user.film79 - self.film79) + abs(current_user.film80 - self.film80) + \
            abs(current_user.film81 - self.film81) + abs(current_user.film82 - self.film82) + \
            abs(current_user.film83 - self.film83) + abs(current_user.film84 - self.film84) + \
            abs(current_user.film85 - self.film85) + abs(current_user.film86 - self.film86) + \
            abs(current_user.film87 - self.film87) + abs(current_user.film88 - self.film88) + \
            abs(current_user.film89 - self.film89) + abs(current_user.film90 - self.film90) + \
            abs(current_user.film91 - self.film91) + abs(current_user.film92 - self.film92) + \
            abs(current_user.film93 - self.film93) + abs(current_user.film94 - self.film94) + \
            abs(current_user.film95 - self.film95) + abs(current_user.film96 - self.film96) + \
            abs(current_user.film97 - self.film97) + abs(current_user.film98 - self.film98) + \
            abs(current_user.film99 - self.film99) + abs(current_user.film100 - self.film100)
            n = abs(v - 800) / 800
            return "{:.0%}".format(n)
        except:
            return "  :(  "

    def ppic_exists1(self):
            path = 'C:\\Users\\hanco\\moovietribe\\app\\static\\ppics\\' + str(self.id) + '.jpg'
            return os.path.exists(path)

    def ppic_exists2(self):
            path = 'C:\\Users\\hanco\\moovietribe\\app\\static\\ppics\\' + str(self.id) + '.png'
            return os.path.exists(path)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(SearchableMixin, db.Model):
    __searchable__ = ['body']
    id = db.Column(db.Integer, primary_key=True)
    moovie_id = db.Column(db.Integer, db.ForeignKey('moovie.id'))
    mootitle = db.Column(db.String(140))
    rating = db.Column(db.Integer)
    body = db.Column(db.String(280))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    language = db.Column(db.String(5))
    chat_count = db.Column(db.Integer)

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Subpost(SearchableMixin, db.Model):
    __searchable__ = ['body']
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    language = db.Column(db.String(5))
    originalpost_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Subpost {}>'.format(self.body)

class Moovie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mootitle = db.Column(db.String(140))
    posts = db.relationship('Post', backref='title', lazy='dynamic')
    imdb = db.Column(db.String(16))

    def poster_exists1(self):
        path = 'C:\\Users\\hanco\\moovietribe\\app\\static\\posters\\' + str(self.id) + '.jpg'
        return os.path.exists(path)

    def poster_exists2(self):
        path = 'C:\\Users\\hanco\\moovietribe\\app\\static\\posters\\' + str(self.id) + '.png'
        return os.path.exists(path)

    def moovie_posts(self):
        moovieposts = Post.query.filter_by(moovie_id=self.id)
        return moovieposts.order_by(Post.timestamp.desc())

    def __repr__(self):
        return '<Moovie {}>'.format(self.moovie)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    prevmsg_id = db.Column(db.Integer)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    new = db.Column(db.Integer)

    def __repr__(self):
        return '<Message {}>'.format(self.body)


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.Float, index=True, default=time)
    payload_json = db.Column(db.Text)

    def get_data(self):
        return json.loads(str(self.payload_json))
