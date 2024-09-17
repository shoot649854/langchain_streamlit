#!/bin/bash

# Define log variables
LOG_DIR=./deploy
LOG_FILE=$LOG_DIR/docker_logs.txt

# Create the log directory if it doesn't exist
mkdir -p $LOG_DIR

# Add debug logging to check environment variables
echo "PROJECT_ID: $PROJECT_ID"
echo "IMAGE_NAME: $IMAGE_NAME"
echo "REGION: $REGION"

# Check if variables are missing
if [ -z "$PROJECT_ID" ] || [ -z "$IMAGE_NAME" ] || [ -z "$REGION" ]; then
  echo "Missing required environment variables."
  exit 1
fi


# Submit a build to Google Cloud Build
gcloud builds submit --project $PROJECT_ID --tag gcr.io/$PROJECT_ID/$IMAGE_NAME --quiet >> $LOG_FILE

# Deploy to Google Cloud Run
gcloud run deploy $IMAGE_NAME \
  --image gcr.io/$PROJECT_ID/$IMAGE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated --quiet >> $LOG_FILE
