#!/usr/bin/env bash

docker run -it --rm -p 8085:8085 gcr.io/google.com/cloudsdktool/cloud-sdk gcloud beta emulators pubsub start --host-port=0.0.0.0:8085