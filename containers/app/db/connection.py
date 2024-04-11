import psycopg2
import time


class RetryDecorator:

    def __init__(self, max_attempts=5, delay=0.1):
        self.delay = delay
        self.max_attempts = max_attempts

        self.func = None

    def __call__(self, *args, **kwargs):
        if not self.func:
            self.func = args[0]
            return self

        results = None
        attempts = 1

        while not results:
            try:
                results = self.func(*args, **kwargs)

            except TypeError as error:
                if attempts == self.max_attempts:
                    raise

            finally:
                time.sleep(attempts * self.delay)
                attempts += 1


@RetryDecorator(5, 0.5)
def get_connection():
    return psycopg2.connect(
        host="database",
        database="postgres",
        user="postgres",
        password="ratestask",
    )
