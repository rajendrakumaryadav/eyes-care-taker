import os
import time

from plyer import notification

import caretakers.time_moniter as time_moniter


class caretaker:
    def __init__(self) -> None:
        pass

    def notify(self, title: str, message: str) -> None:

        notification.notify(
            title=title,
            message=message,
            app_name="Eyes Caretaker",
            app_icon=os.path.realpath(".") + "/icons/eyes.png",
            timeout=5,  # hide notification after 5 seconds
        )

    def run(self) -> None:
        while True:
            current_time = time_moniter.time_moniter.start(self)

            self.notify(
                title="Eyes Caretaker",
                message="""Watch away for 20 seconds.\nI will be back after \
20 minuts.""",
            )
            time.sleep(current_time + (2 * 60))
            time_moniter.reset_time()
            self.run(self)
