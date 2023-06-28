from typing import (
    NewType,
    List,
    Tuple
)


Position = NewType('Position', Tuple[int, int])
Coordinates = NewType('Coordinates', List[Tuple[int, int]])
