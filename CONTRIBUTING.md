# Contributing

Thanks for taking the time to contribute. Here's everything you need to get started.

## Development Setup

1. **Clone the repo**

   ```bash
   git clone <repo-url>
   cd ecommerce-aws-platform
   ```

2. **Python services** — create a virtual environment at the repo root:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Frontend**

   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Start infrastructure** (Postgres, Redis, LocalStack, OpenSearch):

   ```bash
   docker compose up -d postgres redis localstack opensearch
   ```

## Branch Naming

| Type | Pattern | Example |
|---|---|---|
| Feature | `feature/<short-description>` | `feature/add-wishlist` |
| Bug fix | `fix/<short-description>` | `fix/cart-quantity-overflow` |
| Chore / maintenance | `chore/<short-description>` | `chore/upgrade-fastapi` |

Always branch off `develop`. PRs targeting `main` are reserved for releases.

## Pull Request Process

1. Open a PR against `develop` (not `main`).
2. Fill in the PR template — describe what changed and why.
3. Ensure CI passes (lint, type-check, tests).
4. Request at least one review.
5. Squash-merge once approved.

## Code Style

### Python

We use [ruff](https://docs.astral.sh/ruff/) for both linting and formatting.

```bash
make lint   # check
make fmt    # auto-fix
```

- Line length: 100
- Target: Python 3.11
- Follow PEP 8 naming conventions.
- Add type hints to all public functions.

### TypeScript / React

We use ESLint (Next.js default config) and Prettier.

```bash
cd frontend
npm run lint        # ESLint
npm run type-check  # tsc --noEmit
```

- Prefer named exports over default exports for components.
- Use `const` arrow functions for React components.
- Keep components small and focused.

## Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short summary>

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`

Examples:

```
feat(cart): add quantity update endpoint
fix(payment): handle Stripe webhook signature mismatch
chore(deps): upgrade fastapi to 0.111.0
```

## Running Tests

```bash
# All Python services
make test

# Single service
cd services/order && pytest tests/ -v

# Frontend
cd frontend && npm run type-check && npm run lint
```
