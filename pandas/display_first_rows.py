import pandas as pd 
from typing import List

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)    

print(selectFirstRows(pd.DataFrame([
    [1, 'x'],
    [1, 'x'],
    [1, 'x'],
    [1, 'x'],
    [1, 'x']
])))


