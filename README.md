# Health Compass

A Streamlit dashboard of curated general adult health education. It offers ten essentials, a rotating evidence-linked daily fact, a dated metric timeline with CSV export/import, a weekly habits view, an appointment summary download, eight self-contained topic tabs, scenarios and sources. Content is static and reviewed as of September 25, 2026; it does not ingest current news or fetch personal medical records.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

For Streamlit Community Cloud, upload these files to a GitHub repository, select `app.py` as the entry point, and deploy. No API key is needed.

## Scope

Guidelines are linked in each tab. Inputs are stored in Streamlit server session memory and sent to the server while the app is in use; no database or account storage is implemented. Download your measurements as CSV and upload it on a future visit. The appointment summary is generated on demand. Do not deploy with analytics that collect health inputs unless you have assessed privacy and security requirements. Routine sliders compare values with general adult recommendations; they do not estimate medical risk. Review clinical facts and links periodically before relying on them. This is educational software, not a clinical decision tool.
