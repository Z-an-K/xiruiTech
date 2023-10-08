import pandas as pd

df = pd.read_csv("./fyx_chinamoney.csv")
batch_size = 80
batches = [df[i:i+batch_size] for i in range(0, len(df), batch_size)]

for i, batch in enumerate(batches):
    print(f'Batch {i+1}:')
    print(batch)