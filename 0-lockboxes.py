#!/usr/bin/python3


def canUnlockAll(boxes):
    opened_boxes = [False for i in range(len(boxes))]
    if all(box is True for box in opened_boxes):
        return True
    return False
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))