# NLP-CONSUMER-COMPLAINT

## Problem Statement
Consumer complaints provide valuable feedback to businesses. Manually analysing and categorising these complaints, on the other hand, can be time-consuming and error-prone.
[The Consumer Financial Protection Bureau (CFPB)](https://www.consumerfinance.gov/data-research/consumer-complaints/) is a federal U.S. agency that acts as a mediator between financial institutions and consumers when disputes arise. Consumers can file complaints using a web form. As a result, an automated solution is needed to process and categorize consumer complaints based on their content. 


## Solution
This project will attempt to predict whether a consumer will file a dispute after the company has responded to his or her complaint. The model is trained on a dataset of consumer complaints in order to recognize and categorize them. The steps are as follows:

1. Extract the data from CFPB API and load it in required format: JSON to PARQUET file
2. Pre-process the data and feature extraction: KNN imputer and SMOTE
3. Train machine learning models for the classification: CatBoost
4. Deply on AWS

### Scope of this application:
Companies can use this application to prioritize their work and focus more on issues that are likely to spark a dispute saving both time and money.

## Similar Applications
* [CIVICA for UK](https://www.civica.com/en-gb/site-search-results/?aspxerrorpath=/en-gb/product-pages/case-management-software/toolkits-and-resources)
* [RBI Complaints](https://rbi.org.in/Scripts/Complaints.aspx)

## Tech Stack Used:
* Python
* PySpark
* PySpark ML
* Airflow as Scheduler
* MongoDB

## Please refer flowcharts folder for further details
