#!/usr/bin/env python

from functools import wraps
from flask import g, request, redirect, url_for, render_template, session

def template(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint \
                    .replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator

