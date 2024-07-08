import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401
def main():
    try:
        win_test()
    except Exception as e:
        print(str(e))
    #    print(traceback.format_exc())
