# hcl_project
HCL Project – Marketing Campaign Data Analysis

Project Overview

This project focuses on data cleaning, Exploratory Data Analysis (EDA), and basic data analysis of a Marketing Campaign dataset using Python and Pandas.

The main objective is to clean and organize customer data, handle missing values and duplicates, create meaningful features, and analyze customer information to gain useful insights.

Tools & Technologies Used

- Python
- Pandas
- CSV Dataset
- GitHub

Project Workflow

1. Data Loading

- Imported the Pandas library.
- Loaded the Marketing Campaign dataset using "read_csv()".

2. Exploratory Data Analysis (EDA)

- Displayed the first and last rows of the dataset.
- Checked dataset shape, columns, and data types.
- Used "info()" and "describe()" for data understanding.
- Examined unique values and value counts.

3. Data Cleaning

- Identified and handled missing values.
- Filled missing income values using the median.
- Converted customer date into datetime format.
- Removed duplicate records.
- Standardized inconsistent categories in Education and Marital Status.
- Removed unnecessary columns and filtered invalid records.

4. Feature Engineering

- Created a new column "Total_Children" by combining Kidhome and Teenhome.
- Created "Total_Spending" by combining spending across different product categories.

5. Data Selection

- Used "loc" and "iloc" to select specific rows and columns.
- Displayed relevant customer information.

6. Basic Data Analysis

- Calculated average customer income.
- Calculated average total spending.
- Analyzed customers based on education.
- Analyzed customers based on marital status.

7. Exporting Cleaned Data

- Exported the cleaned dataset into a new CSV file named "Final_cleaned_marketing.csv".

Conclusion

This project demonstrates the complete basic data preprocessing workflow, from loading raw data to cleaning, transforming, and analyzing it. It helps improve data quality and makes the dataset more suitable for further analysis and decision-making.
