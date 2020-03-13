class Login():
    def validate(form):
        email = form.email
        if not isinstance(email, str):
            return 'Invalid E-mail'
        else:
            return 'Validated'
