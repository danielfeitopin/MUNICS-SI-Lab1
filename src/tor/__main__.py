from sys import argv
from .config import ID, PASSWORD
from .encrypt import MyKeys, nest_encrypt, relay_and_decrypt, extract_id
from .input import Input
from .mqtt import MQTT
from .pubkeys import PublicKeys
from .ui import UI


def main() -> None:

    def get_mqqt(id: str) -> MQTT:

        def on_message(client, userdata, message):

            print(UI.message_header())
            try:
                data: dict = relay_and_decrypt(message.payload,
                                               userdata['private_key'])
                next_hop: str = data['next_hop'].decode('ascii')
                if next_hop == 'end':
                    print(UI.get_info_message(
                        extract_id(data['message']).decode('ascii'),
                        (data['message'][5:]).decode('ascii')))
                else:
                    print(UI.get_info_forward(next_hop))
                    client.publish(next_hop, data['message'])
            except:
                print(UI.get_info_error())

        mqtt = MQTT(id)
        mqtt.on_message = on_message
        mqtt.user_data_set({'private_key': MyKeys(PASSWORD).private_key})

        return mqtt

    OPTIONS: set = {'activate', 'encrypt', 'send'}
    if len(argv) != 2 or argv[1].casefold() not in OPTIONS:
        print(UI.get_help_message())
        return

    option: str = argv[1]

    if option == 'activate':
        mqtt = get_mqqt(ID)
        print('Activating node...', end=' ')
        mqtt.connect()
        print('Done')
        mqtt.loop_forever()
    elif option in {'encrypt', 'send'}:
        # p = (s, h_1, h_2, ..., h_n)
        p: list[str] = Input.get_path()
        print(f'Path: {p}')
        if len(p) < 2:
            print('Invalid path, leaving...')
            return

        # K = {pk_1, pk_2, ..., pk_n}
        K: list[bytes] = [PublicKeys.get_key(id) for id in p[1:]]

        m: bytes = Input.get_message()

        c = nest_encrypt(p, K, m)

        if option == 'encrypt':
            print('Encrypted message: ')
            print(c)
        elif option == 'send':
            mqtt = get_mqqt(ID)
            print('Conecting...', end=' ')
            mqtt.connect()
            print('Done')

            print(f'Sending message to {p[1]}...', end=' ')
            mqtt.publish(p[1], c)
            print('Done')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Exiting...')
