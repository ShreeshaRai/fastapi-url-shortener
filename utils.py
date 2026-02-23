import string

BASE62 = string.ascii_letters + string.digits

def encode_base62(num):
    if num == 0:
        return BASE62[0]

    result = []
    base = len(BASE62)

    while num:
        remainder = num % base
        result.append(BASE62[remainder])
        num //= base

    return ''.join(reversed(result))

