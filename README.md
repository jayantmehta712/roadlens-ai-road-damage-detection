# RoadLens — online deployment

AI road-damage classification with PyTorch ResNet18, OpenCV, Flask, location-linked inspections, review history and reports.

This repository contains the exact runnable source in **roadlens-source.zip** and the genuine trained checkpoint split into six files to fit GitHub browser-upload limits. It is not a fake browser-only detector. `prepare_deploy.py` verifies SHA-256 checksums, extracts the source to `service/`, and reconstructs `service/models/road_damage_model.pth` during deployment.

## Deploy on Render

Create a Blueprint using render.yaml. It declares one **Free** Python web service and automatically generated SECRET_KEY and APP_PASSWORD environment values. No paid disk/database is declared. Open the resulting HTTPS URL; the workspace password is the APP_PASSWORD value in the Render service's Environment section. Never commit or publicly post that value.

Build: `python prepare_deploy.py && pip install -r service/requirements.txt && python service/scripts/check_model.py`

Start: `gunicorn -c service/gunicorn.conf.py --chdir service app:app`

The free instance can sleep and lose uploaded images/history on sleep, restart or redeploy. Export records before that occurs. Persistent hosting requires a separately approved storage plan. This is an academic demonstration, not field-validated safety software.

## Actual measured baseline

Training: 560 real RDD2022 images; validation: 120; test: 119. Held-out test accuracy: **63.87%**. Macro F1: **61.86%**. All six API tests passed. Country and class are correlated in the subset; see `models/MODEL_CARD.md` inside the source archive. No normal-road class, bounding boxes, automated severity, or object-detection mAP is claimed.

The source archive includes the full application README, model card, genuine evaluation charts, tests and third-party notices. Training data is excluded from this deployment repository; the original downloadable project bundle contains the exact data split and source XML annotations.

RDD2022: Arya et al., https://doi.org/10.6084/m9.figshare.21431547 (CC BY 4.0 per the release metadata). The bundled sample road image is attributed in DATASET_ATTRIBUTION.md inside the source archive.

Project team: Jayant Mehta, Kavya, Kashish Vohra and Ayush Sharma. Dronacharya Group of Institutions, academic session 2026–27.

