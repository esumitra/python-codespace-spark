# run with puthon taxi-batch-analysis.py
import pandas as pd

# Load the data
data:pd.DataFrame = pd.read_csv('./data/taxi_tripdata.csv')

# total number of trips
def total_trips(data:pd.DataFrame)->int:
    return data.shape[0]

# run main function
if __name__ == '__main__':
    print(f'Total number (count) of trips:{total_trips(data)}')
