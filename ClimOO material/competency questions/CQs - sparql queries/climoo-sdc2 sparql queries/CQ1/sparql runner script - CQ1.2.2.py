from rdflib import Graph
import csv

# -----------------------------
# RDF files to load
# -----------------------------
rdf_files = [
    "/Users/f.u./Desktop/ClimOO-Ontology/ClimOO material/competency questions/CQs - sparql queries/climoo-sdc2 sparql queries/CQ1/climoo-sdc2-inferred-hierarchies-2026-09-14.ttl"
    
    # add more files here
]
# This script has been run on Giorgio A. Ubbiali's local version of ClimOO-SDC2. Please ensure you change the IRI to your local version.

# -----------------------------
# Create graph and load files
# -----------------------------
g = Graph()

for file in rdf_files:
    print(f"Loading {file}...")
    
    # rdflib often guesses format, but explicit is safer:
    if file.endswith(".ttl"):
        g.parse(file, format="turtle")
    elif file.endswith(".rdf") or file.endswith(".xml"):
        g.parse(file, format="xml")
    elif file.endswith(".nt"):
        g.parse(file, format="nt")
    else:
        g.parse(file)

print(f"Loaded {len(g)} triples")

# -----------------------------
# SPARQL query
# -----------------------------
query = """
PREFIX ClimOO: <https://www.w3id.org/climoo/climoo-sdc2#>
PREFIX SCO: <https://www.w3id.org/sco#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT ?perspective ?perspectiveLabel ?perspectiveDescription
WHERE {
    ClimOO:ClimOO_0000302 SCO:SCO_0000039 ?perspective .
    ?perspective rdfs:label ?perspectiveLabel .
   OPTIONAL {
        ?perspective dcterms:description ?perspectiveDescription .
    }
}
"""

# -----------------------------
# Run query
# -----------------------------
results = g.query(query)

# -----------------------------
# Export to CSV
# -----------------------------
output_file = "results.csv"

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # write header
    writer.writerow(results.vars)

    # write rows
    for row in results:
        writer.writerow([str(value) for value in row])

print(f"Results written to {output_file}")