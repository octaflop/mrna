from flaskext.mail import Message
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

