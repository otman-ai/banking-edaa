import pandas as pd
import json
import numpy as np
input_title = ['job', 'marital', 'education', 'default', 'housing', 'loan',
                'poutcome','day_of_week',"contact"]
df = pd.read_csv("Dataset/data.csv")
dict_ = {}
for input in input_title:
    uniques = [in_ for in_  in df[input].unique()]
    dict_[input] = uniques
print(dict_)
with open("Dataset/uniques.json","w") as f:
    f.write(json.dumps(dict_))