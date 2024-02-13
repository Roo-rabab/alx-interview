#!/usr/bin/python3
"""A module for working with lockboxes.
This is a module that provides a function for determining if all
boxes in a given list can be opened.
"""


def canUnlockAll(boxes):
    """Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.

    This function takes a list of lists and returns a boolean indicating
    whether all boxes in the list can be opened. A key with the same
    number as a box opens that box. You can assume all keys will be
    positive integers. There can be keys that do not have boxes.
    The first box boxes[0] is unlocked.

    boxes (List[List[int]]): The list of lists representing the boxes
    and their keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    visible_boxes = set([0])
    invisible_boxes = set(boxes[0]).difference(set([0]))
    while len(invisible_boxes) > 0:
        boxIdx = invisible_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in visible_boxes:
            invisible_boxes = invisible_boxes.union(boxes[boxIdx])
            visible_boxes.add(boxIdx)
    return n == len(visible_boxes)
