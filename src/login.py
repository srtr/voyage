import re

class Login:

    EMAIL_MIN_LENGTH = 7
    MOBILE_LENGTH = 10
    ALLOWED_KEYS = {'name', 'mobile', 'email'}

    def validate_email(self,email):
        if not isinstance(email, str) or not email:
            return False

        if len(email) > self.EMAIL_MIN_LENGTH:
            
            if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
                return True

        return False

    def validate_name(self,name):
        if not isinstance(name, str) or not name:
            return False

        return True
    
    def validate_mobile(self,mobile):
        if not isinstance(mobile, str):
            return False
        
        if len(mobile) == self.MOBILE_LENGTH:
            
            if re.match('^[0-9]+$', mobile) != None:
                return True

        return False

    def validate(self, form):
        if form.keys() != self.ALLOWED_KEYS:
            return False

        email = form['email']
        name = form['name']
        mobile = form['mobile']
        
        return self.validate_email(email) and self.validate_name(name) and self.validate_mobile(mobile)

        
