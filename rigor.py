def precond(expr):
    if not expr: raise PreconditionError('Precondition Failure')


def postcond(expr):
    if not expr: raise PostconditionError('PostconditionError Failure')


class PreconditionError(Exception):
    def __init__(self, value):
        self.value = value


class PostconditionError(Exception):
    def __init__(self, value):
        self.value = value
