from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

def encode_uuid(pk):
    return force_str(urlsafe_base64_encode(force_bytes(pk)))


def decode_uuid(pk):
    return force_str(urlsafe_base64_decode(force_bytes(pk)))