# Integrations and SDK — L_SOAPYSDR

**Project:** `L_SOAPYSDR`
**Tier:** TIER_8_RF_MESH_DEFENSE
**Domain:** RF mesh networking, tactical communications, software-defined radio, defense
**Maintainer:** Anticloud FZ LLE · 0-1.gg · lois@0-1.gg · Dubai, UAE
**Model:** Anticloud PAX L5 Narrow L2 General 27B
**AIOSS Chain:** `8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560`
**Date:** October 2026

---

## SDK Overview

`L_SOAPYSDR` ships with a Python SDK and integration packages for common platforms.

## Python SDK

```bash
pip install anticloud-l-soapysdr
```

### Core SDK Usage

```python
from anticloud.l_soapysdr import LSoapysdrClient

client = LSoapysdrClient(
    api_key="your-license-key",
    chain_genesis="8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560",
    compliance_mode="hipaa",  # or gdpr, fedramp, pci-dss
)

result = client.run(prompt="Your query here")
print(result.text)
print(f"Chain entry: {result.aioss_hash}")
```

## REST API

```
POST /v1/infer
Authorization: Bearer <license-key>
Content-Type: application/json

{
  "prompt": "Your query",
  "max_tokens": 512,
  "compliance_mode": "gdpr",
  "project": "L_SOAPYSDR"
}
```

**Response:**
```json
{
  "text": "...",
  "aioss_entry_hash": "sha3-256-hash",
  "latency_ms": 508,
  "tokens_used": 312,
  "compliance_checks": {"gdpr": "PASS", "pii_detected": false}
}
```

## Platform Integrations

| Platform | Integration | Status |
|---|---|---|
| GitHub Actions | `.github/workflows/anticloud-ci.yml` | Available |
| Slack | api-oss-integrations-slack | Available |
| Zapier | api-oss-integrations-zapier | Available |
| Kubernetes | `kubernetes-manifests/` | Available |
| Terraform (AWS) | `terraform-aws/` | Available |
| Docker Compose | `docker-compose/` | Available |

## WebHook Integration

```python
from anticloud.webhooks import AIAOSSWebhook

hook = AIAOSSWebhook(
    endpoint="https://your-system.example.com/aioss",
    secret="your-webhook-secret",
    events=["inference.complete", "chain.update", "compliance.alert"],
)
hook.register()
```

## SDK Reference Documentation

Full SDK reference is auto-generated from type stubs and published at 0-1.gg/docs/l-soapysdr.

**Support:** lois@0-1.gg · 0-1.gg
