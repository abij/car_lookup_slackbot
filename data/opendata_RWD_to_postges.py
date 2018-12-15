import sys, os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

assert len(sys.argv) == 2, 'The CSV filepath must be the first / only argument.'
file_name = sys.argv[1]

connectionProperties = {
    "user": os.environ.get('POSTGRES_USER', 'postgres'),
    "password": os.environ.get('POSTGRES_PASS', 'example'),
    "driver": "org.postgresql.Driver"
}

# Get a reference to the spark session.
spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Some ETL to filter and keep some of the interesting field:
df = spark.read.csv('/job/' + file_name, header=True)
df = df.filter(F.col('Voertuigsoort').isin('Personenauto', 'Motorfiets', 'Bedrijfsauto'))
df = df.select(
    F.col('Kenteken').alias('kenteken'),
    F.col('Voertuigsoort').alias('voertuigsoort'),
    F.col('Merk').alias('merk'),
    F.col('Handelsbenaming').alias('handelsbenaming'),
    F.to_date('Vervaldatum APK', 'dd/MM/yyyy').alias('dt_verval_apk'),
    F.col('Zuinigheidslabel').alias('label'),
    F.col('Catalogusprijs').cast('int').alias('catalogusprijs')
)

# Write dataframe to postgres
jdbc_url = "jdbc:postgresql://{}:5432/{}".format(
    os.environ.get('POSTGRES_CONTAINER_NAME', 'postgres'),
    os.environ.get('POSTGRES_DB', 'postgres'))

df.write.jdbc(jdbc_url, os.environ.get('POSTGRES_TABLE', 'voertuigen'),
              properties=connectionProperties,
              mode='overwrite')
