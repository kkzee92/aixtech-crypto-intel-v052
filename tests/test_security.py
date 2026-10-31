from crypto_intel.security.redact import redact
from crypto_intel.security.audit import seal_event

def test_redact_key():
    assert "[REDACTED]" in redact("private key is secret123")

def test_seal_has_hashes():
    e = seal_event({"action": "test"})
    assert "sha256" in e and "sha3" in e and "blake2b" in e
