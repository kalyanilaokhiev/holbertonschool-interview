#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """Going through all lists in the boxes to unlock boxes with keys"""
    # initialising set and keys
    unlocked = {0}
    keys = list(boxes[0])

    while len(keys) > 0:
        # pop out first int
        key = keys.pop()
        if key <= 0 or key < len(boxes):
            # add key if int isnt already in keys list
            if key not in unlocked:
                unlocked.add(key)
                # add all keys found inside unlocked box into keys list
                keys.extend(boxes[key])

    # if all boxes unlocked = true
    if len(unlocked) == len(boxes):
        return True
    else:
        return False
