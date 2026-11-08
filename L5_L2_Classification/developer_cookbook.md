# Developer Cookbook — L_SOAPYSDR
**Stack:** Python 3.11, SoapySDR (C++ + Python bindings), numpy, PAX 27B, AIOSS_FORMAT
**Domain:** SoapySDR: universal SDR hardware abstraction for Anticloud RF systems

## SDR hardware abstraction
```python
from l_soapysdr import SoapySDRClient

sdr = SoapySDRClient(
    driver="rtlsdr",
    pax_model="./pax-27b-q4.gguf",
    aioss_chain="./soapysdr.aioss"
)

# Get PAX-recommended config for task
config = sdr.pax_configure(
    task="lora_868mhz",
    constraints={"bandwidth_hz": 250_000}
)
print(f"Configured: freq={config.freq_hz/1e6:.3f}MHz, gain={config.gain}dB")

# Stream IQ samples
for batch in sdr.stream(n_samples=1024):
    process(batch)
```

## AIOSS Chain Append
```python
import hashlib, time

def aioss_append(chain_path, payload: bytes, module_id: str):
    entry_hash = hashlib.sha3_256(payload).digest()
    ts = int(time.time_ns()).to_bytes(8, 'big')
    with open(chain_path, 'rb') as f:
        f.seek(-32, 2); prev_hash = f.read(32)
    new_hash = hashlib.sha3_256(prev_hash + entry_hash + ts).digest()
    with open(chain_path, 'ab') as f:
        f.write(ts + entry_hash + new_hash)
    return new_hash.hex()
```
