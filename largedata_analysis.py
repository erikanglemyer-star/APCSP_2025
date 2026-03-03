import pandas as pd

chunk_size = 1000
chunks = pd.read_csv("Public_School_Characteristics_2022-23.csv", chunksize=chunk_size)

for chunk in chunks:
    first_20_lines = chunk.head(20)
    
    print(first_20_lines)

    # Calculate mean of a specific column (e.g., 'WH' for White students)
    mean_X = first_20_lines['X'].mean()
    mean_Y = first_20_lines['Y'].mean()
    print(f"Mean school longitude and latitude: {mean_X}, {mean_Y}")
    break