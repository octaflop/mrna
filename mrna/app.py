from flask import Flask

from mrna.views import contactform
from forms import ContactForm

app = Flask.app(__name__)

#from mrna.settings import ADMIN

@app.route('/contact/')
def contact_form(request, *args, **kwargs):
    form = ContactForm(request.form)
    if form.validate_on_submit():
        subject = form.subject.data
        message = form.message.data
        sender = form.sender.data
        msg = dict(sender=sender, subject=subject, message=message)
        ret = mail_admin(request, msg, args, kwargs)
        if ret[succ_code] != 0:
            flash("There was an error sending this message")
            return redirect(app.route('/'))
    return ret


