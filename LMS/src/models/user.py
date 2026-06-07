class User:

    def __init__(
            self,
            user_id=None,
            full_name=None,
            email=None,
            password_hash=None,
            role=None):

        self.user_id = user_id
        self.full_name = full_name
        self.email = email
        self.password_hash = password_hash
        self.role = role