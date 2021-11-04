import time


class time_moniter:
    def __init__(self) -> None:
        self.start_time = time.time()  # Start time of the program
        self.end_time = None
        self.elapsed_time = None   # 20 minutes

    def start(self) -> None:
        self.start_time = time.time()   # resetting start time

    def end(self) -> None:
        self.end_time = time.time()

    def get_elapsed_time(self) -> float:
        if self.end_time is None:
            return time.time() - self.start_time
        else:
            return self.end_time - self.start_time
