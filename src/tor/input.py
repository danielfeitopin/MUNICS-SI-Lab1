class Input:
    """Class to get input from user."""

    @staticmethod
    def get_path() -> list[str]:
        """Gets the path followed from s to r.

        Returns
        -------
            list[str]: List of IDs.
        """        

        path: list[str] = []

        s: str = input(f'Introduce sender-id (or leave blank for \'none\'): ')
        path.append(s if s != '' else 'none')

        while True:
            id: str = input(f'Introduce user-id or leave blank to finish: ')

            if id == '':
                break

            if 3 <= len(id) and len(id) <= 4:
                path.append(id)
            else:
                print('user-id must be three or four letters!')

        return path

    @staticmethod
    def get_message() -> bytes:
        """Gets message from input.

        Returns
        -------
            bytes: Message as bytes.
        """

        return input('Write message to send: ').encode('ascii')