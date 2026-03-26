# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| `main` branch | ✅ |
| `develop` branch | ✅ (pre-release) |
| Older tags | ❌ |

We only provide security fixes for the current `main` branch. Please upgrade before reporting.

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Please report security issues via private disclosure:

1. Email **security@example.com** with the subject line `[SECURITY] <brief description>`.
2. Include:
   - A description of the vulnerability and its potential impact.
   - Steps to reproduce or a proof-of-concept (if safe to share).
   - Any suggested mitigations.
3. You will receive an acknowledgement within **48 hours** and a status update within **7 days**.
4. We will coordinate a fix and disclosure timeline with you before publishing anything publicly.

We follow [responsible disclosure](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure) and will credit reporters in release notes unless you prefer to remain anonymous.

## Security Considerations

### Authentication & Authorization

- All service-to-service calls must include a valid JWT issued by AWS Cognito.
- The API Gateway validates tokens before forwarding requests to services.
- Never expose internal service ports (8001–8009) publicly — they should only be reachable within the VPC.

### Secrets Management

- All secrets (database credentials, Stripe keys, etc.) are stored in AWS Secrets Manager.
- Services retrieve secrets at startup via the AWS SDK — never hardcode credentials.
- Rotate secrets regularly using Secrets Manager rotation policies.
- The `.env` files are for local development only and must never be committed (they are in `.gitignore`).

### Data

- All data in transit is encrypted via TLS (enforced at the API Gateway and ALB layers).
- Aurora PostgreSQL and ElastiCache are encrypted at rest.
- S3 buckets have server-side encryption enabled and public access blocked.
- PII should be minimised; do not log sensitive customer data.

### Container Security

- All service images run as a non-root user (`appuser`).
- Base images are pinned to specific versions and should be updated regularly.
- Scan images for vulnerabilities using Amazon ECR image scanning or a third-party tool before deploying to production.

### Infrastructure

- VPC security groups follow least-privilege: services only accept traffic from the ALB or other services that need to call them.
- WAF rules are applied at the CloudFront and API Gateway layers.
- IAM roles follow least-privilege; avoid wildcard permissions.
- Enable AWS CloudTrail and GuardDuty in all environments.

### Dependency Management

- Keep Python and Node.js dependencies up to date.
- Use `pip audit` and `npm audit` in CI to catch known vulnerabilities.
- Dependabot or Renovate is recommended for automated dependency updates.
