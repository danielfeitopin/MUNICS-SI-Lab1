from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class MyKeys:
    """
    Class to get public and private keys from key files.

    ...

    Attributes
    ----------
    public_key : _SSH_PUBLIC_KEY_TYPES
        SSH public key.

    private_key : _SSH_PRIVATE_KEY_TYPES
        SSH private key.
    """

    def __init__(self, password: bytes) -> None:
        """
        Constructs all the necessary attributes for the object.

        Parameters
        ----------
        password: bytes
            Password to open the private key file.

        Returns
        -------
        None
        """

        with open("id_rsa.pub", "rb") as key_file:
            public_key = key_file.read()

        self.public_key = serialization.load_ssh_public_key(
            public_key,
            backend=default_backend()
        )

        with open("id_rsa", "rb") as key_file:
            private_key = key_file.read()

        self.private_key = serialization.load_ssh_private_key(
            private_key,
            password=password,
            backend=default_backend()
        )


def rsa_encrypt(key, m: bytes) -> bytes:
    """Encrypts message using RSA.

    Args:
        key: RSA key.
        m (bytes): Message to encrypt.

    Returns:
        bytes: Encrypted message.
    """

    return key.encrypt(
        m,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


def rsa_decrypt(key, c: bytes) -> bytes:
    """Decrypts message using RSA.

    Args:
        key: RSA key.
        c (bytes): Encrypted message.

    Returns:
        bytes: Decrypted message.
    """

    return key.decrypt(
        c,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


def aes_encrypt(key: bytes, m: bytes) -> bytes:
    """Encrypts message using AES.

    Args:
        key (bytes): AES key.
        m (bytes): Message to encrypt.

    Returns:
        bytes: Encrypted message.
    """

    return AESGCM(key).encrypt(key, m, None)


def aes_decrypt(key: bytes, c: bytes) -> bytes:
    """Decrypts message using AES.

    Args:
        key (bytes): AES key.
        c (bytes): Encrypted message.

    Returns:
        bytes: Decrypted message.
    """

    return AESGCM(key).decrypt(key, c, None)


def embed_id(id: bytes, message: bytes) -> bytes:
    """Prepends the 5 bytes of the ID before the message.

    Args:
        id (bytes): ID.
        message (bytes): Message.

    Returns:
        bytes: ID and message in bytes.
    """

    return b'\x00'*(5-len(id)) + id + message


def extract_id(message: bytes) -> bytes:
    """Extracts the 5 bytes of the ID from the message.

    Args:
        message (bytes): Message.

    Returns:
        bytes: ID without padding.
    """

    return message[:5].strip(b'\x00')


def encrypt(pk, data: bytes) -> bytes:

    k: bytes = AESGCM.generate_key(128)
    c: bytes = rsa_encrypt(pk, k) + aes_encrypt(k, data)
    return c


def nest_encrypt(p: list[str], K: list, m: bytes) -> bytes:

    m: bytes = embed_id(p[0].encode('ascii'), m)  # m = (s, m)
    m: bytes = embed_id(b'end', m)  # End-of-path marker

    c: bytes = encrypt(K[-1], m)  # c = E(pk_n, m)

    for i in range(len(p[1:])-1, 0, -1):  # for i=n−1 to 1
        c: bytes = encrypt(K[i-1], embed_id(p[i+1].encode('ascii'), c))

    return c


def relay_and_decrypt(c_h: bytes, sk_h) -> dict:

    c_1h: bytes = c_h[:sk_h.key_size//8]
    c_2h: bytes = c_h[sk_h.key_size//8:]
    k: bytes = rsa_decrypt(sk_h, c_1h)  # k = D(sk_h, c_1h)
    aux: bytes = aes_decrypt(k, c_2h)
    next_hop: bytes = extract_id(aux)
    c_h_plus_1 = aux[5:]
    return {
        'next_hop': next_hop,
        'message': c_h_plus_1
    }
