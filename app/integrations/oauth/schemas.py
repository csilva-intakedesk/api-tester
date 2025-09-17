"""
Copyright (c) 2025 IntakeDesk LLC. All rights reserved.
Proprietary and Confidential. Unauthorized copying, use, modification,
or distribution is prohibited.
"""

from typing import TypedDict


class OauthResponsePayload(TypedDict):
    access_token: str
    token_type: str
    expires_in: int
    scope: str
    refresh_token: str
