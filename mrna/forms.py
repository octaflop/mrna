from flaskext.wtf import Form, BooleanField, TextField, validators,\
PasswordField, FileField, TextAreaField, DateTimeField, RecaptchaField,\
HiddenField, DateField

from flaskext.babel import gettext as _
from flaskext.babel import ngettext as _n

class ContactForm(Form):
    subject = TextField(_("Subject"),\
                [validators.Required(),\
                validators.length(min=3, max=200)])
    sender = TextField(_("Your Contact Email Address"),\
            [validators.required(),\
            validators.length(min=3, max=100),\
            validators.Email()])
    message = TextAreaField(_("Message"))
