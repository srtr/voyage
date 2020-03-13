class Login:
    def validate(self, form):
        email = form['email']
        if not isinstance(email, str):
            return False
        else:
            return True
