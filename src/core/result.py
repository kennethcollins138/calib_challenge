import loguru


class Result:
    """
    Result is a monad wrapper for the return value of a function.
    I decided to add this to simplify my logging and error handling.
    """
    def __init__(self, value=None, error=None):
        self.value = value
        self.error = error

    @classmethod
    def from_(cls, func, *args, **kwargs):
        """
        from_ is a class method that wraps the function call and returns a Result object.
        :param func: the function to be called.
        :param args: the arguments to be passed to the function.
        :param kwargs: the keyword arguments to be passed to the function.
        :return: Result object.
        """
        try:
            return cls(value=func(*args, **kwargs))
        except Exception as e:
            return cls(error=e)

    def map(self, fn):
        """
        map is a method that applies a function to the value of the Result object.
        :param fn: the function to be applied to the value.
        :return: the result of the function application.
        """
        if self.error:
            return self
        try:
            return Result(value=fn(self.value))
        except Exception as e:
            return Result(error=e)

    def tap(self, logger: loguru.Logger):
        """
        tap is a method that logs the value of the Result object.

        :param logger:
        :return:
        """
        if self.error:
            logger.error(f"[ERROR] {self.error}")
        else:
            logger.info(f"[OK] {self.value}")
        return self
