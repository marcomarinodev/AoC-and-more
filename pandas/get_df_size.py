import pandas as pd 
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]

print(getDataframeSize(pd.DataFrame([
    [1, 'x'],
    [1, 'x'],
    [1, 'x'],
    [1, 'x'],
    [1, 'x']
])))


