#!/bin/bash

# Load environment value
set -a
source .env
set +a

# Define variables
GCP_DIR=~/.gcp/credentials
GCP_LOG_FILE=$GCP_DIR/gcp.log
mkdir -p $GCP_DIR
cd $GCP_DIR

# Ensure the service account environment variable is set
if [ -z "$GCP_SERVICE_ACCOUNT" ]; then
  echo "Error: GCP_SERVICE_ACCOUNT is not set."
  exit 1
fi

# Create the service account key
gcloud iam service-accounts keys create credential \
  --iam-account="$GCP_SERVICE_ACCOUNT" >> $GCP_LOG_FILE

echo "Service account key created for $GCP_SERVICE_ACCOUNT."
