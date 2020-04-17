class CanNotRegisterDuplicatedUserException(Exception):
    status_code = 411


class CanNotRegisterNot20sUserException(Exception):
    status_code = 422


class CanNotRegisterUserNameException(Exception):
    status_code = 433
