import os
import secrets
from PIL import Image
from flask import url_for
from flask import current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path , 'static/profile_images' ,picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    #form_picture.save(picture_path)
    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset Request',
                 sender='mudashiruagm@gmail.com', 
                recipients=[user.email])
    msg.body = "To reset your password, visit the following link: " + str({url_for('reset_token',token=token, _external=True)}) + " If you did not make this request, please ignore this email"
    mail.send(msg)