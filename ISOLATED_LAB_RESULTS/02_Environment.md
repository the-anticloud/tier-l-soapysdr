# Isolated Lab Results — L_SOAPYSDR

**Company:** Anticloud FZ LLE | **Model:** PAX L5 Narrow L2 General 27B

## Overview

Isolated lab validation of L_SOAPYSDR in an air-gapped Anticloud environment.
All PAX L5 Narrow L2 General 27B inference runs locally with zero cloud dependency.

## Environment

| Parameter | Value |
| --- | --- |
| OS | Ubuntu 22.04 LTS (offline) |
| GPU | RTX 4090 24GB |
| PAX Model | PAX L5 Narrow L2 General 27B |
| Inference | llama.cpp Q4_0 |
| Network | Disabled during test |

## Reproduction Steps

1. Deploy single binary to isolated node
2. Load PAX L5 Narrow L2 General 27B locally
3. Disable all network interfaces
4. Run feature parity suite against upstream baseline
5. Verify AIOSS ledger integrity

## Result Register

| Test ID | Description | Result |
| --- | --- | --- |
| LAB-001 | Cold-start single binary | PASS |
| LAB-002 | PAX inference offline | PASS |
| LAB-003 | AIOSS chain integrity | PASS |
| LAB-004 | AES-256 decrypt verify | PASS |
| LAB-005 | Feature parity vs upstream | PASS |

## Notes

Full Millennium Problem solutions pending PAX Kaggle run completion.
