# run with: python spark-wordcount.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode,split,col


def count_words() -> None:
  '''Counts frequency of words in the text
  of Alice in Wonderland
  '''
  spark = SparkSession.builder.getOrCreate()
  df=spark.read.text("data/alice_in_wonderland.txt")
  #Apply Split, Explode and groupBy to get count()
  df_count = (
    df.withColumn('word', explode(split(col('value'), ' ')))
      .groupBy('word')
      .count()
      .sort('count', ascending=False)
  )

  #Display Output
  df_count.show()
  spark.stop()

if __name__ == "__main__":
  count_words()