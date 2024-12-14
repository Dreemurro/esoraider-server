class ESOLogsException(Exception):
    pass


class ZeroLengthFightException(ESOLogsException):
    def __init__(self):
        message = "This fight's duration is zero"
        super().__init__(message)
