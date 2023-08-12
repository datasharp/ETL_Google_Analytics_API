# Google Analytics ETL and Data Visualization


Welcome to the Google Analytics ETL and Data Visualization project repository! This repository showcases a Python-based ETL pipeline for extracting data from the Google Analytics API, performing data cleaning and transformation, creating data visualizations using Matplotlib and Seaborn, and storing the processed data in a MySQL database. The project is organized in a modular structure to facilitate extensibility and maintainability.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Google Analytics ETL and Data Visualization project is a demonstration of an end-to-end data processing pipeline. It is designed to showcase how data can be extracted from the Google Analytics API, transformed and cleaned, visualized using graphs, and then stored in a MySQL database for analysis.
The project's structure is built around modular scripts, each responsible for a specific aspect of the ETL process. This modular approach offers several benefits:

Modularity: Each script focuses on a particular task, making the codebase organized, maintainable, and easy to understand.

Reusability: Modular scripts can be reused in other projects or extended with minimal changes.

Collaboration: Team members can work on different modules simultaneously, enhancing collaboration.


## Project Structure

The repository is structured as follows:

- `src/`: Directory containing the modular Python scripts.
  - `scrape.py`: Script for data extraction from Google Analytics API.
  - `scraper_day_index.py`: Script for adding day index to data.
  - `cleaning.py`: Data cleaning and transformation scripts.
  - `visualize.py`: Data visualization scripts using Matplotlib and Seaborn.
  - `upload_mysql_func.py`: Script for uploading data to MySQL database.
- `config.example.json`: Configuration file (API keys, database credentials, etc.).
- `requirements.txt`: List of required Python packages.
- `main.py`: The main script demonstrating the usage of the modular scripts.

## Configuration

Although the project can't be executed due to missing API keys, you can study the `config.example.json` file to understand how to set up your API credentials, database connection, and other configuration details.

## Usage

The `main.py` script acts as an entry point to demonstrate the complete ETL process. It showcases data extraction, cleaning, transformation, visualization, and database storage.
