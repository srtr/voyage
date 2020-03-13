import re

class Login:
    def validate(self, form):
        if 'name' not in form or 'mobile' not in form or 'email' not in form:
            return False

        email = form['email']
        name = form['name']
        mobile = form['mobile']

        if not isinstance(email, str) or not isinstance(name, str) or not name or not email:
            return False

        if len(email) > 7:
            if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
                return True
        return False
