# Develop Environment for Python Data Analytics
This project illustrates simple data analytics with Python Pandas and Pyspark. The develop enviroment uses Github codespaces.

The project illustrates the following kinds of data analysis
1. Run analysis locally using pandas
See taxi-batch-analysis

2. Run Spark analysis job locally
See spark-wordcount.py

## Using up a Codepsace
1. Click the "Open in Github Codespaces" button
2. Start a terminal
3. Run pandas analysis
4. Run spark analysis

`python taxi-batch-analysis.py`

## Using Devcontainers
1. Open Visual Studio Code (VSC) editor
```
code .
```
2. Install devcontainers plugin
In VSC plugins search for and install
3. Open project in a dev container
4. Start a terminal
5. Run pandas analysis
6. Run spark analysis
`python taxi-batch-analysis.py`

## Pyspark Interactive console
1. Open pyspark console
```
pyspark
```
2. Load csv file
```
spark_df = spark.read.csv("./data/taxi_tripdata.csv", header=True, inferSchema=True)
```
3. Show dataframe
```
spark_df.show()
```
4. Count rows
```
spark_df.count()
```
5. Quit console
```
quit()
```

Open spark console at http://localhost:4040/jobs/

### Copyright
Copyright 2025, Edward Sumitra

Licensed under the MIT License.
