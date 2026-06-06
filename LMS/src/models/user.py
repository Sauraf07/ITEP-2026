class User:
    def __init__(self, user_id, name, email, password, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def __str__(self):
        return (
            f"User ID: {self.user_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Role: {self.role}"
        )