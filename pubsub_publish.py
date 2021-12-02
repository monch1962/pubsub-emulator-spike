#!/usr/bin/env python
from google.cloud import pubsub
import google.api_core.exceptions

publisher = pubsub.PublisherClient()
pubsub_topic = 'projects/dummy-project/topics/test-topic'

try:
    publisher.create_topic(name=pubsub_topic)
except google.api_core.exceptions.AlreadyExists:
    print(f"Topic already exists - no need to recreate it...")

# Use publish to start shipping messages...
publisher.publish(pubsub_topic, b'Hello?')
publisher.publish(pubsub_topic, b'Is anyone there?')
