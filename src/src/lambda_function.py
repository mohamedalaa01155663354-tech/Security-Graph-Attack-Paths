import json
import os

import boto3

from attack_paths import (
    build_graph,
    find_attack_paths,
    compare_paths,
    to_cytoscape,
)
s3 = boto3.client("s3")
def _load_json_from_s3(bucket, key):
    response = s3.get_object(
        Bucket=bucket,
        Key=key,
    )

    return json.loads(
        response["Body"].read().decode("utf-8")
    )
  def _save_json_to_s3(bucket, key, data):
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(data, indent=2).encode("utf-8"),
        ContentType="application/json",
    )
def lambda_handler(event, context):
  
