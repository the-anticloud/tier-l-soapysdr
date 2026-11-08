# L5 Narrow / L2 General Classification — L_SOAPYSDR
**Platform:** Anticloud | **Tier:** TIER_8_RF_MESH_DEFENSE | **PAX:** 27B
**IP:** USPTO pending 2026, Anticloud FZ LLE, 0-1.gg | **License:** Apache-2.0

## L5 Narrow
L_SOAPYSDR provides the SoapySDR hardware abstraction layer for Anticloud: a single Python API for RTL-SDR, HackRF, LimeSDR, USRP, and other SDR hardware. Narrow scope: Anticloud SDR hardware abstraction.

## L2 General
L2 General: L_SOAPYSDR abstracts SDR hardware for all Anticloud RF modules. L_OPENWEBRX, L_RETICULUM, and L_SIGUTILS all use L_SOAPYSDR's hardware API. Swap SDR hardware without changing RF code.

## PAX 27B Integration
PAX 27B assists with SDR hardware configuration: 'For Anticloud tactical mesh in EU868 band, configure SoapySDR with gain=30dB and sample rate 1.25MSPS for optimal LoRa decoding.'

## AIOSS Audit Chain
Every SDR hardware event (device hash + configuration hash + sample batch hash + hardware health) is chained: H_n = SHA3-256(H_{n-1} || entry_hash_n || timestamp_n).
Offline-verifiable, tamper-evident, zero cloud dependency.

## Regulatory / Compliance
FCC Part 15 (SDR hardware). Passive receive by default. Transmit requires license.
