from termcolor import colored

import caretakers

print(f"""version: {caretakers.__version__}
author: {caretakers.__author__}
url: {caretakers.__url__}

This application is made for eyes care taking...
You screen will be blocked once you activate it.
After, Each 20 min of slot you will be notified with message
and your screen will be blocked for next 20 seconds with a message
colored.red "Watch 20 meters aways to relax the eyes mascules" 
""")
