"""Session-only trackers and exportable user data for the Health Compass app."""
import csv
import io
from datetime import date, timedelta

import streamlit as st
import pandas as pd

from knowledge import GUIDES

METRIC_UNITS = {
    "Blood pressure systolic": "mm Hg", "Blood pressure diastolic": "mm Hg",
    "A1c": "%", "Fasting glucose": "mg/dL", "LDL cholesterol": "mg/dL",
    "Sleep": "hours/night", "Moderate activity": "minutes/week", "Body weight": "lb",
}
FIELDS = ["date", "metric", "value", "unit"]


def _records():
    return st.session_state.setdefault("health_records", [])


def _csv_bytes(records):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(records)
    return output.getvalue().encode("utf-8")


def timeline():
    st.header("📊 My metric timeline")
    st.caption("Your entries live in this Streamlit session. Download a CSV to keep them; import it on a later visit. The server receives entered and uploaded data during use. Avoid using this on a shared device.")
    upload = st.file_uploader("Restore a previously downloaded Health Compass CSV", type=["csv"], key="history_upload")
    if upload is not None and st.button("Import CSV (replaces current session entries)"):
        try:
            payload = upload.getvalue()
            if len(payload) > 1_000_000:
                raise ValueError("File exceeds 1 MB")
            reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig")))
            if reader.fieldnames != FIELDS:
                raise ValueError("Use a CSV exported by this app")
            rows = []
            for row in reader:
                if len(rows) >= 1000 or row["metric"] not in METRIC_UNITS or row["unit"] != METRIC_UNITS[row["metric"]]:
                    raise ValueError("Unsupported metric, unit or too many rows")
                date.fromisoformat(row["date"])
                value = float(row["value"])
                if not 0 <= value <= 100000 or value != value:
                    raise ValueError("Invalid value")
                rows.append({"date": row["date"], "metric": row["metric"], "value": value, "unit": row["unit"]})
            st.session_state["health_records"] = rows
            st.success(f"Imported {len(rows)} entries")
        except (ValueError, UnicodeError, TypeError, KeyError) as exc:
            st.error(f"Import failed: {exc}")
    with st.form("add_metric", clear_on_submit=True):
        a,b,c=st.columns(3)
        when=a.date_input("Date",value=date.today(),max_value=date.today())
        metric=b.selectbox("Metric",list(METRIC_UNITS))
        value=c.number_input(f"Value (see unit below)",min_value=0.0,max_value=100000.0,step=0.1)
        st.caption(f"Selected unit: **{METRIC_UNITS[metric]}**")
        if st.form_submit_button("Add dated measurement"):
            _records().append({"date":when.isoformat(),"metric":metric,"value":value,"unit":METRIC_UNITS[metric]})
            st.success("Measurement added to this session")
    records=_records()
    if records:
        selected=st.selectbox("View trend for",list(METRIC_UNITS),key="trend_metric")
        points=sorted((r for r in records if r["metric"]==selected),key=lambda r:r["date"])
        if points:
            chart = pd.DataFrame({"Date": [p["date"] for p in points], "Value": [p["value"] for p in points]})
            st.line_chart(chart, x="Date", y="Value", x_label="Date", y_label=METRIC_UNITS[selected])
            if len(points)>1:
                st.metric("Change from first to latest entry",f"{points[-1]['value']-points[0]['value']:+g} {METRIC_UNITS[selected]}")
                st.caption("A change can reflect measurement conditions or normal variation. It is not proof that health improved or worsened.")
        st.dataframe(sorted(records,key=lambda r:r["date"],reverse=True),hide_index=True,use_container_width=True)
        st.download_button("Download all measurements as CSV",_csv_bytes(records),file_name="health_compass_my_metrics.csv",mime="text/csv")
        if st.button("Clear current session measurements"):
            st.session_state["health_records"]=[]
            st.rerun()
    else:
        st.info("Add a measurement to see its dated trend and export it.")


def habits():
    st.header("✅ Weekly habit dashboard")
    st.caption("Choose one modest goal. These checkboxes reset when this browser session ends; download a short visit summary if you want a record.")
    goal=st.selectbox("This week's focus",["Walk or move", "Consistent sleep time", "Vegetables or fruit", "Strength session", "Contact a friend"],key="week_goal")
    days=st.columns(7)
    results=[]
    for i,col in enumerate(days):
        with col:
            results.append(st.checkbox((date.today()-timedelta(days=6-i)).strftime("%a %d"),key=f"habit_{date.today().isoformat()}_{goal}_{i}"))
    count=sum(results)
    st.progress(count/7,text=f"{count}/7 days checked for: {goal}")
    st.write("Reflection: What helped, and what would make next week easier?")
    st.text_area("My observation",key="habit_reflection",height=80)
    st.caption("This is a consistency visual, not a validated health score or prescription to do every habit daily.")


def visit_prep():
    st.header("📝 Appointment prep")
    st.caption("Prepare a concise summary for a clinician. The downloaded text includes only what you enter and the latest session measurements.")
    reason=st.text_area("Main concern or goal",key="visit_reason")
    symptoms=st.text_area("Symptoms, start date, frequency and what makes them better or worse",key="visit_symptoms")
    medicines=st.text_area("Medicines and supplements, including doses (optional)",key="visit_medicines")
    questions=st.text_area("My top three questions",key="visit_questions")
    lines=["Health Compass - visit preparation",f"Prepared: {date.today().isoformat()}","",f"Main concern: {reason}",f"Symptoms / timeline: {symptoms}",f"Medicines and supplements: {medicines}",f"Questions: {questions}","","Measurements entered this session:"]
    lines += [f"{r['date']}: {r['metric']} {r['value']:g} {r['unit']}" for r in sorted(_records(),key=lambda r:r["date"],reverse=True)[:20]]
    st.download_button("Download visit summary (.txt)","\n".join(lines),file_name="health_compass_visit_summary.txt",mime="text/plain")
    st.caption("Review the downloaded summary for accuracy before sharing. This tool does not interpret symptoms or recommend a treatment.")


def daily_fact():
    st.header("💡 Today's evidence-linked fact")
    facts=[(topic,fact,url) for topic,guide in GUIDES.items() for fact,url in guide["facts"]]
    topic,fact,url=facts[date.today().toordinal()%len(facts)]
    st.info(f"**{topic}:** {fact}")
    st.markdown(f"[Read the original source ↗]({url})")
    st.caption("One curated fact rotates each day; it is not a live news feed. Review the linked source for updates.")
