# pubsub-emulator-spike
Spike to investigate how to locally test GCP PubSub integration with GCP Cloud Functions

## Setup

`$ python3 -m venv spike`
`$ source spike/bin/activate`
`$ pip install -f requirements.txt`

to create a clean Python virtual environment and install dependencies

Then 

`$ ./start-pubsub-emulator`

to pull & run a PubSub emulation environment inside Docker. This will be exposed on TCP/8085

## Run

`$ PUBSUB_EMULATOR_HOST=localhost:8085 ./pubsub_publish.py `

will load some sample messages into the PubSub emulator.

Running

`$ PUBSUB_EMULATOR_HOST=localhost:8085 ./pubsub_subscribe.py`

in a separate shell will let you view those messages.
