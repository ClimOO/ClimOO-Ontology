# Competency Questions (CQs) - SPARQL queries

## Description

This directory contains [SPARQL](https://www.w3.org/TR/sparql11-query/) queries translating ClimOO CQs for ontology validation, and a virtual environment for running them. Each folder is dedicated to one of the ClimOO suite modules. 
Each folder includes:

- A list of the CQs, in natural language, in a markdown format.
- Dedicated subfolders for each CQ, containing the SPARQL query in SPARQL format, the query runner script (adapted from [here](https://github.com/giacomodecolle/PythonRDF/blob/test/sparql_query_runner/query_runner.py)) in pythonstring format, and the query result in csv format. 

N.B. SPARQL runner scripts generate the CSV result files in the directory where the venv folder is located. We revised the result file labels manually and moved them into the appropriate folder.