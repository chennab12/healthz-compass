"""Curated educational facts. Each row includes a direct primary-source URL."""

GUIDES = {
"Heart & blood pressure": {
"facts": [
("Normal blood pressure is below 120/80 mm Hg; stage 1 hypertension starts at 130 systolic or 80 diastolic.", "https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings"),
("A home reading is most useful after five minutes of quiet rest, with a correctly sized cuff and two readings one minute apart.", "https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings/monitoring-your-blood-pressure-at-home"),
("Cardiovascular health includes diet, activity, nicotine exposure, sleep, weight, cholesterol, glucose and blood pressure.", "https://www.heart.org/en/healthy-living/healthy-lifestyle/lifes-essential-8")],
"metrics": [("BP", "mm Hg, top/bottom", "Use a repeated home trend; confirm the plan with your clinician."),("LDL / non-HDL", "mg/dL from lipid panel", "Treatment targets depend on overall risk, not one universal cutoff.")],
"faq": [("Does one high reading mean I have hypertension?", "Usually no. Recheck with proper technique and discuss the pattern and diagnostic confirmation."),("Can I stop my BP medicine if home numbers look normal?", "No. Review changes with the prescriber first.")]},
"Blood sugar & metabolism": {
"facts": [("A1c 5.7–6.4% is in the prediabetes range; 6.5% or above is in the diabetes range.", "https://www.cdc.gov/diabetes/diabetes-testing/index.html"),("Fasting plasma glucose of 100–125 mg/dL is in the prediabetes range; 126 mg/dL or above is in the diabetes range.", "https://www.cdc.gov/diabetes/diabetes-testing/index.html"),("Lifestyle interventions can reduce progression to type 2 diabetes for people with prediabetes.", "https://www.cdc.gov/diabetes/prevention/index.html")],
"metrics": [("A1c", "%", "Reflects average glucose over approximately 2–3 months."),("Fasting glucose", "mg/dL", "A lab sample requires the specified fasting conditions.")],
"faq": [("What if A1c and fasting glucose disagree?", "They measure different aspects; ask a clinician about repeat or alternative testing."),("Is 6.4% the same as a diabetes diagnosis?", "It is in the prediabetes A1c range, but a fasting result may tell a different story; obtain clinical follow-up.")]},
"Food & nutrition": {
"facts": [("A heart-healthy pattern emphasizes vegetables, fruit, whole grains, legumes, healthy protein and unsaturated oils.", "https://www.heart.org/en/healthy-living/healthy-lifestyle/lifes-essential-8"),("Supplements cannot replace a varied diet and may interact with medications.", "https://ods.od.nih.gov/HealthInformation/ODS_Frequently_Asked_Questions/")],
"metrics": [("Food pattern", "Weekly variety", "Note vegetables, fruit, legumes and whole grains rather than scoring one meal."),("Nutrient labs", "Lab-specific units", "Investigate a suspected deficiency and its cause with your clinician.")],
"faq": [("Should I eliminate all carbohydrates?", "No universal rule applies; focus on quality and portions and tailor to your medical situation."),("Should I start several vitamins at once?", "Review the need, dose and interactions first, especially with known deficiencies or medicines.")]},
"Movement & strength": {
"facts": [("Adults generally benefit from at least 150 minutes of moderate activity per week and two muscle-strengthening days.", "https://www.cdc.gov/physical-activity-basics/guidelines/adults.html"),("Some activity is better than none; minutes can be spread across the week.", "https://www.cdc.gov/physical-activity-basics/adding-adults/index.html")],
"metrics": [("Moderate activity", "minutes/week", "Work gradually toward 150; vigorous activity has a different equivalence."),("Strength", "days/week", "Aim for two days covering major muscle groups.")],
"faq": [("Must I exercise 30 minutes without stopping?", "No; activity can be accumulated over the week."),("What if I am currently sedentary?", "Start at a manageable level and increase gradually; seek tailored advice if you have symptoms or limitations.")]},
"Sleep & recovery": {
"facts": [("Adults ages 18–60 are generally recommended to sleep seven or more hours per night.", "https://www.cdc.gov/sleep/about/index.html"),("Loud snoring and daytime sleepiness are possible symptoms of sleep apnea.", "https://www.nhlbi.nih.gov/health/sleep-apnea/symptoms")],
"metrics": [("Sleep duration", "hours/night", "Track usual patterns, not one night."),("Daytime function", "Symptoms/week", "Note sleepiness, breathing pauses and morning symptoms.")],
"faq": [("Does eight hours rule out sleep apnea?", "No. Sleep duration and breathing quality are separate issues."),("Will sleep music treat insomnia or apnea?", "It may help some people relax, but persistent insomnia or suspected apnea merits evaluation.")]},
"Mental wellbeing": {
"facts": [("Persistent changes in mood, energy, sleep and functioning can signal a need for professional support.", "https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health"),("The USPSTF recommends depression screening in adults.", "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation-topics/uspstf-a-and-b-recommendations")],
"metrics": [("Mood/function", "Days affected", "Track what has changed and whether daily life is disrupted."),("Support", "Follow-up date", "Arrange care if symptoms persist or worsen.")],
"faq": [("Can a questionnaire diagnose depression?", "No; screening identifies people who may need assessment."),("When is this urgent?", "Immediate danger or suicidal thoughts require urgent help; in the US, call or text 988 or emergency services.")]},
"Prevention & screening": {
"facts": [("For average-risk adults, USPSTF recommends colorectal cancer screening from ages 45 through 75.", "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/colorectal-cancer-screening"),("Blood pressure screening is recommended for adults, with out-of-office confirmation before treatment.", "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/hypertension-in-adults-screening"),("Adult vaccine recommendations vary by age, health condition and vaccine history.", "https://www.cdc.gov/vaccines/hcp/imz-schedules/adult-age.html")],
"metrics": [("Screening", "Last date / next due", "Record test type, result and recommended interval."),("Vaccines", "History / next review", "Check the current CDC schedule with your clinician.")],
"faq": [("Is a stool test the same as a colonoscopy?", "Both are screening options for some people, but intervals and follow-up requirements differ."),("Does family history change my schedule?", "It can; discuss it before applying average-risk ages.")]},
"Medicines & supplements": {
"facts": [("The FDA does not determine dietary supplement effectiveness before marketing in the way it evaluates medications.", "https://ods.od.nih.gov/factsheets/WYNTK-Consumer/"),("Some supplements can alter the effects of prescription drugs.", "https://ods.od.nih.gov/HealthInformation/ODS_Frequently_Asked_Questions/")],
"metrics": [("Medicine list", "Name / dose / frequency", "Include nonprescription drugs and supplements."),("Safety review", "Date and clinician", "Recheck with changes in diagnoses, doses or products.")],
"faq": [("Does natural mean harmless?", "No; dose, interactions and individual conditions matter."),("Can a supplement replace a prescribed medicine?", "Do not substitute without discussing it with the prescriber.")]},
}
