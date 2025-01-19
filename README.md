# Develop Environment for Python Data Analytics
This project illustrates simple data analytics with Python Pandas and Pyspark. The develop enviroment uses Github codespaces and Devcontainers.

The project illustrates the following kinds of data analysis
1. Run analysis locally using pandas
See [taxi-batch-analysis.py](taxi-batch-analysis.py)

2. Run analysis using a Spark job locally
See [spark-wordcount.py](spark-wordcount.py)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/esumitra/python-codespace-spark?quickstart=1)


## Using Codepspaces
(image-goes-here)
1. Click the "Open in Github Codespaces" button above
2. Start a terminal
3. Run pandas analysis
```
python taxi-batch-analysis.py
```
4. Run spark analysis
```
python spark-wordcount.py
```

## Using Local Devcontainer
[<img src="./images/devcontainer-local.png" width="400"/>](./images/devcontainer-local.png)
1. Open Visual Studio Code (VSC) editor
```
code .
```
2. Install devcontainers plugin
3. Open project in a dev container
(Cmd + Shift + P) and select `Devcontainers: Rebuild Container`
4. Start a terminal window
5. Run pandas analysis
```
python taxi-batch-analysis.py
```
6. Run spark analysis
```
python spark-wordcount.py
```

## Pyspark Interactive console
(image-goes-here)
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
