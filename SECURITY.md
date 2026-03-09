# Security Policy

## About This Project

CordovaOS is a **demo and reference implementation** for SDC4 cross-domain interoperability. It contains only synthetic data for the fictional Republic of Cordova. No real personal, financial, or government data is present in this repository.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 4.x.x   | Yes       |
| < 4.0   | No        |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, report vulnerabilities via email to: **security@axius-sdc.com**

Include the following in your report:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### What to Report

- API key authentication bypass
- GraphDB/triplestore unauthorized access
- CSRF, XSS, or injection vulnerabilities
- Django security misconfigurations
- Credential exposure in code or configuration
- Docker container escape or privilege escalation

### What Not to Report

- Default credentials in `.env.example` (these are intentional demo defaults)
- Synthetic data content (all data is fictional by design)
- Vulnerabilities in upstream dependencies without a CordovaOS-specific exploit path

## Response Timeline

| Stage | Timeline |
|-------|----------|
| Acknowledgment | Within 48 hours |
| Initial assessment | Within 5 business days |
| Status updates | Every 7 days until resolved |
| Fix release | Depends on severity |

## Severity Levels

- **Critical**: Remote code execution, authentication bypass, data exfiltration
- **High**: Privilege escalation, significant access control failures
- **Medium**: XSS, CSRF, information disclosure
- **Low**: Minor misconfigurations, hardening recommendations

## Disclosure Policy

We follow coordinated disclosure. We ask that you:

1. Allow us reasonable time to investigate and fix the issue
2. Do not exploit the vulnerability beyond what is necessary to demonstrate it
3. Do not disclose the vulnerability publicly until we have released a fix

We will credit reporters in the fix announcement unless anonymity is requested.
