import uuid
import pandas as pd
df = pd.read_csv('test.csv')
df.reset_index(inplace=True)
print(df.columns)
print(df.groupby('uuid').count())
print([uuid.uuid4() for x in range(1, 10)])

print(df['index'].tolist())