import re

class Login:

    def validate_email(self,email):
        if not isinstance(email, str) or not email:
            return False

        if len(email) > 7:
            
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
        
        if len(mobile) == 10:
            
            if re.match('^[0-9]+$', mobile) != None:
                return True

        return False

    def validate(self, form):
        keys = ['name','mobile','email']

        for key in keys:
            if key not in form:
                return False

        email = form['email']
        name = form['name']
        mobile = form['mobile']
        
        return self.validate_email(email) and self.validate_name(name) and self.validate_mobile(mobile)

        
