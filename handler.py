import json

def hello(event, context):
    event_attr = event["Records"]

    print(event_attr)

    # or you can do more processes here

    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
