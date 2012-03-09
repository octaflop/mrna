from flask import Flask
app = Flask(__name__)

from views import mail_admin
from forms import ContactForm
from decorators import template

#from mrna.settings import ADMIN
@template('templates/base.html')
@app.route('/contact/')
def contact_form(request, *args, **kwargs):
    form = ContactForm(request.form)
    msg = {}
    if form.validate_on_submit():
        subject = form.subject.data
        message = form.message.data
        sender = form.sender.data
        msg = dict(sender=sender, subject=subject, message=message)
        ret = mail_admin(request, msg, args, kwargs)
        if ret[succ_code] != 0:
            flash("There was an error sending this message")
            return redirect(app.route('/'))
    ret = dict(request=request, args=args, kwargs=kwargs, msg=msg)
    return ret

if __name__ == "__main__":
    app.run()
