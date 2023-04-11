
import pandas as pd

df = pd.read_csv("matrix/matrix.csv")
columns = df.columns
line = " ----- "
cols = "|"
sep = "|"
lines_ = "|"

for i ,col in enumerate(columns):
    cols = cols + col+sep
    lines_ = lines_+line+sep
kk = []
print(cols)
print(lines_)
for row in df.values:
    ll = ""
    for r in row:
        ll  = ll+sep+str(r)
    ll = ll+sep
    print(ll)
    kk.append(ll)
