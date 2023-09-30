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
    processed_data = source.process_data(json.loads(event['body']))
    
    if not processed_data:
        return {
            'statusCode': 200,
            'body': json.dumps('No notifications sent')
        }
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
            # ... other headers
        },
        'body': r'''{ "current_user": { "details": "", "email": "lewis.lewin@patchworks.co.uk", "external_id": "", "first_name": "Lewis", "language": "English (UK)", "name": "Lewis", "notes": "", "phone": "", "organization": { "details": "", "name": "Patchworks", "notes": "" } }, "satisfaction": { "current_comment": "", "current_rating": "" }, "ticket": { "account": "Patchworks", "assignee": { "email": "lewis.lewin@patchworks.co.uk", "first_name": "Lewis", "last_name": "Lewis", "name": "Lewis" }, "brand": { "name": "Patchworks" }, "cc_names": "", "ccs": "[]", "current_holiday_name": "", "description": "----------------------------------------------\n\nLewis, 28 Sept 2023, 20:02\n\nlewis test ticket\n\nThanks,\nLewis.", "due_date": "", "external_id": "", "group": { "name": "Tier 3" }, "id": "13107", "latest_comment_html": "----------------------------------------------\n\ntest\n\nThanks,\nLewis.", "latest_public_comment_html": "----------------------------------------------\n\nLewis, 29 Sept 2023, 23:01\n\ntest\n\nThanks,\nLewis.", "organization": { "details": "", "external_id": "", "name": "Patchworks", "notes": "" }, "priority": "", "requester": { "details": "", "email": "lewis.lewin@patchworks.co.uk", "external_id": "", "first_name": "Lewis", "language": "English (UK)", "last_name": "Lewis", "name": "Lewis", "phone": "", "requester_field": "" }, "status": "Open", "tags": "some enterprise_", "ticket_type": "Ticket", "title": "test", "url": "gopatchworks.zendesk.com/agent/tickets/13107", "via": "Web Form" } }''',
        'httpMethod': 'POST'
    }
    
    context = {}
    
    print(lambda_handler(event, context))