"""Small self-contained trackers; inputs are session-only and never diagnose."""
import streamlit as st

METRICS = {
 "Heart & blood pressure": [("Systolic BP", "mm Hg", 120.0, "below", "https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings"), ("Diastolic BP", "mm Hg", 80.0, "below", "https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings")],
 "Blood sugar & metabolism": [("A1c", "%", 5.7, "below", "https://www.cdc.gov/diabetes/diabetes-testing/index.html"), ("Fasting glucose", "mg/dL", 100.0, "below", "https://www.cdc.gov/diabetes/diabetes-testing/index.html")],
 "Food & nutrition": [("Days with fruit and vegetables", "days/week", 7.0, "at_least", "https://www.heart.org/en/healthy-living/healthy-lifestyle/lifes-essential-8"), ("Days with whole grains or legumes", "days/week", 7.0, "illustrative", "https://www.heart.org/en/healthy-living/healthy-lifestyle/lifes-essential-8")],
 "Movement & strength": [("Moderate movement", "minutes/week", 150.0, "at_least", "https://www.cdc.gov/physical-activity-basics/guidelines/adults.html"), ("Strength sessions", "days/week", 2.0, "at_least", "https://www.cdc.gov/physical-activity-basics/guidelines/adults.html")],
 "Sleep & recovery": [("Typical sleep", "hours/night", 7.0, "at_least", "https://www.cdc.gov/sleep/about/index.html"), ("Nights of loud snoring", "nights/week", None, "observe", "https://www.nhlbi.nih.gov/health/sleep-apnea/symptoms")],
 "Mental wellbeing": [("Days mood affects functioning", "days/week", None, "observe", "https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health"), ("Days connected with someone", "days/week", None, "observe", "https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health")],
 "Prevention & screening": [("Years since preventive care review", "years", None, "observe", "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation-topics/uspstf-a-and-b-recommendations"), ("Outstanding questions for visit", "questions", None, "observe", "https://medlineplus.gov/healthtopics.html")],
 "Medicines & supplements": [("Products on current list", "items", None, "observe", "https://ods.od.nih.gov/factsheets/WYNTK-Consumer/"), ("Unreviewed products", "items", None, "observe", "https://ods.od.nih.gov/HealthInformation/ODS_Frequently_Asked_Questions/")],
}

def render_topic_dashboard(topic):
    """A lightweight visual uses native Streamlit and has no extra dependencies."""
    st.subheader("Your quick dashboard")
    st.caption("Optional entries remain in this browser session. Reference values are broad adult education, not personal treatment targets.")
    cols = st.columns(2)
    for i, (label,unit,ref,kind,url) in enumerate(METRICS[topic]):
        with cols[i]:
            enabled = st.checkbox(f"I know my {label.lower()}", key=f"enabled_{topic}_{i}")
            if enabled:
                value = st.number_input(f"{label} ({unit})", min_value=0.0, max_value=1000.0, value=0.0, step=0.1 if unit in ("%","hours/night") else 1.0, key=f"metric_{topic}_{i}")
                st.metric(label, f"{value:g} {unit}")
                if ref is not None:
                    if kind == "at_least":
                        st.progress(min(value/ref, 1.0), text=f"{min(value/ref*100,100):.0f}% of general {ref:g} {unit} reference")
                    elif kind == "below":
                        st.caption(f"General category boundary: {ref:g} {unit}. This reading alone is not a diagnosis.")
                    else:
                        st.caption("Illustrative habit tracker; no validated clinical threshold.")
                else:
                    st.caption("Use as a pattern to discuss, not as a medical score.")
            else:
                st.metric(label, "Not entered")
            st.markdown(f"[Metric context ↗]({url})")
    st.markdown("**One action for this week**")
    st.text_input("Write a small, concrete next step", key=f"action_{topic}", placeholder="Example: book a preventive visit")
    st.checkbox("I completed this step", key=f"done_{topic}")
