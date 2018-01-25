import boto3 

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='TradeStatus.fifo')

for message in queue.receive_messages():
	print('Hello, {0}'.format(message.body))

	message.delete()

	