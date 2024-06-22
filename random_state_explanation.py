import pandas as pd

x = pd.DataFrame(pd.Series([x for x in range(1, 11)]), columns=['serial_number'])

sample_x = x.sample(n=5, random_state=0)

print(sample_x)

