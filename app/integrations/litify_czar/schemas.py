"""
Copyright (c) 2025 IntakeDesk LLC. All rights reserved.
Proprietary and Confidential. Unauthorized copying, use, modification,
or distribution is prohibited.
"""

from typing import TypedDict


class CaseResponsePayload(TypedDict):
    attempt: str
    id: str
    request_id: str
    status: str
