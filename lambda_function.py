
import json
import boto3
from decimal import Decimal

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')

def lambda_handler(event, context):
    # Increment the visit count in DynamoDB
    response = table.update_item(
        Key={'VisitorId': 'visit_count'},
        UpdateExpression='ADD #count :increment',
        ExpressionAttributeNames={'#count': 'count'},
        ExpressionAttributeValues={':increment': Decimal(1)},
        ReturnValues='UPDATED_NEW'
    )
    # Retrieve updated count
    count = response['Attributes']['count']
    # Return response as JSON
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": {"count": int(count)}
    }
