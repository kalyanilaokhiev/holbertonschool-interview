#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    unlocked = {0}
    keys = list(boxes[0])

    while len(keys) > 0:
        key = keys.pop()
        if key <= 0 or key < len(boxes):
            if key not in unlocked:
                unlocked.add(key)
    
    if len(unlocked) == len(boxes):
        return True
    else:
        return False