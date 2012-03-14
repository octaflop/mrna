from flaskext.wtf import Form, BooleanField, TextField, validators,\
PasswordField, FileField, TextAreaField, DateTimeField, RecaptchaField,\
HiddenField, DateField

from flaskext.babel import gettext as _
from flaskext.babel import ngettext as _n

class ContactForm(Form):
    subject = TextField(_("Subject"),
            [validators.Length(min=3, max=200)])
    sender = TextField(_("Your Contact Email Address"),
            [validators.Length(min=3, max=100),
            validators.Email(message=u'Invalid email address given')])
    emessage = TextAreaField(_("Message"))
    nospam = TextField(_("Please answer this question:\n\
            What is 1+1 = ?\
            Computers can answer this, but most can't read this."))
    # honeypot
    message = HiddenField(_("Don't even think of adding something here"),
            default="8")

