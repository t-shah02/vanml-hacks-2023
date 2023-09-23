# VanML Hacks 2023

# Setup
Step 1: Clone the repository
```bash
git clone https://github.com/t-shah02/vanml-hacks-2023.git
cd vanml-hacks-2023
```
Step 2: Create a virtual environment
```bash
python3 -m venv venv
```
Step 3: Install project dependencies
```
pip install -r requirements.txt
```
Step 4: Create an .env based on the provided **template.env** file
```
touch .env
```
Step 5: Launch the Jupyter notebook server from the root directory of the project
```bash
jupyter notebook
```
Step 6: Setup models and data folders (according to your .env | it is recommended to just copy the same variables in the template.env for good measure)
Note: The nested directories inside data separate the raw and processed data (in case we need to perform some additional ETL and general cleaning)
Ex from the root directory:
```bash
mkdir data
cd data
mkdir raw
mkdir processed
cd ..
mkdir models
```

# Project folders
- models: Contains all the serialized models that we train
- data: Contains both the raw and processed datasets, during our EDA and analysis I/O stage
- notebooks: Our main workspace with Jupyter 😎 

# Running the project
```bash
python3 main.py
```
Additional running details TBA

# Team Members
1. Tanish Shah
2. Jeffrey Collinson
3. Alison Rao
4. Sophie d.V.
