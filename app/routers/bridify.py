"""
Copyright (c) 2025 IntakeDesk LLC. All rights reserved.
Proprietary and Confidential. Unauthorized copying, use, modification,
or distribution is prohibited.
"""

from secrets import randbelow

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/retainer", response_class=JSONResponse)
async def retainer() -> JSONResponse:
    payload = {
        "code": 0,
        "message": "Succeeded",
        "data": {
            "id": f"{randbelow(9999999) + 1:04d}",
            "organizationId": 247,
            "vendorOrganizationId": 376,
            "matterId": "d01b54f71a0d499e806092ca56f3093e",
        },
    }
    return JSONResponse(content=payload)


@router.post("/document", response_class=JSONResponse)
async def document() -> JSONResponse:
    payload = {
        "code": 0,
        "message": "Succeeded",
        "data": {
            "id": f"{randbelow(9999999) + 1:04d}",
            "organizationId": 247,
            "vendorOrganizationId": 376,
            "matterId": "d01b54f71a0d499e806092ca56f3093e",
        },
    }
    return JSONResponse(content=payload)


@router.post("/case", response_class=JSONResponse)
async def case() -> JSONResponse:
    payload = {
        "code": 0,
        "message": "Succeeded",
        "data": {
            "id": 677959,
            "organizationId": 247,
            "vendorOrganizationId": 376,
            "matterId": "d01b54f71a0d499e806092ca56f3093e",
            "matterName": "Roundup - Crane",
            "contactId": 10215685,
            "prospectId": "1d23dec0d948477bba728400033e9c5e",
            "source": "Intake Desk",
            "matterType": "roundup",
            "firstName": "Susan",
            "middleName": None,
            "lastName": "Crane",
            "primarySsn": None,
            "ssnLast4": None,
            "gender": "Female",
            "dob": None,
            "email": "poodlekitty@gmail.com",
            "phone": "(206) 999-4540",
            "state": "Washington",
            "city": "Shoreline",
            "county": "",
            "zipCode": "98133-6007",
            "address": "15739 Densmore Avenue North ",
            "externalId": "163083",
            "externalId2": None,
            "externalId3": None,
            "orderId": "6886677",
            "matterIntake": {
                "vendor_case_number": "163083",
                "vendor_campaign": "Kline & Specter/Bay Point - Roundup 95 - One",
                "orderId": "6886677",
                "whenFirstDiscoverLymphomaRelatedRoundup": "2024-04-16",
                "behalfCity": "Shoreline",
                "diagnosedWithNonHodgkinLymphoma": "",
                "emergencyContactPhone": "",
                "directOrIndirect": "directlyieYouSprayed",
                "useOtherProducts": "",
                "anyLivingEyeWitness": "No",
                "usedRoundupCommerciallyResidentially": "Washington",
                "beToldInjuryRelatedToProduct": "no",
                "caseSummary": """SENT USPS PACKAGE TO CLIENT WITH HIPAA AUTHORIZATIONS TO
                EXECUTE WITH AN ORIGINAL SIGNATURE AND RETURN IN PRE-PAID POSTAGE ENVELOPE.
                \nTRACKING #: 9405511206224863697130\nRETURN TRACKING #: 9405511206224863697352
                \n(SEE ATTACHED LABEL)\n\nSusan was exposed to Roundup between the years 1992 -
                2008 at her residence.\n\nSusan was exposed to Roundup for approximately
                45 minutes per day, 4 days per month, 3 months out of the year, for 16 years,
                totaling 144 hours of exposure.\n\nSusan used the 1.3-gallon Roundup
                ready-to-spray to eliminate weeds throughout the 1/4-acre landscape,
                2-car asphalt driveway, 14 ft. x 10 ft. patio, and the 20 ft. fence line.\n\n
                Susan's father purchased Roundup to use at the residence.\n\nAt the age of 69,
                in September 2023, Susan was diagnosed with Nodal Marginal Zone B-cell Lymphoma
                at Proliance Surgical Specialists of Edmonds Care Center located in Edmonds,
                Washington.\n\nIn 2023, Susan had a tumor removal performed at Proliance Surgical
                Specialists of Edmonds Care Center located in Edmonds, Washington.""",
                "lastWill": "unknow",
                "redFlag": [None],
                "channel": "intakedesk",
                "middleName": "",
                "treatmentInformation": [
                    {
                        "surgeryType": "",
                        "phoneNumber": "",
                        "treatingPhysicianSurgeonName": "Carol, Cornejo, MD",
                        "hospitalAddress": "7320 216th Street Southwest Suite B-20",
                        "hospitalName": "Proliance Surgical Specialists of Edmonds Care Center",
                        "startDateofTreatment": "2023-10-01",
                        "hospitalCity": "Edmonds",
                        "hospitalZIP": "98026",
                        "endDateofTreatment": "2023-10-01",
                        "hospitalState": "WA",
                        "typeOfTreatmentReceived": [{"value": "surgery"}],
                    }
                ],
                "dateOfDiagnosisLymphoma": "09/2023",
                "isClientResident": "yes",
                "previouslySettled": "no",
                "whoisEmployer": "",
                "behalfZipCode": "98133",
                "spousePhoneNumber": "",
                "previousCancerDiagnosesModel": [{"canerType": "", "dateOfDiagnosis": ""}],
                "provideDeathCertificate": "",
                "tobaccoModel": {
                    "whenStartedUsingTobaccoProducts": "1978-01-01",
                    "whenQuitSmoke": "1985-01-01",
                },
                "last4SSN": "2325",
                "typeOfLymphomaDiagnosed": "marginalZonaLymphoma",
                "aliases": "",
                "relationOfLivingEyeWitnesstoDeceased": "Self",
                "endDateofUsingRoundup": "2008",
                "explainOfNotInRemission": "",
                "dutiesAtThatJob": "",
                "spouseFirstName": "",
                "receivedTreatment": "yes",
                "behalfReason": "",
                "city": "Shoreline",
                "exposed10Times": "yes",
                "county": "",
                "exposed10Hours": "no",
                "nameOfOffbrandRoundupUsed": "",
                "behalfFirstName": "Susan",
                "behalfLastName": "Crane",
                "cellPhone": "2069994540",
                "behalfPhoneHome": "",
                "behalfEmail": "",
                "behalfAddress": "15739 Densmore Avenue North",
                "behalfState": "WA",
                "behalfSsn": "2325",
                "behalfBirthDate": "10-26-1953",
                "behalfGender": "Female",
                "behalfRelation": "Self",
                "havePoA": "",
                "bestContactTime": "Anytime - Pacific Standard Time (PST) - Any Day",
                "behalfContactNotes": """Susan does not feel comfortable providing the full
                SSN at this time and will provide it to the paralegal/attorney.""",
                "emergencyContactFirstName": "",
                "emergencyContactLastName": "",
                "emergencyContactPhoneNumber": "",
                "emergencyContactRelationship": "",
                "emergencyContactFirstNameTwo": "",
                "emergencyContactLastNameTwo": "",
                "emergencyContactPhoneNumberTwo": "",
                "emergencyContactRelationshipTwo": "",
                "firstName": "Susan",
                "lastName": "Crane",
                "phone": "(206) 999-4540",
                "phone2": "",
                "email": "poodlekitty@gmail.com",
                "addres": "",
                "state": "Washington",
                "zipCode": "98133-6007",
                "address": "15739 Densmore Avenue North ",
                "injuredSsn": "2325",
                "dob": "1953-10-26",
                "gender": "Female",
                "martialStatus": "Married",
                "injuredNotes": "Previous Occupation: Assignment Technician",
                "aliveOrDeceased": "No",
                "deathDate": "",
                "causeOfDeath": "",
                "deathOccurState": "",
                "deathExecutorOfWill": "No",
                "deathEstateRepresentative": "No",
                "deathNamedInformant": "No",
                "moreInfoAboutCase": [False],
                "residentialRoundupUsageArea": """Landscape: 1/4 Acre\nDriveway: 2 cars,
                Asphalt\nPatio: 14 ft x 10 ft\nFenceline: 20 ft""",
                "residentialRoundupYearFirstUsed": "1992",
                "residentialRoundupDiscontinued": "Yes",
                "residentialRoundupYearLastUsed": "2008",
                "residentialRoundupTotalLifetimeYearsUsed": "16 years ",
                "residentialRoundupTotalHoursFrequency": """144 hours ( 45 mins/day, 4 days/mo,
                3 months/yr, 16 years )""",
                "residentialRoundupTotalLifetimeExposure": "192 times used ",
                "personalProtectiveEquipment": "No",
                "containerSize": "1.3-gallon Ready To Spray",
                "sprayerSpreaderTyper": "Sprayer that came with Roundup Bottle",
                "residentialExposureNote": """Susan used the 1.3-gallon Roundup ready-to-spray to
                eliminate weeds throughout the 1/4-acre landscape, 2-car asphalt driveway,
                14 ft. x 10 ft. patio, and the 20 ft. fence line.""",
                "workUsageArea": "",
                "workYearFirstUsed": "",
                "workDiscontinued": "",
                "workYearLastUsed": "",
                "workTotalLifetimeYearsUsed": "",
                "workTotalLifetimeHoursFrequency": "",
                "workTotalLifetimeExposures": "",
                "workPersonalProtectiveEquipment": "",
                "workExposureNotes": "",
                "injuredPartyPriorDiagnosisOther": "None",
                "diagnosedWithCancerPriortoLymphomaDiagnosis": "No",
                "agentOrangeExposure": "No",
                "organTransplant": "No",
                "receivedBenefits": "No",
                "priorToxicMinePlantOil": "No",
                "priorEBV": "No",
                "priorBI": "No",
                "priorBreastImplants": "No",
                "priorDiabetes": "No",
                "priorExposurePesticides": "No",
                "usedTobaccoProducts": "Yes",
                "tobaccoTotalYearsUsed": "7 year(s) 0 month(s)",
                "tobaccoYearsStoppedPriorToDiagnosis": "38 year(s) 8 month(s)",
                "familyHistoryCancer": "Yes",
                "familyHistoryDetails": [
                    {"value": "Relationship: Father "},
                    {"value": " Diagnosis: Colon Cancer\nRelationship: Sister "},
                    {"value": " Diagnosis: Breast Cancer\nRelationship: Mother "},
                    {"value": " Diagnosis: Ovarian"},
                ],
                "bmiModel": {
                    "currentHeight": "5 ft 5 in ",
                    "currentWeight": "200 pounds",
                    "currentBMI": "33.3",
                },
                "priorBmiModel": {
                    "priorHeight": "5 ft 5 in",
                    "priorWeight": "175 pounds",
                    "priorBMI": "29.1",
                },
                "wherePurchasedRoundup": "Supplied",
                "purchaseReceipts": "No",
                "purchaseStoreCreditCard": "No",
                "purchaseStoreRewardCard": "No",
                "hasRoundupContainer": "No",
                "hasRoundupUsagePhotos": "No",
                "currentOccupation": "Retired",
                "priorEmployment": "",
                "militaryService": "No",
                "disscussWithOtherLawFirm": "No",
                "discoveryDate": "2024-04-16",
                "discoveryInformation": "Internet",
                "provideProofOfUsage": "yes",
                "stateLivingWhenDiagnosis": "Washington",
                "repeatResidentialRoundupExposureLocation": [
                    {
                        "residentialRoundupExposureStartDate": "1992-01-02",
                        "residentialRoundupExposureEndDate": "2008-12-31",
                        "residentialRoundupExposureCity": "Shoreline",
                        "residentialRoundupExposureAddress": "16916 Stone Avenue North",
                        "residentialRoundupExposureState": "WA",
                        "residentialRoundupExposureZipCode": "98133",
                    }
                ],
                "otherTreatingPhysician": [
                    {
                        "hospitalName": "Swedish Cancer Institute Medical Oncology - Edmonds",
                        "hospitalAddress": "21632 Highway 99 \r\n Edmonds, WA 98026",
                        "phoneNumber": "Phone: (425) 673-8300 ",
                        "treatingPhysicianName": "Elizabeth F., Mcgehee, MD",
                        "reasonForConsultation": """Susan was placed under watch and wait
                        observation and has follow-up visits every 3-6 months with
                        this oncologist.""",
                        "startDateofTreatment": "2023-09-28",
                    }
                ],
                "spouseLastName": "",
                "additionalInjurySuffered": "",
                "exposedToRoundup": "yes",
                "useOtherProductsNote": "",
                "statesUsedRoundup": "Washington",
                "endDateofEmployment": "",
                "howKnowLovedOneUsedRoundup": "",
                "diagnosingPhsyicianModel": [
                    {
                        "diagnosingHospitalName": """Proliance Surgical Specialists of Edmonds
                        Care Center""",
                        "diagnosingHospitalAddress": " Edmonds, WA 98026",
                        "diagnosingPhysicianState": "Washington",
                        "diagnosingPhysicianZIP": "98026",
                        "diagnosingPhysicianPhoneNumber": "(425) 778-8116",
                        "diagnosingPhysicianAddress": "7320 216th Street Southwest Suite B-20",
                        "diagnosingPhysicianCity": "Edmonds",
                        "nameOfDiagnosingPhysician": "",
                    }
                ],
                "between18and80": "yes",
                "behalfOf": "",
                "stillCurrentlyUsingRoundup": "no",
                "startDateofUsingRoundup": "1992",
                "anyOtherPhysiciansTreatedLymphoma": "yes",
                "startDateofEmployment": "",
                "nameOfLivingEyeWitness": "",
                "stageOfCancer": "",
                "inRemission": "",
                "useOffBrandRoundup": "",
                "workExposureLocation": [],
                "cancerDiagnosis": [
                    {
                        "cancerDiagnosisDate": "2023-09-01",
                        "diagnosisAge": "69",
                        "cancerYearsInRemission": "",
                        "cancerStage": "Unsure",
                        "cancerChemotherapy": "",
                        "cancerRadiation": "",
                        "stateResidenceDiagnosis": "Washington",
                        "cancerSurgery": "",
                        "cancerType": "Nodal marginal zone B-cell lymphoma (B-NMZL)",
                    }
                ],
                "surgeryFacility": [
                    {
                        "surgeryHospitalAddress": "7320 216th Street Southwest Suite B-20",
                        "surgeryHospitalZipCode": "98026",
                        "surgeryHospitalPhysicianLastName": "Cornejo, MD",
                        "surgeryStartDate": "2023-10-01",
                        "surgeryHospitalPhysicianFirstName": "Carol",
                        "surgeryHospitalCity": "Edmonds",
                        "surgeryHospitalState": "WA",
                        "surgeryEndDate": "2023-10-01",
                        "surgeryHospitalName": """Proliance Surgical Specialists of Edmonds
                        Care Center""",
                        "surgeryHospitalPhoneNumber": "(425) 778-8116",
                    }
                ],
                "repeatChemotherapy": [],
                "repeatRadiation": [],
                "repeatRetailer": [],
                "primaryPhysicianPhoneNumber": "(206) 709-5994",
                "primaryPhysicianAddress": "15214 Aurora Avenue North",
                "primaryPhysicianCity": "Shoreline",
                "primaryPhysicianState": "WA",
                "primaryPhysicianZipCode": "98133",
                "primaryHospital": "One Medical Seniors: Shoreline",
                "primaryPhysicianStart": "",
                "primaryPhysicianFirstName": "Beth",
                "primaryPhysicianLastName": "Fricke, MD",
                "startDateofTreatment": "2021-01-01",
            },
            "matterRelationOrgList": [
                {
                    "id": 867557,
                    "matterId": "d01b54f71a0d499e806092ca56f3093e",
                    "matterOrgId": None,
                    "organizationId": 376,
                    "contactId": 10215685,
                    "organizationName": None,
                    "orgRelationId": 1,
                    "orgRelation": "vendor",
                    "orgRelationName": None,
                    "stageId": None,
                    "stage": None,
                    "stageName": None,
                    "isFinance": None,
                    "isManagerOrganization": None,
                    "customInfo": None,
                    "createdTime": None,
                    "modifiedTime": None,
                    "archive": None,
                }
            ],
        },
    }
    return JSONResponse(content=payload)
