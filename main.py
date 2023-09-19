import pandas as pd

# with open('dados.csv', 'r') as file:
#     text = file.read()
    
df = pd.read_csv('words.csv', 
    names=['index', 'word', 'freq'])
print(df)