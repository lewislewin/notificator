import json
from destinations.slack_destination import SlackDestination
from sources.zendesk_source import ZendeskSource

def lambda_handler(event, context):
    # Determine the source (Intercom, Zendesk, etc.)
    source_type = event['headers'].get('Source-Type')
    if source_type == 'zendesk':
        source = ZendeskSource()
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid Source-Type')
        }
    
    # Process the data
    processed_data = source.process_data(event['body'])
    
    # Define destinations
    destinations = [
        SlackDestination(),
    ]
    
    # Send notifications
    for destination in destinations:
        destination.send_notification(processed_data)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notifications sent!')
    }

if __name__ == '__main__':
    # Sample event data mimicking the incoming webhook from Zendesk
    event = {
        'headers': {
            'Host': 'd29d-82-163-154-201.ngrok.io',
            'User-Agent': 'Zendesk Webhook',
            'Content-Type': 'application/json; charset=utf-8',
            'Source-Type': 'zendesk',
            'X-Zendesk-Account-Id': '11178178',
        },
        'body': {
            'ticket': {
                'id': 35436,
                'priority': 'high',
                'status': 'open',
                'subject': 'Help, my printer is on fire!',
                'description': 'The fire is very colorful.',
                'tags': ['enterprise', 'other_tag']
            }
        },
        'httpMethod': 'POST'
    }
    
    context = {}
    
    print(lambda_handler(event, context))