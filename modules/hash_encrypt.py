import hashlib, logging

def encrypt(value: str):
    encode_ready = value.encode("utf-8")
    sha256 = hashlib.sha256()
    sha256.update(encode_ready)
    if value is None or value == "":
        logging.error("value is None or empty")
        raise ValueError("I'm get None or empty value")
    return sha256.hexdigest()


