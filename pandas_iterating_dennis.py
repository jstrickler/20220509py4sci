import pandas as pd
import numpy as np

from EXAMPLES.printheader import print_header

cols = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']  # <1>
index = ['a', 'b', 'c', 'd', 'e', 'f']  # <2>

values = [  # <3>
    [100, 110, 120, 130, 140],
    [200, 210, 220, 230, 240],
    [300, 310, 320, 330, 340],
    [400, 410, 420, 430, 440],
    [500, 510, 520, 530, 540],
    ["abc", 610, 620, 630, 640],
]

df = pd.DataFrame(values, index=index, columns=cols)  # <4>
print_header('DataFrame df')
print(df, '\n')

# all values in column 'alpha'
result = all(isinstance(x, np.int64) for x in df['alpha'].values)
print("result: {}".format(result))


# all values in DF
result = all(isinstance(x, np.int64) for x in df.values.flatten())
print("result: {}".format(result))
