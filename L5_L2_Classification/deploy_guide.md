# Deploy Guide — L_SOAPYSDR
**Tier:** TIER_8_RF_MESH_DEFENSE | **Stack:** Python 3.11, SoapySDR (C++ + Python bindings), numpy, PAX 27B, AIOSS_FORMAT
**Air-gap capable after initial setup.**

## Prerequisites
Python 3.11+, SoapySDR (C++ build + Python bindings), supported SDR hardware (RTL-SDR, HackRF, etc.).

## Environment
SoapySDR C++ library installed. RTL-SDR, HackRF, or other SoapySDR-supported hardware. 4GB RAM.

## AIOSS Integration
```bash
aioss init --module L_SOAPYSDR --output ./l_soapysdr.aioss
aioss append --chain ./l_soapysdr.aioss --payload ./output.bin --module L_SOAPYSDR
aioss verify --chain ./l_soapysdr.aioss
```

## Air-Gap Setup
```bash
pip download -r requirements.txt -d ./wheels/
pip install --no-index --find-links ./wheels/ -r requirements.txt
```

## PAX 27B Harness Wiring
```python
from anticloud_pax import PAXHarness
harness = PAXHarness(
    model_path="./pax-27b-q4.gguf",
    module="L_SOAPYSDR",
    aioss_chain="./L_SOAPYSDR.aioss",
    classification="L5_NARROW_L2_GENERAL"
)
result = harness.process(input_data)
```

## Verification
```bash
aioss verify --chain ./L_SOAPYSDR.aioss --verbose
python -m L_SOAPYSDR.tests.smoke
```
