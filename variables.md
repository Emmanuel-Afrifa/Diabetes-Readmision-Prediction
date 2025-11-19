### Variable Table
---
| Variable Name | Description | Data Type | Has Missing Values |
| -- | -- | -- | -- |
| encounter_id | Unique identifier of an encounter | Integer | No |
| patient_nbr | Unique identifier of a patient | Integer | No |
| race | Values: Caucasian, Asian, African American, Hispanic, and other | Categorical | Yes |
| gender | Values: male, female, and unknown/invalid | Categorical | No |
| age | Grouped in 10-year intervals: [0, 10), [10, 20),..., [90, 100) | Categorical | No |
| weight | Weight in pounds. | Categorical | Yes |
| admission_type_id | Integer identifier corresponding to 9 distinct values, for example, emergency, urgent, elective, newborn, and not available | Categorical | No |
| discharge_disposition_id | Integer identifier corresponding to 29 distinct values, for example, discharged to home, expired, and not available | Categorical | No |
| admission_source_id | Integer identifier corresponding to 21 distinct values, for example, physician referral, emergency room, and transfer from a hospital |  Categorical | No |
| time_in_hospital | Integer number of days between admission and discharge | Integer | No |
| payer_code | Integer identifier corresponding to 23 distinct values, for example, Blue Cross/Blue Shield, Medicare, and self-pay | Categorical | Yes |
| medical_specialty | Integer identifier of a specialty of the admitting physician, corresponding to 84 distinct values, for example, cardiology, internal medicine, family/general practice, and surgeon | Categorical | Yes | 
| num_lab_procedures | Number of lab tests performed during the encounter | Integer | No |
| num_procedures | Number of procedures (other than lab tests) performed during the encounter | Integer | No |
| num_medications | Number of distinct generic names administered during the encounter | Integer | No |
| number_outpatient | Number of outpatient visits of the patient in the year preceding the encounter | Integer | No |
| number_emergency | Number of emergency visits of the patient in the year preceding the encounter | Integer | No |
| number_inpatient | Number of inpatient visits of the patient in the year preceding the encounter | Integer | No
| diag_1 | The primary diagnosis (coded as first three digits of ICD9); 848 distinct values | Categorical | Yes |
| diag_2 | Secondary diagnosis (coded as first three digits of ICD9); 923 distinct values | Categorical | Yes |
| diag_3 | Additional secondary diagnosis (coded as first three digits of ICD9); 954 distinct values | Categorical | Yes |
| number_diagnoses | Number of diagnoses entered to the system | Integer | No |
| max_glu_serum | Indicates the range of the result or if the test was not taken. Values: >200, >300, normal, and none if not measured | Categorical | No |
| A1Cresult | Indicates the range of the result or if the test was not taken. Values: >8 if the result was greater than 8%, >7 if the result was greater than 7% but less than 8%, normal if the result was less than 7%, and none if not measured. | Categorical | No |
| metformin | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| repaglinide | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| nateglinide | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| chlorpropamide | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| glimepiride | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| acetohexamide | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| glipizide | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| glyburide | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| tolbutamide | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| pioglitazone | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| rosiglitazone | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| acarbose | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| miglitol | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| troglitazone | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| tolazamide | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| examide | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| citoglipton | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| insulin | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| glyburide-metformin | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| glipizide-metformin | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| glimepiride-pioglitazone | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| metformin-rosiglitazone | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| metformin-pioglitazone | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed | Categorical | No |
| change | Indicates if there was a change in diabetic medications (either dosage or generic name). Values: change and no change | Categorical | No |
| diabetesMed | Indicates if there was any diabetic medication prescribed. Values: yes and no | Categorical | No |
| readmitted | Days to inpatient readmission. Values: <30 if the patient was readmitted in less than 30 days, >30 if the patient was readmitted in more than 30 days, and No for no record of readmission. | Categorical | No |