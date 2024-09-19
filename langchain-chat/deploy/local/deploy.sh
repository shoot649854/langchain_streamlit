#!/bin/bash

# Load environment value
set -a
source .env
set +a

# Define variables
LOG_DIR=./deploy
LOG_FILE=$LOG_DIR/docker.log

# Create the log directory if it doesn't exist
mkdir -p $LOG_DIR

# # Build the Docker image
# docker build -t $IMAGE_NAME .

# # Run the Docker container, mapping port 8080 to 8080
# docker run -p 8080:8080 $PROJECT_ID

# Submit a build to Google Cloud Build
gcloud builds submit --project $PROJECT_ID --tag gcr.io/$PROJECT_ID/$IMAGE_NAME >> $LOG_FILE

# Deploy to Google Cloud Run
gcloud run deploy $PROJECT_ID \
  --image gcr.io/$PROJECT_ID/$IMAGE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated >> $LOG_FILE

# Allow unauthenticated access
gcloud run services add-iam-policy-binding $IMAGE_NAME \
  --region $REGION \
  --member="allUsers" \
  --role="roles/run.invoker" >> $LOG_FILE
