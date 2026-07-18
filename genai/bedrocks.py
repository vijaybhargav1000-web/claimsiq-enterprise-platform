import json
import boto3

from prompts import CLAIM_SUMMARY_PROMPT


bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="ap-south-1"
)

MODEL_ID = "meta.llama3-70b-instruct-v1:0"


def analyze_claim(claim):

    prompt = CLAIM_SUMMARY_PROMPT.format(
        claim=claim
    )

    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5
    }

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(
        response["body"].read()
    )

    return result["generation"]
