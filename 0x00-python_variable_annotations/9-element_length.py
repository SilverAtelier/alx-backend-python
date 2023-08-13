#!/usr/bin/env python3
from typing import List, Tuple, Sequence, Iterable
"""
function annotations
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    advanced annotations
    """
    return [(i, len(i)) for i in lst]
