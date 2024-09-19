#!/bin/bash

# Define log variables
LOG_DIR=./deploy
LOG_FILE=$LOG_DIR/docker.log
mkdir -p $LOG_DIR

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
