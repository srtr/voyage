class Login():
    def validate(form):
        email = form.email
        if not isinstance(email, str):
            return false
        else:
            return true
