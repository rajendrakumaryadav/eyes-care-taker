import os
import time

from plyer import notification

import caretakers.time_moniter as time_moniter


class caretaker:
    def __init__(self) -> None:
        # self.run()
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
            self.notify("Eyes Caretaker", "Watch away for 20 seconds\n\
I will be back after 20 minuts.")
            time.sleep(60 * 20)  # 20 min
            time_moniter.time_moniter().reset_time()  # reset time
            print(
                f"Time counter is resetting \
                    {time_moniter.time_moniter.start()}")
