import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401
import demistomock as demisto
from CommonServerPython import *


def main():
    try:
        xyz_test()
        print("test")
    except Exception as e:
        print(str(e))
