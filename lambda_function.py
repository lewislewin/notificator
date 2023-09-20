import json
from destinations.slack_destination import SlackDestination
from sources.zendesk_source import ZendeskSource

def lambda_handler(event, context):
    # Determine the source (Intercom, Zendesk, etc.)
    source_type = event['headers'].get('Source-Type')
    if source_type == 'Zendesk':
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
    print(lambda_handler(None, None))