class ESOLogsError(Exception):
    pass


class ZeroLengthFightError(ESOLogsError):
    def __init__(self):
        message = "This fight's duration is zero"
        super().__init__(message)


class NonexistentLogError(ESOLogsError):
    def __init__(self):
        message = "This log is either private or doesn't exist"
        super().__init__(message)


class NonexistentFightError(ESOLogsError):
    def __init__(self):
        message = 'Could not find this fight'
        super().__init__(message)
