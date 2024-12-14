class AnalysisException(Exception):
    pass


class SkillsNotFoundException(AnalysisException):
    def __init__(self):
        message = 'Log is broken - character skills were not found'
        super().__init__(message)


class NothingToTrackException(AnalysisException):
    def __init__(self):
        message = 'There is nothing to track'
        super().__init__(message)


class WrongCharException(AnalysisException):
    def __init__(self):
        message = 'Wrong char selected'
        super().__init__(message)


class OutsideOfCombatException(AnalysisException):
    def __init__(self):
        message = 'This char was outside of combat'
        super().__init__(message)
