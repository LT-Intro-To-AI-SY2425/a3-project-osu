import pandas as pd

file_path = '/Users/jonathanhimawan/Documents/imdb_top_1000.csv'
imdb_data = pd.read_csv(file_path)

print(imdb_data.info())

