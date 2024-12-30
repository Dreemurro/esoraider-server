class AnalysisError(Exception):
    pass


class SkillsNotFoundError(AnalysisError):
    def __init__(self):
        message = 'Log is broken - character skills were not found'
        super().__init__(message)


class NothingToTrackError(AnalysisError):
    def __init__(self):
        message = 'There is nothing to track'
        super().__init__(message)


class WrongCharError(AnalysisError):
    def __init__(self):
        message = 'Wrong char selected'
        super().__init__(message)


class OutsideOfCombatError(AnalysisError):
    def __init__(self):
        message = 'This char was outside of combat'
        super().__init__(message)
