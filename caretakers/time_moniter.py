import datetime
import time


class time_moniter:
    # This class is used to monitor the time of the system.
    # It is used to determine if the system is running for a long time.
    # It is used to determine if the system is running for a long time.
    def __init__(self) -> None:
        self.start_time = datetime.time()  # Start time of the program
        self.end_time = None
        self.elapsed_time = None   # 20 minutes

    # get Current system time.
    def get_current_time(self):
        return datetime.datetime.now()

    def start_t(self):
        self.start_time = datetime.time()   # resetting start time
        return self.start_time

    def end_t(self) -> float:
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
