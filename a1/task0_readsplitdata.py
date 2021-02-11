from typing import List, Dict
from collections.abc import Callable


def classify(classifier_obj: Dict, new_line: List[str]) -> None:
    """Adds the polarity and content of a line to the proper dictionary key

    Parameters
    ----------
    classifier_obj : Dict
        Object storing all types of label as lists of {polarity, content} for each line
    new_line : List[str]
        String representing a line of the txt document

    Returns
    -------
    None
    """
    doctype, polarity, _, content = new_line
    classifier_obj.setdefault(doctype, []).append({"polarity": polarity, "content": content})


def get_classifier_obj_from_file(filename: str, line_callback: Callable) -> Dict:
    """Goes through all lines of a file and calls a callback for each

    Parameters
    ----------
    filename : str
        Name of the file to open
    line_callback : Callable
        Callback function to execute for each line

    Returns
    -------
    Dict
    """
    classifier_obj = {}
    with open(filename) as f:
        for line in f.read().splitlines():
            line_callback(classifier_obj, line.rstrip('\n').split(' ', 3))
    return classifier_obj
