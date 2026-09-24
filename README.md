# Apollo Data Mining & Contact Quality Analysis

## Project goal
This project turns Apollo.io contact exports into a small, portfolio-ready data analytics project.

### What this demonstrates
- Data collection and export
- CSV data cleaning
- Data-quality validation
- Email-status analysis
- Company and job-title analysis
- Basic visualization
- Streamlit dashboarding

## Dataset used for this analysis
The internship export contained:
- **25 contacts**
- **19 Verified**
- **4 Unavailable**
- **2 Extrapolated**
- Location: **Saratoga, California**
- Industry in the export: **Real Estate**

Verified-contact rate: **76.0%**

## Important privacy note
Do **not** upload real Apollo contact names, email addresses, phone numbers, or other personal/business contact data to a public GitHub repository unless you have explicit authorization.

The included `sample_anonymized_contacts.csv` removes direct personal identifiers and is intended for a portfolio/demo repository.

## How to run the Python analysis
1. Install dependencies:
   `pip install -r requirements.txt`
2. Put your authorized Apollo CSV in this folder and name it `apollo_contacts.csv`.
3. Run:
   `python apollo_data_mining_analysis.py`

## How to run the dashboard
`python -m streamlit run dashboard.py`

## Possible project title for CV/GitHub
**Business Contact Data Mining & Data Quality Analysis using Apollo.io, Python and Streamlit**

## Skills demonstrated
Python, Pandas, CSV processing, data cleaning, data validation, exploratory analysis, visualization, Streamlit.
