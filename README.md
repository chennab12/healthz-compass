# Health Compass

A Streamlit dashboard of curated general adult health education. It offers an overview with ten essentials, eight self-contained topic tabs with evidence-linked facts, metrics, optional session-only trackers, action checklists and FAQs, routine scenarios and linked sources. Content is static and reviewed as of September 25, 2026; it does not ingest current news or personal medical records.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

For Streamlit Community Cloud, upload these files to a GitHub repository, select `app.py` as the entry point, and deploy. No API key is needed.

## Scope

Guidelines are linked in each tab. Routine sliders use only local Streamlit session state and compare values with general adult recommendations; they do not estimate medical risk. Review clinical facts and links periodically before relying on them. This is educational software, not a clinical decision tool.
