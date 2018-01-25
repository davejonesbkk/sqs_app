import boto3

sqs_msg = boto3.resource('sqs')

sqs_queue = sqs_msg.get_queue_by_name(QueueName='TradeStatus.fifo')

try:
	userInput = raw_input("Enter the file name: ")
except NameError:
	pass 

with open(userInput, 'r') as fp:
	data=fp.read()

response = queue.send_message(
	MessageBody=data,
	MessageGroupId='messageGroup1'
)

print(response.get('MessageId'))
print(response.get('MD50MessageBody'))

