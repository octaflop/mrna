from flask import Flask
from flaskext.mail import Mail
app = Flask(__name__)
mail = Mail(app)
from flask import request, render_template, url_for, flash, redirect

from views import mail_admin
from forms import ContactForm
from decorators import template

#from mrna.settings import ADMIN
#@template('templates/base.html')
@app.route('/contact/', methods=['GET','POST',])
def contact_form():
    form = ContactForm(request.form)
    msg = {}
    if request.method == 'POST' and form.validate():
    #if form.validate_on_submit():
        subject = form.subject.data
        message = form.message.data
        sender = form.sender.data
        msg = dict(sender=sender, subject=subject, message=message)
        ret = mail_admin(msg, mail)
        if ret['succ_code'] != 0:
            flash("There was an error sending this message")
            return redirect(url_for('contact_success'))
        else:
            flash("Message %(subject)s was sent successfully by %(email)s" %\
                    {
                        "subject" : msg.subject,
                        "email" : msg.sender,
                    })
            return redirect(url_for('contact_success'))
    return render_template('base.html', msg=msg, form=form)

@app.route('/contact/success/')
def contact_success():
    return render_template('success.html')

if __name__ == "__main__":
    app.secret_key = "curengoiehgoeaity8von3ysl6nveyli8nutifxrhyb7ivty"
    app.debug = True
    app.run()
