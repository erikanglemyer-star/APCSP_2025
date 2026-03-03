import pandas as pd

chunk_size = 1000
chunks = pd.read_csv("apple_quality.csv", chunksize=chunk_size)

for chunk in chunks:
    first_15_lines = chunk.head(15)
    
    # Calculate the average sweetness for the first 15 lines
    average_sweetness = first_15_lines['Sweetness'].mean()
    print(f"Average Sweetness (first 15 lines): {average_sweetness}")
    
    first_15_lines.to_csv('first_15_lines.csv', index=False)
    break