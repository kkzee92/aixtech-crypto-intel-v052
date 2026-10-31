"""Hash-chained audit log with multi-hash seal. v0.52."""
import hashlib
import json
from datetime import datetime, timezone

def seal_event(event: dict, prev_hash: str = "") -> dict:
    event["timestamp"] = datetime.now(timezone.utc).isoformat()
    event["prev_hash"] = prev_hash
    event["residency"] = "synthetic"
    payload = json.dumps(event, sort_keys=True).encode()
    event["sha256"] = hashlib.sha256(payload).hexdigest()
    event["sha3"] = hashlib.sha3_256(payload).hexdigest()
    event["blake2b"] = hashlib.blake2b(payload, digest_size=32).hexdigest()
    return event
