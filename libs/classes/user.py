"""
Represents user's data
"""
__main__ = ['User', 'UserInvalidDataException']


import json


class User():
    def __init__(self, id :int, email: str, password: str, enabled: bool=False, token: str=None):
        if email and password:
            self.id = id
            self.email = email
            self.password = password
            self.enabled = enabled
            self.token = token
            self._display_name = None
        else:
            raise UserInvalidDataException

    def to_dict(self):
        """ Make it JSON serializable """
        return {
            'id': self.id,
            'email': self.email,
            'displayName': self.display_name
        }

    @property
    def display_name(self):
        if not self._display_name:
            self._display_name = self.email.split('@')[0]
        return self._display_name


class UserInvalidDataException (Exception):
    pass
