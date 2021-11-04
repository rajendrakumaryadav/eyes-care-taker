import time

from plyer import notification


class caretaker:
    def __init__(self) -> None:
        pass

    def notify(self, title: str, message: str) -> None:
        notification.notify(
            title=title,
            message=message,
            app_name="Caretaker",
            timeout=10,
        )

    def run(self) -> None:
        while True:
            self.notify("Caretaker", "Caretaker is running")
            time.sleep(60)
