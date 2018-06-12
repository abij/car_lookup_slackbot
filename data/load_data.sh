#!/usr/bin/env bash

set -e  # exit on error

dirname=$(basename "$PWD")
if [ ${dirname} != 'data' ]; then
    echo 'Error: must run script from within the data directory'
    exit 1
fi

data_filename="Open_Data_RDW__Gekentekende_voertuigen.csv"
download_url="https://opendata.rdw.nl/api/views/m9d7-ebf2/rows.csv?accessType=DOWNLOAD"

if [ -f ${data_filename} ]; then
    echo "Skipping download of '$data_filename', file is present."
else
    echo "Start downloading the '$data_filename' locally ~7Gb..."
    curl ${download_url} -o ${data_filename}
fi

is_postgres_container_running=$(docker inspect -f {{.State.Running}} postgres)
if [ ${is_postgres_container_running} == 'false' ]; then
    echo "Error: No container running with name 'postgres'. Just follow the readme!"
    exit 1
fi


echo "Create empty table 'voertuigen', and load with CSV data using Spark..."
docker exec -it postgres psql -U postgres -c "CREATE TABLE IF NOT EXISTS public.voertuigen ();"

# Open the Spark UI:
open http://localhost:4040/

## Run a PySpark job to load the data, mounting the current dir as '/job'
docker run --rm \
    --volume $(pwd):/job \
    --link postgres:postgres \
    --net car_lookups_default \
    --publish 4040:4040 \
    --env POSTGRES_USER='postgres' \
    --env POSTGRES_PASS='example' \
    --name GDD_PySpark_Dataloader \
    godatadriven/pyspark:latest \
        --master 'local[2]' \
        --conf 'spark.driver.memory=2g' \
        --packages 'org.postgresql:postgresql:42.2.2' \
        /job/pyspark_OpenDataRWD_csv_to_postges.py ${data_filename}

echo 'Create a primary key for quick query "voertuigen"'
docker exec -it postgres psql -U postgres -c "ALTER TABLE public.voertuigen ADD CONSTRAINT voertuigen_kenteken_pk PRIMARY KEY (kenteken);"


echo 'Create table "owners" and (re)load data from the small CSV file.'
docker exec -it postgres psql -U postgres -c "CREATE TABLE IF NOT EXISTS public.carowners (kenteken char(6) primary key, owner varchar(255));"
docker exec -it postgres psql -U postgres -c "TRUNCATE TABLE public.carowners;"
docker cp car-owners.csv postgres:/tmp/car-owners.csv
docker exec -it postgres psql -U postgres -c "COPY public.carowners FROM '/tmp/car-owners.csv' WITH DELIMITER '|' CSV HEADER;"

echo "~~~ Finished successfully ~~~"