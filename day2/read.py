import pandas as pd

filename = 'data.csv'
df = pd.read_csv(filename)

a=df['x']
b=df['y']

sum_a=0
sum_b=0

for i in range(0, 5):
    sum_a=sum_a+a[i]

for j in range(0,5):
    sum_b=sum_b+b[j]
    

print(sum_a, sum_b)


    


