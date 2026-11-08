"""
AIOSS (Anticloud I/O Sovereign System) integration for L_SOAPYSDR.
Wraps every call with a hash-chained audit ledger entry.
"""
import hashlib, json, time
from pathlib import Path

LEDGER_PATH = Path(__file__).parent / "ledger" / "aioss_ledger.jsonl"
LEDGER_PATH.parent.mkdir(exist_ok=True)

_prev_hash = "0" * 64

def log_call(event: str, data: dict):
    global _prev_hash
    payload = json.dumps({"event": event, "data": data, "ts": time.time()}, sort_keys=True)
    results_hash = hashlib.sha256(payload.encode()).hexdigest()
    chain_hash = hashlib.sha256((_prev_hash + results_hash).encode()).hexdigest()
    entry = {"event": event, "results_hash": results_hash,
              "prev_hash": _prev_hash, "chain_hash": chain_hash}
    with open(LEDGER_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")
    _prev_hash = chain_hash
    return chain_hash
