"""
Copyright (c) 2025 IntakeDesk LLC. All rights reserved.
Proprietary and Confidential. Unauthorized copying, use, modification,
or distribution is prohibited.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from integrations.litify.schemas import DocumentResponsePayload
from integrations.oauth.schemas import OauthResponsePayload

router = APIRouter()


@router.post("/case", response_class=JSONResponse)
async def case() -> JSONResponse:
    payload = {
        "data": {
            "Exposures": [
                {
                    "State of Residency During Occurrence": "OK",
                    "State Exposure Occurred": "OK",
                    "Date of Last Exposure": "2020-01-01",
                    "Date of First Exposure": "2016-01-01",
                },
                {
                    "State of Residency During Occurrence": "OK",
                    "State Exposure Occurred": "OK",
                    "Date of Last Exposure": "2016-01-01",
                    "Date of First Exposure": "2015-01-01",
                },
            ],
            "Medical Facilities": [
                {
                    "End Date": None,
                    "Start Date": "2022-07-01",
                    "Facility Address": {
                        "city": "Fort Smith",
                        "country": "United States",
                        "countryCode": "US",
                        "geocodeAccuracy": None,
                        "latitude": None,
                        "longitude": None,
                        "postalCode": "72903",
                        "state": "Arkansas",
                        "stateCode": "AR",
                        "street": None,
                    },
                    "Facility Location": "Mercy Hospital Fort Smith",
                    "Facility Type": "Unknown",
                    "Facility Phone": "(479) 314-6000",
                    "Provider Address": "Mackey, MD",
                    "Provider Name": "Daniel",
                }
            ],
            "Injured Party Date of Death": None,
            "Injured Party Marital Status": None,
            "Injured Party Gender": None,
            "Injured Party Date of Birth": None,
            "Injured Party SSN": None,
            "Injured Party Suffix": None,
            "Does caller have authority to sign?": None,
            "Injured Party Name": "None None",
            "Client Best time to reach": "after 4:00 PM",
            "Client Phone Home": "5555017899",
            "Client Phone Mobile": "5555017899",
            "Client Email": "csilva@intakedesk.com",
            "Client Description": None,
            "Client Marital Status": "Single",
            "Client Gender": "Male",
            "Client Date of Birth": "1984-10-23",
            "Client SSN": "123-45-6789",
            "Client Billing Address": {
                "city": "Talihina",
                "country": "United States",
                "countryCode": "US",
                "geocodeAccuracy": None,
                "latitude": None,
                "longitude": None,
                "postalCode": "74571",
                "state": "Oklahoma",
                "stateCode": "OK",
                "street": "450 Hellen Street",
            },
            "Client Suffix": "N/A",
            "Client Name": "Kevin Brown",
            "Cilent Estate Opened": None,
            "Intake Retainer Signed": "2025-01-31T00:00:00.000Z",
            "Intake Retainer Sent": "2025-01-31T00:00:00.000Z",
            "Intake Description": """Kevin was exposed to Roundup between the years 2016 - 2020
            at his residences.\n\nKevin was exposed to Roundup for approximately 30 minutes per day,
              4 days per month, 3 months out of the year, for 4 years, totaling 24 hours of
              exposure.\n\nKevin used the 1.3-gallon of Roundup ready-to-spray to eliminate weeds
              throughout the 1/4 acre landscape, 3 cars pavers driveway, 10 ft. x 10 ft. patio,
              2 ft. x 1 ft. flowerbed area, 10 ft. sidewalk, and 500 ft. fence line.\n\nKevin
              was exposed to Roundup while employed as an Groundskeeper with Cedar Creek Golf
              Course between the years 2015 - 2016.\n\nKevin was exposed to Roundup for
              approximately 1 hour per day, 4 days per month, 3 months out of the year, for 1
              years, totaling 12 hours of exposure.\n\nKevin used the 2.5-gallon of Roundup
              concentrate mixed into a container with a larger handheld pump sprayer. Kevin
              sprayed Roundup throughout the 80-acre golf course. \n\nKevin purchased Roundup
              from Poteau True Value Hardware to use at the residences and while working.
              \n\nAt the age of 37, on or about, 07/01/2022, Kevin was diagnosed with Adult
              T-cell lymphoma/leukemia, at Mercy Hospital Fort Smith located in Fort Smith,
              Arkansas.\n\nOn or about 07/25/2022, Kevin began a cycle of chemotherapy at
              Choctaw Nation Healthcare Center located in Talihina, Oklahoma.""",
            "IntakeId": "a0CTI00002Xv1df2AB",
        },
        "success": True,
    }
    return JSONResponse(content=payload)


@router.post("/document", response_class=JSONResponse)
async def document() -> JSONResponse:
    payload: DocumentResponsePayload = {
        "relatedVendorMatterId": "DEMOTEST-SELFREP-20250601",
        "documents": [
            {
                "vendorDocumentId": "DEMOTEST-SELFREPFILE-20250601",
                "tekmirDocumentId": "406becd9-de05-4aa5-a36c-5061f6032836",
            }
        ],
    }
    return JSONResponse(content=payload)


@router.post("/oauth", response_class=JSONResponse)
async def oauth() -> JSONResponse:
    payload: OauthResponsePayload = {
        "access_token": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "token_type": "Bearer",
        "expires_in": 3600,
        "scope": "user:read profile:write",
        "refresh_token": "r1t2y3u4i5o6p7q8r9s0t1u2v3w4x5y6",
    }
    return JSONResponse(content=payload)
