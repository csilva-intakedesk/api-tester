from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_healthz() -> None:
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_litify_case() -> None:
    r = client.post("/litify/case")
    assert r.status_code == 200
    j = r.json()
    assert "intakeId" in j and "message" in j


def test_smart_case_works_post_document() -> None:
    r = client.post("/smart_case_works/document")
    assert r.status_code == 200
    assert r.headers.get("content-type", "").startswith("application/xml")
    text = r.text
    assert text.startswith('<?xml version="1.0" encoding="utf-8"?>OK')


def test_napoli_emergency_contact_sysid() -> None:
    sysid = "C66B7E02D466ACF4"
    r = client.post(f"/napoli/EmergencyContact/{sysid}")
    assert r.status_code == 200
    j = r.json()
    assert j.get("sysid") == sysid
