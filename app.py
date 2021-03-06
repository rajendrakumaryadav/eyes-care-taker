import caretakers


class app:
    caretakers = caretakers.caretaker()

    def __init__(self):
        self.welcome_message()
        self.run()

    def run(self):
        while True:
            self.caretakers.run()

    def welcome_message(self):
        print(f"""
        Version: {caretakers.__version__}
        Author: {caretakers.__author__}
        Author's Git Profile: {caretakers.__url__}
        License: {caretakers.__license__}

        This application is made for eyes care taking...
        You screen will be blocked once you activate it.
        After, Each 20 min of slot you will be notified with message
        and your screen will be blocked for next 20 seconds with a message.
        "Watch 20 meter aways to relax the eyes mascules"
        """)


if __name__ == "__main__":
    try:
        app = app()
        app.run()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        exit(0)
