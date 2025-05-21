import boto3
import time

# AWS-Client für Redshift Data API
client = boto3.client('redshift-data', region_name='eu-central-1')  # Region ggf. anpassen

# Parameter
cluster_id = 'mein-redshift-cluster'         # Oder bei Serverless: workgroup_name
database = 'mein_datenbankname'
db_user = 'mein_db_user'                     # Optional bei Serverless
sql = 'SELECT current_date;'

# SQL ausführen
response = client.execute_statement(
    ClusterIdentifier=cluster_id,
    Database=database,
    DbUser=db_user,
    Sql=sql
)

# Abfrage-ID
query_id = response['Id']
print(f"Query ID: {query_id}")

# Warten auf das Ergebnis
while True:
    status = client.describe_statement(Id=query_id)
    if status['Status'] in ['FINISHED', 'FAILED', 'ABORTED']:
        break
    time.sleep(1)

# Ergebnis abrufen
if status['Status'] == 'FINISHED':
    result = client.get_statement_result(Id=query_id)
    print("Ergebnis:", result['Records'])
else:
    print("Fehler oder Abbruch:", status['Error'])
