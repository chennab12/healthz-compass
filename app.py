"""Evidence-linked, general education dashboard. No network calls or persistence."""
import csv
import io
from datetime import date

import streamlit as st
from knowledge import GUIDES

st.set_page_config(page_title="Health Compass", page_icon="🧭", layout="wide")

SOURCES = {
    "CDC diabetes tests": "https://www.cdc.gov/diabetes/diabetes-testing/index.html",
    "AHA blood pressure": "https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings",
    "CDC activity": "https://www.cdc.gov/physical-activity-basics/guidelines/adults.html",
    "CDC sleep": "https://www.cdc.gov/sleep/about/index.html",
    "AHA Life's Essential 8": "https://www.heart.org/en/healthy-living/healthy-lifestyle/lifes-essential-8",
    "CDC healthy eating": "https://www.cdc.gov/nutrition/php/resources/healthy-eating-benefits-for-adults.html",
    "USPSTF recommendations": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation-topics/uspstf-a-and-b-recommendations",
    "CDC adult immunizations": "https://www.cdc.gov/vaccines/hcp/imz-schedules/adult-age.html",
    "NIMH caring for mental health": "https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health",
    "MedlinePlus health topics": "https://medlineplus.gov/healthtopics.html",
    "NHLBI sleep apnea": "https://www.nhlbi.nih.gov/health/sleep-apnea",
    "CDC cholesterol": "https://www.cdc.gov/cholesterol/about/index.html",
    "NCI screening": "https://www.cancer.gov/about-cancer/screening",
    "NIH dietary supplements": "https://ods.od.nih.gov/HealthInformation/DS_WhatYouNeedToKnow.aspx",
    "CDC diabetes prevention": "https://www.cdc.gov/diabetes/prevention/index.html",
}

TOPICS = [
    {"name":"Heart & blood pressure", "icon":"❤️", "kpi":"Blood pressure and cholesterol", "why":"Elevated blood pressure and LDL cholesterol can raise cardiovascular risk over time.", "learn":"A blood pressure reading has an upper (systolic) and lower (diastolic) value. Context and repeated measurements matter.", "action":"Record several properly taken home readings; discuss sustained elevation and overall heart risk with a clinician.", "watch":"Chest pain, new severe breathlessness, stroke signs, or BP above 180/120 with symptoms calls for emergency care.", "sources":["AHA blood pressure","AHA Life's Essential 8","CDC cholesterol"]},
    {"name":"Blood sugar & metabolism", "icon":"🩸", "kpi":"A1c and fasting glucose", "why":"Higher blood sugar can precede type 2 diabetes and is an opportunity for prevention or treatment.", "learn":"A1c describes roughly 2–3 months of glucose. A1c 5.7–6.4% is in the prediabetes range; ≥6.5% is in the diabetes range. Fasting glucose 100–125 mg/dL is in the prediabetes range; ≥126 mg/dL is in the diabetes range.", "action":"Confirm an abnormal result with your clinician; discuss activity, food patterns and an evidence-based prevention program when appropriate.", "watch":"A single home or laboratory value does not settle a diagnosis; test conditions and repeat testing matter.", "sources":["CDC diabetes tests","CDC diabetes prevention"]},
    {"name":"Food & nutrition", "icon":"🥗", "kpi":"Eating pattern, fiber and nutrient adequacy", "why":"Overall food patterns influence heart and metabolic health.", "learn":"Build meals around vegetables, fruit, whole grains, beans and suitable protein; pay attention to sodium, saturated fat and added sugar.", "action":"Start with one sustainable swap and review any suspected nutrient deficiency with a clinician before high-dose supplements.", "watch":"Pregnancy, kidney disease, food allergies and medications can change appropriate advice.", "sources":["CDC healthy eating","NIH dietary supplements"]},
    {"name":"Movement & strength", "icon":"🚶", "kpi":"150 minutes/week + 2 strength days", "why":"Movement supports heart health, function, sleep and blood sugar.", "learn":"For most adults, aim for at least 150 minutes of moderate activity each week plus strength work on 2 days; smaller amounts also count.", "action":"Track a weekly total and build gradually with walking and basic strength sessions.", "watch":"Adjust activity to symptoms, disability and existing conditions with a clinician.", "sources":["CDC activity"]},
    {"name":"Sleep & recovery", "icon":"🌙", "kpi":"Sleep duration and quality", "why":"Regular sleep supports daytime functioning and overall health.", "learn":"Most adults need at least 7 hours per night; duration alone does not capture sleep quality.", "action":"Keep a consistent schedule and note persistent snoring, breathing pauses or daytime sleepiness.", "watch":"Possible sleep apnea deserves medical assessment rather than self-treatment.", "sources":["CDC sleep","NHLBI sleep apnea"]},
    {"name":"Mental wellbeing", "icon":"🧠", "kpi":"Mood, stress and daily functioning", "why":"Persistent symptoms deserve the same attention as physical symptoms.", "learn":"Changes in sleep, energy, mood and enjoyment can be useful signals; screening tools are conversation starters.", "action":"Track patterns and seek professional support if symptoms persist or disrupt daily life.", "watch":"For immediate danger call emergency services; in the US call or text 988 for suicide or emotional crisis.", "sources":["NIMH caring for mental health","USPSTF recommendations"]},
    {"name":"Prevention & screening", "icon":"🩺", "kpi":"Due dates for age- and risk-based care", "why":"Vaccination and screening can identify risks before symptoms arise.", "learn":"Screening choices depend on age, anatomy, family history and prior results; recommendations change.", "action":"Review blood pressure, diabetes risk, cancer screening and immunizations at a preventive visit.", "watch":"A screening schedule cannot be safely inferred from age alone.", "sources":["USPSTF recommendations","CDC adult immunizations","NCI screening"]},
    {"name":"Medicines & supplements", "icon":"💊", "kpi":"Current list and interactions", "why":"A complete list helps avoid interactions, duplication and missed treatment.", "learn":"Supplements can have side effects and interact with medicines; 'natural' does not establish safety.", "action":"Keep a current list with doses; bring it to a clinician or pharmacist before changing treatments.", "watch":"Do not stop a prescribed medicine based on a dashboard summary.", "sources":["NIH dietary supplements","MedlinePlus health topics"]},
]

st.title("🧭 Health Compass")
st.caption("Plain-language, evidence-linked health awareness • Curated review: September 25, 2026 • US adult context")
st.info("Use this to prepare questions and healthy routines. It cannot diagnose, replace a clinician, or predict your personal outcome. For urgent symptoms, seek immediate care.")

tabs = st.tabs(["🏠 Overview"] + [t["icon"] + " " + t["name"] for t in TOPICS] + ["📈 Trends & scenarios", "📚 Sources & method"])

with tabs[0]:
    st.subheader("Start with the measures that change decisions")
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Movement", "150 min/wk", help="Moderate aerobic activity for most adults; add two strength days")
    c2.metric("Sleep", "7+ hours", help="General adult recommendation, with individual variation")
    c3.metric("Blood pressure", "Track trend", help="Use repeated readings and clinical confirmation")
    c4.metric("Blood sugar", "Know A1c", help="Follow up abnormal values")
    st.markdown("### The 8 practical areas")
    st.dataframe([{"Area":t["name"],"Key measure":t["kpi"],"First step":t["action"]} for t in TOPICS],hide_index=True,use_container_width=True)
    st.caption("These are editorial priorities for general adult self-care, not a calculated 'top 10%' ranking or a personalized medical score.")

for tab, t in zip(tabs[1:1+len(TOPICS)], TOPICS):
    with tab:
        st.header(t["icon"]+" "+t["name"])
        st.metric("Useful KPI",t["kpi"])
        for heading,key in [("Why it matters","why"),("Understand","learn"),("Try next","action"),("When to get help","watch")]:
            st.markdown(f"**{heading}:** {t[key]}")
        st.markdown("**Read the original guidance:** " + " · ".join(f"[{s}]({SOURCES[s]})" for s in t["sources"]))
        guide = GUIDES[t["name"]]
        st.subheader("Crucial evidence-backed facts")
        for fact, url in guide["facts"]:
            st.markdown(f"- {fact} [Source ↗]({url})")
        st.subheader("Metrics to understand")
        st.dataframe([{"Metric":name,"Unit / format":unit,"How to use it":meaning} for name,unit,meaning in guide["metrics"]],hide_index=True,use_container_width=True)
        st.subheader("Common questions")
        for question, answer in guide["faq"]:
            with st.expander(question): st.write(answer)
        st.caption("General guidance; thresholds and actions may differ for children, pregnancy, medication use and known illness.")

with tabs[-2]:
    st.header("Trends & scenarios")
    st.write("Explore how changing a routine compares with a general guideline. These are arithmetic scenarios, not forecasts of disease, longevity or treatment effects.")
    weekly=st.slider("Moderate activity minutes per week",0,350,90,10)
    strength=st.slider("Strength sessions per week",0,7,1)
    sleep=st.slider("Typical sleep hours per night",0.0,12.0,6.5,0.5)
    a,b,c=st.columns(3)
    a.metric("Activity guideline progress",f"{min(weekly/150*100,100):.0f}%",f"{max(150-weekly,0)} min to 150")
    b.metric("Strength guideline progress",f"{min(strength/2*100,100):.0f}%",f"{max(2-strength,0)} sessions to 2")
    c.metric("Sleep vs 7-hour reference",f"{sleep:g} h",f"{sleep-7:+g} h")
    st.markdown("**Interpretation:** A higher activity total or more consistent sleep is a trackable habit; it cannot be converted into an individual disease-risk percentage from these inputs. [CDC activity](%s) · [CDC sleep](%s)" % (SOURCES["CDC activity"],SOURCES["CDC sleep"]))
    st.caption("Inputs stay in the current browser session. The app stores no health record or account information.")

with tabs[-1]:
    st.header("Sources & editorial method")
    st.write("Sources are public health agencies, national medical organizations and academic medical information services. Website popularity and review counts are not measures of medical reliability. Selection favors actionable, widely relevant adult topics with primary guidance.")
    st.write("Guidance is curated rather than live scraped. Check the original page for updates. No article popularity score, automated news feed or personalized risk projection is claimed.")
    st.write("'Crucial' means editorially selected for relevance and actionability. There is no measured top-1% ranking. WebMD and Wikipedia can help with background reading, but numerical medical guidance here is tied to public health agencies and clinical organizations.")
    st.dataframe([{"Source":name,"URL":url} for name,url in SOURCES.items()],hide_index=True,use_container_width=True, column_config={"URL":st.column_config.LinkColumn("URL")})
    out=io.StringIO(); writer=csv.writer(out); writer.writerow(["area","kpi","why","takeaway","action","caution","source_urls","reviewed_on"])
    for t in TOPICS: writer.writerow([t["name"],t["kpi"],t["why"],t["learn"],t["action"],t["watch"],"; ".join(SOURCES[s] for s in t["sources"]),"2026-09-25"])
    st.download_button("Download curated insights CSV",out.getvalue(),file_name="health_compass_insights.csv",mime="text/csv")
