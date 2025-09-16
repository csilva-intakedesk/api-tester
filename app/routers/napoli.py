from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response

router = APIRouter()


@router.post("/ClientHCPs", response_class=JSONResponse)
async def ClientHCPs():
    payload = {
        "facilityName": "string",
        "fName": "string",
        "lName": "string",
        "address1": "string",
        "address2": "string",
        "city": "string",
        "state": "str",
        "zip": "string",
        "primaryHCP": True,
        "initialVisit": "2024-07-25T20:05:49.858Z",
        "lastVisit": "2024-07-25T20:05:49.858Z",
        "role": 0,
        "specialty": 0,
        "notes": "string",
        "sysid": "stringstringstri",
        "zipPlus4": "string",
        "phone": "string",
        "faxNumber": "string",
        "npi": "string",
    }
    return JSONResponse(content=payload)


@router.post("/ClientHCPsWithInjuries", response_class=JSONResponse)
async def ClientHCPsWithInjuries():
    payload = {
        "facilityName": "string",
        "fName": "string",
        "lName": "string",
        "address1": "string",
        "address2": "string",
        "city": "string",
        "state": "str",
        "zip": "string",
        "primaryHCP": True,
        "initialVisit": "2024-07-25T20:06:45.430Z",
        "lastVisit": "2024-07-25T20:06:45.430Z",
        "role": 0,
        "specialty": 0,
        "notes": "string",
        "sysid": "stringstringstri",
        "zipPlus4": "string",
        "phone": "string",
        "faxNumber": "string",
        "npi": "string",
        "injuries": [
            {
                "sysid": "stringstringstri",
                "injury_ID": "string",
                "injury_Date": "2024-07-25T20:06:45.430Z",
                "confirmation": "string",
                "hcpid": 0,
            }
        ],
    }
    return JSONResponse(content=payload)


@router.post("/ClientInjuries/{sysid}", response_class=JSONResponse)
async def ClientInjuries(sysid: str):
    payload = [
        {
            "sysid": "stringstringstri",
            "injury_ID": "string",
            "injury_Date": "2024-07-25T20:07:47.538Z",
            "confirmation": "string",
            "hcpid": 0,
        }
    ]
    return JSONResponse(content=payload)


@router.post("/ClientStage", response_class=JSONResponse)
async def ClientStage():
    payload = {
        "leadID": "string",
        "ccode": "stri",
        "salutation": "string",
        "lname": "string",
        "fname": "string",
        "mi": "s",
        "address1": "string",
        "address2": "string",
        "city": "string",
        "state": "str",
        "zipCode": "string",
        "country": "string",
        "province": "string",
        "homePhone": "string",
        "workPhone": "string",
        "mobilePhone": "string",
        "emailAddress": "user@example.com",
        "ssn": "string",
        "dob": "2024-07-25",
        "injury": "string",
        "additionalNotes": "string",
        "deceased": True,
        "dateOfDeath": "2024-07-25",
        "trade": "string",
        "industry": "string",
        "campaignID": "string",
        "leadSourceID": 0,
        "stage": "string",
    }
    return JSONResponse(content=payload)


@router.post("/EmergencyContact/{sysid}", response_class=JSONResponse)
async def EmergencyContact(sysid: str):
    payload = {
        "sysid": "string",
        "altFirstName": "string",
        "altLastName": "string",
        "altAddress": "string",
        "altAddress2": "string",
        "altCity": "string",
        "altState": "string",
        "altZip": "string",
        "altHome": "string",
        "altCell": "string",
        "altEmail": "string",
        "altRelationship": "string",
        "altSalutaion": "string",
        "altMI": "string",
        "altZipPlus4": "string",
        "entered": "2024-07-25T20:03:47.390Z",
        "username": "string",
    }
    return JSONResponse(content=payload)


@router.post("/Fiduciary", response_class=JSONResponse)
async def Fiduciary():
    payload = {
        "fiduciary_Type": "string",
        "fiduciary_Salutation": "string",
        "fiduciary_Fname": "string",
        "fiduciary_Mi": "s",
        "fiduciary_Lname": "string",
        "address1": "string",
        "address2": "string",
        "city": "string",
        "state": "string",
        "phone": "string",
        "mobile": "string",
        "zip_Code": "string",
        "updated": "2024-07-25T20:02:48.713Z",
        "relationship": 0,
        "pl_Legal_Status": "string",
        "workPhone": "string",
        "email": "string",
        "cause_Of_Death": "string",
        "death_State": "string",
        "death_Zip": "string",
        "fkafidCheck": 0,
        "fkafidFname": "string",
        "fkafidMi": "s",
        "fkafidLname": "string",
        "fkafidSal": "string",
        "courtAppointed": 0,
        "deathLocation": "string",
        "dob": "2024-07-25T20:02:48.713Z",
        "soulHeir": True,
        "nonHeir": True,
        "zipPlus4": "stri",
    }
    return JSONResponse(content=payload)


@router.post("/FileUpload", response_class=JSONResponse)
async def FileUpload():
    payload = {
        "uploadId": 0,
        "sysID": "string",
        "lockCode": 0,
        "lockID": 0,
        "typeCode": 0,
        "description": "string",
        "uploadDate": "2024-07-25T19:59:10.938Z",
        "executionDate": "2024-07-25T19:59:10.938Z",
        "fileName": "string",
        "fileType": "string",
    }
    return JSONResponse(content=payload)


@router.post("/GetNewSysId", response_class=JSONResponse)
async def GetNewSysId():
    payload = {
        "LeadID": "166987",
        "CCODE": "MSW",
        "Salutation": "Mr.",
        "Lname": "Hill",
        "Fname": "Ricky",
        "MI": None,
        "Address1": "8775 Dickerson Mill Road",
        "Address2": None,
        "City": "Moneta",
        "State": "VA",
        "ZipCode": "24121",
        "Country": "USA",
        "Province": None,
        "HomePhone": "5405807327",
        "WorkPhone": None,
        "MobilePhone": None,
        "EmailAddress": "rickspandmemail@gmail.com",
        "SSN": "9259",
        "DOB": "1963-05-28T00:00:00",
        "Injury": None,
        "AdditionalNotes": "Power of Attorney? N/A\r\nBest Contact Time: Anytime - Eastern Standard Time (EST) - Any Day\r\nClient Contact Notes: Prefers to be called Rick.\n\nRicky does not feel comfortable providing the full SSN at this time and will provide it to the paralegal/attorney.\r\nInjured Party Marital Status: Married\r\nExecutor of Will: No\r\nEstate Representative: No\r\nTotal Exposure Start/Stop Years: <b>From:</b> 09/01/1984 <b>To:</b> 01/01/2000\r\nTotal Lifetime Exposure: 16 year(s)\r\nPhase One List Match: Yes, 2 Phase One location(s) matched.\r\nPWS ID Matches: PWS ID: VA2770900\r\nPWS Name: WESTERN VIRGINIA WATER AUTHORITY\r\nPWS ZIP Code(s): 24019\r\nPWS State: VA\r\nPrimary Source: Surfacewater \r\nPWS Name: McClellan AFB\r\nBlood Tested for PFAS: No\r\nSummary: SENT USPS PACKAGE TO CLIENT WITH HIPAA AUTHORIZATIONS TO EXECUTE WITH AN ORIGINAL SIGNATURE AND RETURN IN PRE-PAID POSTAGE ENVELOPE.\r\nTRACKING #: 9405511206224849462264\r\nRETURN TRACKING #: 9405511206224849462240\r\n(SEE ATTACHED LABEL)\r\n\r\nRicky claims he was exposed to PFAS-contaminated drinking water while living and working at 1 location between the years 1987 - 2000 that are on the Phase One list.\r\n\r\nRicky served in the military from 1982 - 1985. Ricky claims he was exposed to PFAS-contaminated drinking water while working/living on a military base between the years 1984 - 1985 that are on the Phase One list.\r\n\r\nRicky was exposed for approximately 6 years prior to being diagnosed with Testicular Cancer.\r\n\r\nAt the age of 49, in May 2013, Ricky was diagnosed with Testicular Cancer at Centra Bedford Memorial Hospital in Bedford, Virginia.\r\n\r\nIn May 2013, Ricky had a total orchiectomy performed at Centra Virginia Baptist Hospital located in Bedford, Virginia.\r\n\r\nAt the age of 59, in May 2023, Ricky was diagnosed with Testicular Cancer at Centra Bedford Memorial Hospital in Bedford, Virginia.\r\n\r\nIn May 2023, Ricky began a cycle of chemotherapy at Centra Alan B. Pearson Regional Cancer Center in Lynchburg, Virginia.\r\n",
        "Deceased": False,
        "DateOfDeath": None,
        "Trade": None,
        "Industry": None,
        "CampaignID": "PFAS",
        "LeadSourceID": 320,
        "ID": 174995,
        "DateEntered": "2024-07-16T11:39:59.8235709-04:00",
        "Processed": False,
        "ProcessedDate": None,
        "ActionID": 0,
        "SYSID": "C66B7E02D466ACF4",
    }
    return JSONResponse(content=payload)


@router.post("/ResidentialHistory", response_class=JSONResponse)
async def ResidentialHistory():
    payload = {
        "sysid": "string",
        "address1": "string",
        "address2": "string",
        "city": "string",
        "state": "str",
        "zip": "string",
        "zipPlus4": "stri",
        "startDate": "string",
        "endDate": "string",
        "inUtero": True,
        "waterSupplyType": 0,
        "propertyType": 0,
    }
    return JSONResponse(content=payload)


@router.post("/Token", response_class=Response)
async def Token():
    return JSONResponse(content="Ym9zY236Ym9zY28=")
