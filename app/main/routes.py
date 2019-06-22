from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
from app.main.forms import EditProfileForm, EditProfileForm2, EditProfileForm3, PostForm, SearchForm, MessageForm
from app.models import User, Post, Message, Notification, Moovies
from app.translate import translate
from app.main import bp


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        g.search_form = SearchForm()
    g.locale = str(get_locale())


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        language = guess_language(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, author=current_user,
                    language=language)
        db.session.add(post)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.index'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title=_('Home'), form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@bp.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title=_('Explore'),
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.user', username=user.username,
                       page=posts.next_num) if posts.has_next else None
    prev_url = url_for('main.user', username=user.username,
                       page=posts.prev_num) if posts.has_prev else None
    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url)


@bp.route('/user/<username>/popup')
@login_required
def user_popup(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user_popup.html', user=user)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=_('Edit Profile'),
                           form=form)


@bp.route('/edit_profile2', methods=['GET', 'POST'])
@login_required
def edit_profile2():
    form = EditProfileForm2(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.film1 = form.film1.data
        current_user.film2 = form.film2.data
        current_user.film3 = form.film3.data
        current_user.film4 = form.film4.data
        current_user.film5 = form.film5.data
        current_user.film6 = form.film6.data
        current_user.film7 = form.film7.data
        current_user.film8 = form.film8.data
        current_user.film9 = form.film9.data
        current_user.film10 = form.film10.data
        current_user.film11 = form.film11.data
        current_user.film12 = form.film12.data
        current_user.film13 = form.film13.data
        current_user.film14 = form.film14.data
        current_user.film15 = form.film15.data
        current_user.film16 = form.film16.data
        current_user.film17 = form.film17.data
        current_user.film18 = form.film18.data
        current_user.film19 = form.film19.data
        current_user.film20 = form.film20.data
        current_user.film21 = form.film21.data
        current_user.film22 = form.film22.data
        current_user.film23 = form.film23.data
        current_user.film24 = form.film24.data
        current_user.film25 = form.film25.data
        current_user.film26 = form.film26.data
        current_user.film27 = form.film27.data
        current_user.film28 = form.film28.data
        current_user.film29 = form.film29.data
        current_user.film30 = form.film30.data
        current_user.film31 = form.film31.data
        current_user.film32 = form.film32.data
        current_user.film33 = form.film33.data
        current_user.film34 = form.film34.data
        current_user.film35 = form.film35.data
        current_user.film36 = form.film36.data
        current_user.film37 = form.film37.data
        current_user.film38 = form.film38.data
        current_user.film39 = form.film39.data
        current_user.film40 = form.film40.data
        current_user.film41 = form.film41.data
        current_user.film42 = form.film42.data
        current_user.film43 = form.film43.data
        current_user.film44 = form.film44.data
        current_user.film45 = form.film45.data
        current_user.film46 = form.film46.data
        current_user.film47 = form.film47.data
        current_user.film48 = form.film48.data
        current_user.film49 = form.film49.data
        current_user.film50 = form.film50.data
        current_user.film51 = form.film51.data
        current_user.film52 = form.film52.data
        current_user.film53 = form.film53.data
        current_user.film54 = form.film54.data
        current_user.film55 = form.film55.data
        current_user.film56 = form.film56.data
        current_user.film57 = form.film57.data
        current_user.film58 = form.film58.data
        current_user.film59 = form.film59.data
        current_user.film60 = form.film60.data
        current_user.film61 = form.film61.data
        current_user.film62 = form.film62.data
        current_user.film63 = form.film63.data
        current_user.film64 = form.film64.data
        current_user.film65 = form.film65.data
        current_user.film66 = form.film66.data
        current_user.film67 = form.film67.data
        current_user.film68 = form.film68.data
        current_user.film69 = form.film69.data
        current_user.film70 = form.film70.data
        current_user.film71 = form.film71.data
        current_user.film72 = form.film72.data
        current_user.film73 = form.film73.data
        current_user.film74 = form.film74.data
        current_user.film75 = form.film75.data
        current_user.film76 = form.film76.data
        current_user.film77 = form.film77.data
        current_user.film78 = form.film78.data
        current_user.film79 = form.film79.data
        current_user.film80 = form.film80.data
        current_user.film81 = form.film81.data
        current_user.film82 = form.film82.data
        current_user.film83 = form.film83.data
        current_user.film84 = form.film84.data
        current_user.film85 = form.film85.data
        current_user.film86 = form.film86.data
        current_user.film87 = form.film87.data
        current_user.film88 = form.film88.data
        current_user.film89 = form.film89.data
        current_user.film90 = form.film90.data
        current_user.film91 = form.film91.data
        current_user.film92 = form.film92.data
        current_user.film93 = form.film93.data
        current_user.film94 = form.film94.data
        current_user.film95 = form.film95.data
        current_user.film96 = form.film96.data
        current_user.film97 = form.film97.data
        current_user.film98 = form.film98.data
        current_user.film99 = form.film99.data
        current_user.film100 = form.film100.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.film1.data = current_user.film1
        form.film2.data = current_user.film2
        form.film3.data = current_user.film3
        form.film4.data = current_user.film4
        form.film5.data = current_user.film5
        form.film6.data = current_user.film6
        form.film7.data = current_user.film7
        form.film8.data = current_user.film8
        form.film9.data = current_user.film9
        form.film10.data = current_user.film10
        form.film11.data = current_user.film11
        form.film12.data = current_user.film12
        form.film13.data = current_user.film13
        form.film14.data = current_user.film14
        form.film15.data = current_user.film15
        form.film16.data = current_user.film16
        form.film17.data = current_user.film17
        form.film18.data = current_user.film18
        form.film19.data = current_user.film19
        form.film20.data = current_user.film20
        form.film21.data = current_user.film21
        form.film22.data = current_user.film22
        form.film23.data = current_user.film23
        form.film24.data = current_user.film24
        form.film25.data = current_user.film25
        form.film26.data = current_user.film26
        form.film27.data = current_user.film27
        form.film28.data = current_user.film28
        form.film29.data = current_user.film29
        form.film30.data = current_user.film30
        form.film31.data = current_user.film31
        form.film32.data = current_user.film32
        form.film33.data = current_user.film33
        form.film34.data = current_user.film34
        form.film35.data = current_user.film35
        form.film36.data = current_user.film36
        form.film37.data = current_user.film37
        form.film38.data = current_user.film38
        form.film39.data = current_user.film39
        form.film40.data = current_user.film40
        form.film41.data = current_user.film41
        form.film42.data = current_user.film42
        form.film43.data = current_user.film43
        form.film44.data = current_user.film44
        form.film45.data = current_user.film45
        form.film46.data = current_user.film46
        form.film47.data = current_user.film47
        form.film48.data = current_user.film48
        form.film49.data = current_user.film49
        form.film50.data = current_user.film50
        form.film51.data = current_user.film51
        form.film52.data = current_user.film52
        form.film53.data = current_user.film53
        form.film54.data = current_user.film54
        form.film55.data = current_user.film55
        form.film56.data = current_user.film56
        form.film57.data = current_user.film57
        form.film58.data = current_user.film58
        form.film59.data = current_user.film59
        form.film60.data = current_user.film60
        form.film61.data = current_user.film61
        form.film62.data = current_user.film62
        form.film63.data = current_user.film63
        form.film64.data = current_user.film64
        form.film65.data = current_user.film65
        form.film66.data = current_user.film66
        form.film67.data = current_user.film67
        form.film68.data = current_user.film68
        form.film69.data = current_user.film69
        form.film70.data = current_user.film70
        form.film71.data = current_user.film71
        form.film72.data = current_user.film72
        form.film73.data = current_user.film73
        form.film74.data = current_user.film74
        form.film75.data = current_user.film75
        form.film76.data = current_user.film76
        form.film77.data = current_user.film77
        form.film78.data = current_user.film78
        form.film79.data = current_user.film79
        form.film80.data = current_user.film80
        form.film81.data = current_user.film81
        form.film82.data = current_user.film82
        form.film83.data = current_user.film83
        form.film84.data = current_user.film84
        form.film85.data = current_user.film85
        form.film86.data = current_user.film86
        form.film87.data = current_user.film87
        form.film88.data = current_user.film88
        form.film89.data = current_user.film89
        form.film90.data = current_user.film90
        form.film91.data = current_user.film91
        form.film92.data = current_user.film92
        form.film93.data = current_user.film93
        form.film94.data = current_user.film94
        form.film95.data = current_user.film95
        form.film96.data = current_user.film96
        form.film97.data = current_user.film97
        form.film98.data = current_user.film98
        form.film99.data = current_user.film99
        form.film100.data = current_user.film100
    return render_template('edit_profile2.html', title=_('Edit Movies'),
                           form=form)


@bp.route('/edit_profile3', methods=['GET', 'POST'])
@login_required
def edit_profile3():
    form = EditProfileForm3()
    if form.validate_on_submit():
        moovies = Moovies(imdb=form.imdb.data, poster=form.poster.data)
        db.session.add(moovies)
        db.session.commit()
        flash('Moovie added!')
        return redirect(url_for('main.edit_profile3'))
    return render_template('edit_profile3.html', title=_('Edit Profile'),
                           form=form)


@bp.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash(_('You cannot follow yourself!'))
        return redirect(url_for('main.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash(_('You are following %(username)s!', username=username))
    return redirect(url_for('main.user', username=username))


@bp.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash(_('You cannot unfollow yourself!'))
        return redirect(url_for('main.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash(_('You are not following %(username)s.', username=username))
    return redirect(url_for('main.user', username=username))


@bp.route('/translate', methods=['POST'])
@login_required
def translate_text():
    return jsonify({'text': translate(request.form['text'],
                                      request.form['source_language'],
                                      request.form['dest_language'])})


@bp.route('/search')
@login_required
def search():
    if not g.search_form.validate():
        return redirect(url_for('main.explore'))
    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(g.search_form.q.data, page,
                               current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('search.html', title=_('Search'), posts=posts,
                           next_url=next_url, prev_url=prev_url)


@bp.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
    user = User.query.filter_by(username=recipient).first_or_404()
    form = MessageForm()
    if form.validate_on_submit():
        msg = Message(author=current_user, recipient=user,
                      body=form.message.data)
        db.session.add(msg)
        user.add_notification('unread_message_count', user.new_messages())
        db.session.commit()
        flash(_('Your message has been sent.'))
        return redirect(url_for('main.user', username=recipient))
    return render_template('send_message.html', title=_('Send Message'),
                           form=form, recipient=recipient)


@bp.route('/messages')
@login_required
def messages():
    current_user.last_message_read_time = datetime.utcnow()
    current_user.add_notification('unread_message_count', 0)
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    messages = current_user.messages_received.order_by(
        Message.timestamp.desc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.messages', page=messages.next_num) \
        if messages.has_next else None
    prev_url = url_for('main.messages', page=messages.prev_num) \
        if messages.has_prev else None
    return render_template('messages.html', messages=messages.items,
                           next_url=next_url, prev_url=prev_url)


@bp.route('/export_posts')
@login_required
def export_posts():
    if current_user.get_task_in_progress('export_posts'):
        flash(_('An export task is currently in progress'))
    else:
        current_user.launch_task('export_posts', _('Exporting posts...'))
        db.session.commit()
    return redirect(url_for('main.user', username=current_user.username))


@bp.route('/notifications')
@login_required
def notifications():
    since = request.args.get('since', 0.0, type=float)
    notifications = current_user.notifications.filter(
        Notification.timestamp > since).order_by(Notification.timestamp.asc())
    return jsonify([{
        'name': n.name,
        'data': n.get_data(),
        'timestamp': n.timestamp
    } for n in notifications])
