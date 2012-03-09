def mail_admin(request, msg, *args, **kwargs):
    """
    mail the admin an email if the recapcha passes
    """
    try:
        ret = dict(request=request, args=args, kwargs=kwargs,\
                succ_code=0)
    except:
        ret = dict(request=request, args=args, kwargs=kwargs,\
                succ_code=1)
    return ret

