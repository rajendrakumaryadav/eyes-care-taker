import time

from plyer import notification


class caretaker:
    def __init__(self) -> None:
        pass

    def notify(self, title: str, message: str) -> None:
        notification.notify(
            title=title,
            message=message,
            app_name="Eyes Caretaker",
            timeout=5,
        )

    def run(self) -> None:
        while True:
            self.notify("Caretaker", "Watch away from your screen")
            time.sleep(10)
