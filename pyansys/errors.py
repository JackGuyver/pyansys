LOCKFILE_MSG = """
Another ANSYS job with the same job name is already running in this
directory, or the lock file has not been deleted from an abnormally
terminated ANSYS run.

Disable this check by passing ``override=True``

"""

class MapdlRuntimeError(RuntimeError):
    """Raised when MAPDL passes an error"""
    pass


class LockFileException(RuntimeError):
    """Error message when the lockfile has not been removed"""
    def __init__(self, msg=LOCKFILE_MSG):
        RuntimeError.__init__(self, msg)
