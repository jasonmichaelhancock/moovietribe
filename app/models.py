import base64
from datetime import datetime, timedelta
from hashlib import md5
import json
import os
from time import time
from flask import current_app, url_for
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import redis
import rq
from app import db, login
from app.search import add_to_index, remove_from_index, query_index


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


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data


followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
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
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)
    notifications = db.relationship('Notification', backref='user',
                                    lazy='dynamic')
    tasks = db.relationship('Task', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

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

    def launch_task(self, name, description, *args, **kwargs):
        rq_job = current_app.task_queue.enqueue('app.tasks.' + name, self.id,
                                                *args, **kwargs)
        task = Task(id=rq_job.get_id(), name=name, description=description,
                    user=self)
        db.session.add(task)
        return task

    def get_tasks_in_progress(self):
        return Task.query.filter_by(user=self, complete=False).all()

    def get_task_in_progress(self, name):
        return Task.query.filter_by(name=name, user=self,
                                    complete=False).first()

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            'last_seen': self.last_seen.isoformat() + 'Z',
            'about_me': self.about_me,
            'film1': self.film1,
            'film2': self.film2,
            'film3': self.film3,
            'film4': self.film4,
            'film5': self.film5,
            'film6': self.film6,
            'film7': self.film7,
            'film8': self.film8,
            'film9': self.film9,
            'film10': self.film10,
            'film11': self.film11,
            'film12': self.film12,
            'film13': self.film13,
            'film14': self.film14,
            'film15': self.film15,
            'film16': self.film16,
            'film17': self.film17,
            'film18': self.film18,
            'film19': self.film19,
            'film20': self.film20,
            'film21': self.film21,
            'film22': self.film22,
            'film23': self.film23,
            'film24': self.film24,
            'film25': self.film25,
            'film26': self.film26,
            'film27': self.film27,
            'film28': self.film28,
            'film29': self.film29,
            'film30': self.film30,
            'film31': self.film31,
            'film32': self.film32,
            'film33': self.film33,
            'film34': self.film34,
            'film35': self.film35,
            'film36': self.film36,
            'film37': self.film37,
            'film38': self.film38,
            'film39': self.film39,
            'film40': self.film40,
            'film41': self.film41,
            'film42': self.film42,
            'film43': self.film43,
            'film44': self.film44,
            'film45': self.film45,
            'film46': self.film46,
            'film47': self.film47,
            'film48': self.film48,
            'film49': self.film49,
            'film50': self.film50,
            'film51': self.film51,
            'film52': self.film52,
            'film53': self.film53,
            'film54': self.film54,
            'film55': self.film55,
            'film56': self.film56,
            'film57': self.film57,
            'film58': self.film58,
            'film59': self.film59,
            'film60': self.film60,
            'film61': self.film61,
            'film62': self.film62,
            'film63': self.film63,
            'film64': self.film64,
            'film65': self.film65,
            'film66': self.film66,
            'film67': self.film67,
            'film68': self.film68,
            'film69': self.film69,
            'film70': self.film70,
            'film71': self.film71,
            'film72': self.film72,
            'film73': self.film73,
            'film74': self.film74,
            'film75': self.film75,
            'film76': self.film76,
            'film77': self.film77,
            'film78': self.film78,
            'film79': self.film79,
            'film80': self.film80,
            'film81': self.film81,
            'film82': self.film82,
            'film83': self.film83,
            'film84': self.film84,
            'film85': self.film85,
            'film86': self.film86,
            'film87': self.film87,
            'film88': self.film88,
            'film89': self.film89,
            'film90': self.film90,
            'film91': self.film91,
            'film92': self.film92,
            'film93': self.film93,
            'film94': self.film94,
            'film95': self.film95,
            'film96': self.film96,
            'film97': self.film97,
            'film98': self.film98,
            'film99': self.film99,
            'film100': self.film100,
            'post_count': self.posts.count(),
            'follower_count': self.followers.count(),
            'followed_count': self.followed.count(),
            '_links': {
                'self': url_for('api.get_user', id=self.id),
                'followers': url_for('api.get_followers', id=self.id),
                'followed': url_for('api.get_followed', id=self.id),
                'avatar': self.avatar(128)
            }
        }
        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'about_me', 'film1', 'film2', 'film3', 'film4', 'film5', 'film6', 'film7', 'film8', 'film9', 'film10', 'film11', 'film12', 'film13', 'film14', 'film15', 'film16', 'film17', 'film18', 'film19', 'film20', 'film21', 'film22', 'film23', 'film24', 'film25', 'film26', 'f\
        ilm27', 'film28', 'film29', 'film30', 'film31', 'film32', 'film33', 'film34', 'film35', 'film36', 'f\
        ilm37', 'film38', 'film39', 'film40', 'film41', 'film32', 'film43', 'film44', 'film45', 'film46', 'f\
        ilm47', 'film48', 'film49', 'film50', 'film51', 'film32', 'film53', 'film54', 'film55', 'film56', 'f\
        ilm57', 'film58', 'film59', 'film60', 'film61', 'film32', 'film63', 'film64', 'film65', 'film66', 'f\
        ilm67', 'film68', 'film69', 'film70', 'film71', 'film32', 'film73', 'film74', 'film75', 'film76', 'f\
        ilm77', 'film78', 'film79', 'film80', 'film81', 'film32', 'film83', 'film84', 'film85', 'film86', 'f\
        ilm87', 'film88', 'film89', 'film90', 'film91', 'film32', 'film93', 'film94', 'film95', 'film96', 'f\
        ilm97', 'film98', 'film99', 'film100']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(SearchableMixin, db.Model):
    __searchable__ = ['body']
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    language = db.Column(db.String(5))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Moovies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imdb = db.Column(db.String(140))
    poster = db.Column(db.String(280))

    def __repr__(self):
        return '<Moovies {}>'.format(self.body)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

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


class Task(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(128), index=True)
    description = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    complete = db.Column(db.Boolean, default=False)

    def get_rq_job(self):
        try:
            rq_job = rq.job.Job.fetch(self.id, connection=current_app.redis)
        except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
            return None
        return rq_job

    def get_progress(self):
        job = self.get_rq_job()
        return job.meta.get('progress', 0) if job is not None else 100
