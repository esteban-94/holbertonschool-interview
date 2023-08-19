#!/usr/bin/python3


def canUnlockAll(boxes):
    opened_boxes = [False for i in range(len(boxes))]
    opened_boxes[0] = True
    box_index = 0
    while box_index < len(boxes):
        if opened_boxes[box_index]:
            for key in boxes[box_index]:
                if not opened_boxes[key] and box_index < key:
                    opened_boxes[key] = True
                elif not opened_boxes[key] and box_index > key:
                    opened_boxes[key] = True
                    box_index = key - 1

        box_index += 1

    if all(box is True for box in opened_boxes):
        return True
    return False
