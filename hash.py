import hashlib

from config import SECRET_KEY


def hash_password(value):
    md5 = hashlib.md5()
    md5.update(bytes(value + SECRET_KEY, encoding='utf8'))

    return md5.hexdigest()
