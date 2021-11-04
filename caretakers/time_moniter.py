import time


class time_moniter:
    # This class is used to monitor the time of the system.
    # It is used to determine if the system is running for a long time.
    # It is used to determine if the system is running for a long time.
    def __init__(self) -> None:
        self.start_time = time.time()  # Start time of the program
        self.end_time = None
        self.elapsed_time = None   # 20 minutes

    def start(self) -> float:
        self.start_time = time.time()   # resetting start time
        return self.start_time

    def end(self) -> float:
        self.end_time = time.time()
        return self.end_time

    def set_start_time(self, start_time: float) -> None:
        self.start_time = start_time

    def reset_time(self) -> None:
        self.start_time = time.time()
        self.end_time = None

    def get_elapsed_time(self) -> float:
        if self.end_time is None:
            return time.time() - self.start_time
        else:
            return self.end_time - self.start_time
