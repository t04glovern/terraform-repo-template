import boto3
import json
import os

from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()
metrics = Metrics()
tracer = Tracer()


@logger.inject_lambda_context
@metrics.log_metrics
@tracer.capture_lambda_handler
def handler(event: dict, context: LambdaContext) -> dict:
    MAX_MESSAGES_PER_SECOND = os.environ.get('MAX_MESSAGES_PER_SECOND', None)

    sqs = boto3.client("sqs")

    try:
        action = event.get('Action')

        if action == "START":
            if MAX_MESSAGES_PER_SECOND is not None:
                response = sqs.start_message_move_task(
                    SourceArn=event['QueueArn'],
                    MaxNumberOfMessagesPerSecond=MAX_MESSAGES_PER_SECOND
                )
            else:
                response = sqs.start_message_move_task(
                    SourceArn=event['QueueArn']
                )

            logger.info(f"Redrive started: {json.dumps(response)}")

            return {
                'QueueArn': event['QueueArn'],
                'Status': 'INITIATED'
            }

        elif action == "CHECK":
            response = sqs.list_message_move_tasks(
                SourceArn=event['QueueArn']
            )

            logger.info(f"Redrive check response: {json.dumps(response)}")

            if 'Results' in response and len(response['Results']) == 1:
                return {
                    'QueueArn': event['QueueArn'],
                    'Status': response['Results'][0]['Status']
                }
            else:
                return {
                    'QueueArn': event['QueueArn'],
                    'Status': 'NOT_FOUND'
                }

        else:
            logger.error(f"Invalid Action: {action}")
            return {
                'QueueArn': event['QueueArn'],
                'Status': 'INVALID_ACTION'
            }

    except Exception as e:
        if action == "START":
            error_msg = f"Error starting redrive: {str(e)}"
        else:
            error_msg = f"Error checking redrive status: {str(e)}"
        
        logger.error(error_msg)
        raise e
