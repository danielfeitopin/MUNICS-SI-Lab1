from datetime import datetime


class UI:

    __COLOR_LIGHT_RED = '\033[1;31m'
    __COLOR_LIGHT_GREEN = '\033[1;32m'
    __COLOR_YELLOW = '\033[0;33m'
    __COLOR_CYAN = '\033[0;36m'

    __TEXT_RESET = '\033[0m'
    __TEXT_BOLD = '\033[1m'
    __TEXT_UNDERLINE = "\033[4m"
    __TEXT_BLINK = "\033[5m"

    @classmethod
    def get_help_message(cls) -> str:
        message = 'Usage: python -m tor (activate | encrypt | send):\n'
        message += '    activate    Activates tor node.\n'
        message += '    encrypt     Prints output of nest encryption.\n'
        message += '    send        Sends message using nest encryption.\n'
        return message

    @classmethod
    def message_header(cls) -> str:
        timestamp = '[ ' + str(datetime.now()) + ' ]'
        info = ' ' + 'Received message!'

        length = len(timestamp) + len(info)
        message = '\a' # Alert sound
        message += cls.__TEXT_BLINK
        message += '-'*length
        message += cls.__TEXT_RESET
        message += '\n'
        
        message += cls.__TEXT_BOLD
        message += timestamp
        message += cls.__COLOR_LIGHT_GREEN
        message += info
        message += cls.__TEXT_RESET
        
        return message

    @classmethod
    def get_info_forward(cls, id: str) -> str:
        message = cls.__COLOR_YELLOW
        message += f'Forwarding to '
        message += cls.__TEXT_BOLD
        message += id
        message += cls.__TEXT_RESET
        message += cls.__COLOR_YELLOW
        message += '...'
        message += cls.__TEXT_RESET
        return message

    @classmethod
    def get_info_message(cls, id: str, m: str) -> str:
        message = cls.__COLOR_CYAN
        message += 'FROM: '
        message += cls.__TEXT_BOLD
        message += id
        message += cls.__TEXT_RESET
        message += '\n'
        message += cls.__COLOR_CYAN
        message += 'MESSAGE: ' + '\n'
        message += cls.__TEXT_RESET
        message += m
        return message

    @classmethod
    def get_info_error(cls) -> str:
        message = cls.__COLOR_LIGHT_RED
        message += 'ERROR decrypting!'
        message += cls.__TEXT_RESET
        return message
