post = Post.query.filter_by(user_id=current_user.id, moovie_id=91).first()
if post is not None:
    post.rating = form.film91.data
else:
    post = Post(author=current_user, moovie_id=91, rating=int(form.film91.data))
    db.session.add(post)
post = Post.query.filter_by(user_id=current_user.id, moovie_id=92).first()
if post is not None:
    post.rating = form.film92.data
else:
    post = Post(author=current_user, moovie_id=92, rating=int(form.film92.data))
    db.session.add(post)
post = Post.query.filter_by(user_id=current_user.id, moovie_id=93).first()
if post is not None:
    post.rating = form.film93.data
else:
    post = Post(author=current_user, moovie_id=93, rating=int(form.film93.data))
    db.session.add(post)
post = Post.query.filter_by(user_id=current_user.id, moovie_id=94).first()
if post is not None:
    post.rating = form.film94.data
else:
    post = Post(author=current_user, moovie_id=94, rating=int(form.film94.data))
    db.session.add(post)
post = Post.query.filter_by(user_id=current_user.id, moovie_id=95).first()
if post is not None:
    post.rating = form.film95.data
else:
    post = Post(author=current_user, moovie_id=95, rating=int(form.film95.data))
    db.session.add(post)
post = Post.query.filter_by(user_id=current_user.id, moovie_id=96).first()
if post is not None:
    post.rating = form.film96.data
else:
    post = Post(author=current_user, moovie_id=96, rating=int(form.film96.data))
    db.session.add(post)
post = Post.query.filter_by(user_id=current_user.id, moovie_id=97).first()
if post is not None:
    post.rating = form.film97.data
else:
    post = Post(author=current_user, moovie_id=97, rating=int(form.film97.data))
    db.session.add(post)
post = Post.query.filter_by(user_id=current_user.id, moovie_id=98).first()
if post is not None:
    post.rating = form.film98.data
else:
    post = Post(author=current_user, moovie_id=98, rating=int(form.film98.data))
    db.session.add(post)
post = Post.query.filter_by(user_id=current_user.id, moovie_id=99).first()
if post is not None:
    post.rating = form.film99.data
else:
    post = Post(author=current_user, moovie_id=99, rating=int(form.film99.data))
    db.session.add(post)
post = Post.query.filter_by(user_id=current_user.id, moovie_id=100).first()
if post is not None:
    post.rating = form.film100.data
else:
    post = Post(author=current_user, moovie_id=100, rating=int(form.film100.data))
    db.session.add(post)


"No Time To Die (2021)","Dune (2021)","The French Dispatch (2021)","Last Night In Soho (2021)","Antlers (2021)","Knocking (2021)","The Last Duel (2021)","Venom: Let There Be Carnage (2021)","Ron's Gone Wrong (2021)","The Estate (2021)","Passing (2021)","The Gig Is Up (2021)Violet (2021)","Violet (2021)","Suzanna Andler (2021)","ROH (2021)","Fever Dream (2021)","The Souvenir Part II (2021)","The Rescue (2021)","South of Heaven (2021)","Spine of Night (2021)"
