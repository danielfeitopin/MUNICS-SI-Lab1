from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


class PublicKeys:
    """Class to get public keys for RSA cipher."""

    pubkey_dictionary = {
        # TODO
    }

    @classmethod
    def get_key(cls, id: str):
        """Gets a SSH public key from the Base64 key stored in the dictionary.

        Args:
            id (str): User ID.

        Returns:
            SSH_PUBLIC_KEY_TYPES: Public SSH key.
        """

        b64_key: str = cls.pubkey_dictionary.get(id)

        if b64_key is None:
            print(f'Error: Could not get key for id \'{id}\'')
            exit(-1)

        return serialization.load_ssh_public_key(
            ('ssh-rsa ' + b64_key).encode('ascii'),
            backend=default_backend()
        )
