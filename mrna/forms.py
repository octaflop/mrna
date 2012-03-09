from flaskext.wtf import Form, BooleanField, TextField, validators,\
PasswordField, FileField, TextAreaField, DateTimeField, RecaptchaField,\
HiddenField, DateField, EmailField

from flaskext.babel import gettext as _
from flaskext.babel import ngettext as _n

class ContactForm(Form):
    subject = TextField(_("Subject"),\
                [validators.required(),\
                validators.length(min=3, max=200)])
    sender = EmailField(_("Your Email"))
    message = TextAreaField(_("Message"))
