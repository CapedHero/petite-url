import secrets


def create_petite_code() -> str:
    """
    + With the current implementation, this function returns one of 16^10 unique
      codes. This amounts to around a trillion possibilities.

      + We return 5 bytes string. Each byte is encoded into 2 hex values,
        and as 5 x 2 = 10, thus the function returns 10 characters.

      + 16^10 = 16-possible-hex-values ^ 10-returned-characters
    """
    return secrets.token_bytes(nbytes=5).hex()
