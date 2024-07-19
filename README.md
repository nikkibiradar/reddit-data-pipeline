# reddit-data-pipeline
# Reddit DataForge
This repository contains a data engineering pipeline to extract, transform, and load (ETL) Reddit data using various tools and frameworks such as AWS, Apache Airflow, and Python.

## Project Overview

The goal of this project is to build a robust and scalable data pipeline that automates the process of collecting Reddit data, transforming it, and storing it in AWS S3 for further analysis.

## Features

- **Data Extraction:** Fetches posts from Reddit using PRAW.
- **Data Transformation:** Processes and cleans the data, including handling data types and missing values.
- **Data Loading:** Saves the processed data to CSV files.
- **Error Handling and Retry Mechanisms:** Implements exception handling and retry logic to manage API request failures and ensure data consistency.
- **Scheduling:** Uses Apache Airflow for task scheduling and orchestration.

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

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PRAW
- Apache Airflow
- Docker
- Pandas
- NumPy

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/reddit-data-pipeline.git
    ```

2. Navigate to the project directory:

    ```bash
    cd reddit-data-pipeline
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```
4. Setting Up Airflow:
  * Initialize the Airflow database:
    ```plaintext
    airflow db init
    ```
  * Start the Airflow web server and scheduler:
    ```plaintext
    airflow webserver --port 8080
    airflow scheduler
    ```
5. Using Docker:
  * Build the Docker image:
  ```plaintext
  docker build -t reddit-etl:latest .
  ```
  * Start the services using Docker Compose:
    ```plaintext
    docker compose up -d --build
    ```    
6. Running the Pipeline:
  * Trigger the DAG defined in reddit_dag.py from the Airflow web UI or CLI.
  * The DAG orchestrates the following steps:
    * Extracting data from Reddit using the reddit_pipeline.py
    * Transforming the data using reddit_etl.py
    * Loading the transformed data to AWS S3 using aws_s3_pipeline.py and aws_etl.py
      
### Configuration

Update the `config/config.conf` file with your Reddit API credentials and AWS S3 credentials. Ensure this file is excluded from version control to keep your credentials secure.

### Retry Mechanism

The pipeline includes retry logic for handling API request failures:

- **Retry Attempts:** Configured to retry on server errors (HTTP 500) up to a specified number of times.
- **Backoff Strategy:** Exponential backoff is used between retries to avoid overwhelming the server.

### Error Handling

The pipeline handles common errors such as:

- **Connection Errors:** Managed by retrying the request.
- **Data Transformation Errors:** Logs errors and continues processing.

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
