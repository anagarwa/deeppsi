# deeppsi

# Lighthouse Aggregator

## Purpose

This repository provides a tool to run Lighthouse multiple times on a given URL and aggregate the results. It helps in obtaining a more stable and accurate measurement of web performance metrics by averaging multiple Lighthouse runs.

## Installation

1. Install Lighthouse CLI using the following command:
   ```sh
   npm install -g lighthouse
2. ```sh 
  lighthouse --version

## Setup
Copy and paste lighthouse_aggregator.py into your local machine.

Running the Aggregator Script
Run the aggregator script with the following command:

```sh
python3 lighthouse_aggregator.py "<url>" --runs <numOfTimesItNeedToRun>

Example
```sh
python3 lighthouse_aggregator.py "https://main--icicidirect--aemsites.hlx.live/research/equity?delayMartech=0" --runs 10

## Output
Reports of each individual run and the aggregated report are saved in the folder lighthouse_reports.

Sample Final Report
The aggregated report looks like this:
```sh
{
  "averages": {
    "FCP": 1867.02733,
    "SI": 3717.0955303741625,
    "LCP": 1931.37559,
    "TTI": 12648.0222525,
    "TBT": 455.8999999999998,
    "CLS": 0.06706501365391375,
    "performance": 0.84,
    "accessibility": 0.6930000000000001,
    "best-practices": 0.75,
    "seo": 0.77
  }
}


This report is an average of the number of runs provided in the command.


