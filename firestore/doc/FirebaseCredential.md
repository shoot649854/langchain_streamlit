```bash
gcloud iam service-accounts create [SERVICE-ACCOUNT]
```

```bash
gcloud projects add-iam-policy-binding [PROJECT-ID]
    --member="serviceAccount:[SERVICE-ACCOUNT]@[PROJECT-ID].iam.gserviceaccount.com" \
    --role="roles/datastore.user"
```

```bash
gcloud iam service-accounts keys create ~/.gcp/credentials/firestore-keyfile.json
    --iam-account=[SERVICE-ACCOUNT]@[PROJECT-ID].iam.gserviceaccount.com
```
