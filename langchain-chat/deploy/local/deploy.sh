#!/bin/bash

# Load environment value
set -a
source .env
set +a

# Define variables
LOG_DIR=./deploy
LOG_FILE=$LOG_DIR/docker.log
mkdir -p $LOG_DIR

# Submit a build to Google Cloud Build
gcloud builds submit --project $PROJECT_ID --tag gcr.io/$PROJECT_ID/$IMAGE_NAME >> $LOG_FILE

# Deploy to Google Cloud Run
gcloud run deploy $PROJECT_ID \
  --image gcr.io/$PROJECT_ID/$IMAGE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated >> $LOG_FILE

# Allow unauthenticated access
# gcloud run services add-iam-policy-binding $IMAGE_NAME \
#   --region $REGION \
#   --member="allUsers" \
#   --role="roles/run.invoker" >> $LOG_FILE
