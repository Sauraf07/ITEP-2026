import bcrypt


def hash_password(password:str):
    password_bytes = password.encode("utf-8")
    salt_key =  bcrypt.gensalt(12)
    hashed_password = bcrypt.hashpw(password_bytes, salt_key)
    return hashed_password