"""
Copyright (c) 2025 IntakeDesk LLC. All rights reserved.
Proprietary and Confidential. Unauthorized copying, use, modification,
or distribution is prohibited.
"""

from typing import TypedDict


class DocumentPayload(TypedDict):
    vendorDocumentId: str
    tekmirDocumentId: str


class DocumentResponsePayload(TypedDict):
    relatedVendorMatterId: str
    documents: list[DocumentPayload]


class CaseResponsePayload(TypedDict):
    intakeId: str
    message: str
