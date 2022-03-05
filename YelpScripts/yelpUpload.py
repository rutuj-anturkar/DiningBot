pip install dynamodb_json
import json
import dynamodb_json
from dynamodb_json import json_util as json2
import boto3
from datetime import datetime
from decimal import Decimal

session = boto3.Session(
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name="us-east-1"
)

def create_restaurant_table(dynamodb=None):
    if not dynamodb:
        dynamodb = session.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='yelp-restaurants',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
     
    )
    return table


if __name__ == '__main__':
    restaurant_table = create_restaurant_table()
    print("Table status:", restaurant_table.table_status)

def load_restaurant(restaurant, dynamodb=None):
    if not dynamodb:
        dynamodb = session.resource('dynamodb')

    table = dynamodb.Table('yelp-restaurants')
    for rest in restaurant:
        dateTimeObj = datetime.now()
        rest['insertedAtTimestamp'] = str(dateTimeObj)
        table.put_item(Item=rest)


if __name__ == '__main__':
    with open("Italiandata.json") as json_file:
        list_of_restaurants = json.load(json_file, parse_float=Decimal)
    load_restaurant(list_of_restaurants)
