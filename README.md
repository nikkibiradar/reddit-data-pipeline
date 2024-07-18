# reddit-data-pipeline

This repository contains a data engineering pipeline to extract, transform, and load (ETL) Reddit data using various tools and frameworks such as AWS, Apache Airflow, and Python.

## Project Overview

The goal of this project is to build a robust and scalable data pipeline that automates the process of collecting Reddit data, transforming it, and storing it in AWS S3 for further analysis.

## Project Structure

```plaintext
├── reddit_dag.py              # Apache Airflow DAG for orchestrating the pipeline
├── aws_etl.py                 # ETL script for AWS services
├── reddit_etl.py              # ETL script for Reddit data
├── aws_s3_pipeline.py         # Pipeline for handling AWS S3 operations
├── reddit_pipeline.py         # Pipeline for handling Reddit data extraction
├── constants.py               # Constants and configurations used across the project
├── config.conf                # Configuration file for the project
├── reddit_20240716.csv        # Sample CSV data extracted from Reddit
├── requirements.txt           # Python dependencies
├── airflow.env                # Environment variables for Airflow
├── docker-compose.yml         # Docker Compose file for setting up the environment
├── Dockerfile                 # Dockerfile for containerizing the project
└── README.md                  # Project documentation
```
## Requirements
* To install the required dependencies, run:
 ```plaintext
 pip install -r requirements.txt
 ```
 Or
 ```plaintext
 pip freeze > requirements.txt
 ```
* To create necessary folders, run:
  ```plaintext
  mkdir config dags data etls logs pipelines tests utils
  ```
## Configuration
Ensure the config.conf file is properly configured with the necessary credentials and settings for Reddit API and AWS services.

## Usage

1. Setting Up Airflow:
  * Initialize the Airflow database:
    ```plaintext
    airflow db init
    ```
  * Start the Airflow web server and scheduler:
    ```plaintext
    airflow webserver --port 8080
    airflow scheduler
    ```
2. Using Docker:
  * Build the Docker image:
  ```plaintext
  docker build -t reddit-etl:latest .
  ```
  * Start the services using Docker Compose:
    ```plaintext
    docker compose up -d --build
    ```    
3. Running the Pipeline:
  * Trigger the DAG defined in reddit_dag.py from the Airflow web UI or CLI.
  * The DAG orchestrates the following steps:
    * Extracting data from Reddit using the reddit_pipeline.py
    * Transforming the data using reddit_etl.py
    * Loading the transformed data to AWS S3 using aws_s3_pipeline.py and aws_etl.py

## What I Did

In this project, I developed a comprehensive data pipeline to handle Reddit data. The key tasks I undertook include:

* Designing and implementing an Apache Airflow DAG to orchestrate the ETL process.
* Writing Python scripts for extracting data from the Reddit API, transforming the data into a usable format, and loading it into AWS S3.
* Configuring AWS services to store and manage the data efficiently.
* Ensuring the pipeline is scalable and robust to handle large volumes of data.
* Setting up a containerized environment using Docker and Docker Compose to simplify deployment and management.

## Outcomes/Results
The project successfully automated the entire data pipeline process, resulting in:

* Efficient and timely extraction of data from Reddit.
* Seamless transformation and cleaning of the extracted data.
* Reliable storage of the processed data in AWS S3, making it readily available for further analysis.
* Significant reduction in manual intervention, leading to improved productivity and data accuracy.

## Insights Gained:
Working on this project provided me with valuable insights and experience in:

* Building and managing scalable data pipelines using Apache Airflow.
* Integrating various AWS services for data storage and management.
* Enhancing my Python programming skills, particularly in data extraction and transformation.
* Understanding the intricacies of working with APIs and handling large datasets.
* Improving my problem-solving abilities and gaining practical experience in data engineering.
* Setting up and managing containerized environments using Docker.

## Scripts

**'reddit_dag.py'**  
Defines the Apache Airflow DAG for orchestrating the entire ETL pipeline.

**'aws_etl.py'**  
Contains the ETL logic for interacting with AWS services, such as uploading data to S3.

**'reddit_etl.py'**  
Handles the extraction and transformation of Reddit data.

**'aws_s3_pipeline.py'**  
Manages the operations related to AWS S3, including uploading and downloading data.

**'reddit_pipeline.py'**  
Manages the process of extracting data from the Reddit API.

**'constants.py'**  
Defines constants and configuration variables used throughout the project.

**'config.conf'**  
Configuration file containing API keys, AWS credentials, and other settings.

**'reddit_20240716.csv'**  
Sample dataset extracted from Reddit for testing and demonstration purposes.

**'airflow.env'**  
Environment variables for Airflow.

**'docker-compose.yml'**  
Docker Compose file for setting up the environment.

**'Dockerfile'**  
Dockerfile for containerizing the project.
