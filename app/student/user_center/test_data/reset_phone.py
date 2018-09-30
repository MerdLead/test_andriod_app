import random


# data base of image location
# we can add a or multiple account in it, like this '{'x': 'xxxxxxxxxxx', 'y': 'yyyyyyyy'},'

_VALID_RESETPHONE = (
    {'origin': '18011111223', 'reset': '18211111000', 'password': '123456'},
    {'origin': '18211111000', 'reset': '18011111223', 'password': '123456'},
)


class ResetPhone:
    def __init__(self):
        self.valid_account = _VALID_RESETPHONE[random.randint(0, len(_VALID_RESETPHONE)) - 1]

    def origin(self):
        return self.valid_account['origin']

    def reset(self):
        return self.valid_account['reset']

    def password(self):
        return self.valid_account['password']


# global variable
# a instance of image location
# it can be used in any place via 'from App.student.user_center.test_data.image import VALID_IMAGE'
VALID_RESETPHONE = ResetPhone()
VALID_RESETPHONE.origin()
VALID_RESETPHONE.reset()
VALID_RESETPHONE.password()
