class Login:
    def validate(form):
        email = form['email']
        if not isinstance(email, str):
            return False
        else:
            return True
