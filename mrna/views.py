from flaskext.mail import Message
def warn_admin(req, mail):
    """
    emails the request information to the admin
    """
    message = {
            "subject": "WARNING: Bot attempted to access email form",
            "sender": "system@example.com",
            }
    msg = Message(message['subject'], sender=message['sender'],
            recipients=['to@example.com'])

    message['message'] =\
            """
A wannabe cracker (or loose bot) fell for the honeypot. Here are the
details from the req:\n
%(req)s 
            """ % {
                    "req": req,
                }
    msg.body = message['message']
    try:
        mail.send(msg)
        ret = dict(msg=msg,
                succ_code=0)
    except:
        ret = dict(msg=msg,
                succ_code=1)
    return ret


def mail_admin(message, mail):
    """
    mail the admin an email if the recapcha passes
    TODO: add extensions modules on args kwargs
    """
    msg = Message(message['subject'], sender=message['sender'],
            recipients=['to@example.com'])
    msg.body = message['message']
    try:
        mail.send(msg)
        ret = dict(msg=msg,
                succ_code=0)
    except:
        ret = dict(msg=msg,
                succ_code=1)
    return ret

