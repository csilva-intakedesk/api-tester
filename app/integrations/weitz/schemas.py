"""
Copyright (c) 2025 IntakeDesk LLC. All rights reserved.
Proprietary and Confidential. Unauthorized copying, use, modification,
or distribution is prohibited.
"""

from pydantic import BaseModel


class CaseResponsePayload(BaseModel):
    Success: str
    Message: str
    IntakeID: str
    SystemError: str | None = None
