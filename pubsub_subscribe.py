#!/usr/bin/env python
from google.cloud import pubsub
import google.api_core.exceptions

subscriber = pubsub.SubscriberClient()
pubsub_topic = 'projects/dummy-project/topics/test-topic'
sub_name = 'projects/dummy-project/subscriptions/subslot123'

try:
    subscriber.create_subscription(name=sub_name, topic=pubsub_topic)
except google.api_core.exceptions.AlreadyExists:
    print(f"Subscription already exists - no need to recreate it...")

# Blocking call to start listening. Passes all messages to print method
subscriber.subscribe(sub_name, print).result()
