poetry setup

poetry export -f requirements.txt --output requirements.txt --without-hashes

docker build check

---

| 種類         | 名前                | 値                                                                                              |
| ------------ | ------------------- | ----------------------------------------------------------------------------------------------- |
| 変数         | APP_LANGCHAIN       | langchain                                                                                       |
| 変数         | GAR_LOCATION        | asia-northeast1                                                                                 |
| シークレット | PROJECT_ID          | vaulted-zodiac-253111                                                                           |
| シークレット | RUN_SERVICE_ACCOUNT | `shoto-deploy-run@vaulted-zodiac-253111.iam.gserviceaccount.com`                                |
| シークレット | WIF_PROVIDER        | `projects/725062356319/locations/global/workloadIdentityPools/my-wi-pool/providers/my-oidc-gha` |
| シークレット | WIF_SERVICE_ACCOUNT | `shoto-deploy-gha@vaulted-zodiac-253111.iam.gserviceaccount.com`                                |

---

gcloud iam service-accounts create shoto-deploy-gha
gcloud iam service-accounts create shoto-deploy-cloudrun

gcloud iam workload-identity-pools create my-wi-pool --location="global"

gcloud iam workload-identity-pools providers create-oidc my-oidc-gha
--location="global" \
 --workload-identity-pool="my-wi-pool" \
 --issuer-uri="https://token.actions.githubusercontent.com" \
 --attribute-mapping="google.subject=assertion.sub"

<!-- vaulted-zodiac-253111
725062356319
gcloud iam service-accounts add-iam-policy-binding my-sa-gha@${GCP_PROJECT_ID}.iam.gserviceaccount.com \
--role="roles/iam.workloadIdentityUser" \
--member="principalSet://iam.googleapis.com/projects/${GCP_PROJECT_NUM}/locations/global/workloadIdentityPools/my-wi-pool/attribute.repository/${USERNAME}/${REPOSITORY}" -->

gcloud iam service-accounts add-iam-policy-binding shoto-deploy-gha@vaulted-zodiac-253111.iam.gserviceaccount.com \
 --role="roles/iam.workloadIdentityUser" \
 --member="principalSet://iam.googleapis.com/projects/725062356319/locations/global/workloadIdentityPools/my-wi-pool/attribute.repository/shoot649854/vaulted-zodiac"

<!-- gcloud iam roles create myCloudDeployRole --project="${GCP_PROJECT_ID}" --file="permissions.yaml" -->

gcloud iam roles create CloudDeployRole --project="vaulted-zodiac-253111" --file="permissions.yaml"

<!-- gcloud services enable clouddeploy.googleapis.com -->

<!-- gcloud projects add-iam-policy-binding ${GCP_PROJECT_ID} \
--member="serviceAccount:shoto-deploy-gha@${GCP_PROJECT_ID}.iam.gserviceaccount.com" \
--role="projects/${GCP_PROJECT_ID}/roles/myCloudDeployRole" -->

gcloud projects add-iam-policy-binding vaulted-zodiac-253111 \
--member="serviceAccount:shoto-deploy-gha@vaulted-zodiac-253111.iam.gserviceaccount.com" \
--role="projects/vaulted-zodiac-253111/roles/CloudDeployRole"

gcloud projects add-iam-policy-binding vaulted-zodiac-253111 \
 --member="serviceAccount:shoto-deploy-gha@vaulted-zodiac-253111.iam.gserviceaccount.com" \
 --role="roles/iam.serviceAccountTokenCreator"

gcloud projects add-iam-policy-binding vaulted-zodiac-253111 \
 --member="serviceAccount:shoto-deploy-gha@vaulted-zodiac-253111.iam.gserviceaccount.com" \
 --role="roles/iam.workloadIdentityUser"

gcloud projects add-iam-policy-binding vaulted-zodiac-253111 \
 --member="serviceAccount:shoto-deploy-gha@vaulted-zodiac-253111.iam.gserviceaccount.com" \
 --role="roles/iam.serviceAccountTokenCreator"

gcloud projects add-iam-policy-binding vaulted-zodiac-253111 \
 --member="serviceAccount:shoto-deploy-gha@vaulted-zodiac-253111.iam.gserviceaccount.com" \
 --role="roles/clouddeploy.operator"

gcloud projects add-iam-policy-binding vaulted-zodiac-253111 \
 --member="serviceAccount:shoto-deploy-gha@vaulted-zodiac-253111.iam.gserviceaccount.com" \
 --role="roles/clouddeploy.admin"

<!-- Artifact Registryの作成 -->

gcloud artifacts repositories create langchain --repository-format="docker" --location="asia-northeast1"

gcloud artifacts repositories add-iam-policy-binding langchain \
--location="asia-northeast1" \
--member="serviceAccount:shoto-deploy-gha@vaulted-zodiac-253111.iam.gserviceaccount.com" \
--role="roles/artifactregistry.writer"
