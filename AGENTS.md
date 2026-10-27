# Repository notes

## What this repository is

Documentation only: `README.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, the licence files,
and images under `docs/`. There is no application source, no package manifest, no build
step and no test suite — nothing to compile, migrate or unit-test.

The extensions described in the README (GitHub Repositories, Azure Repos) are not
developed or published in this repository; it exists for their README content and for
feedback. The only runnable artifact here is the documentation viewer added for the
Base44 sandbox.

## Running it

- `docker compose -f docker-compose.base44.yml up -d` → docs viewer on http://localhost:3000
- Without Docker: `pip install -r requirements-docs.txt && python docs_server.py`
  (honours `PORT`, defaults to 3000, binds `0.0.0.0`).

`docs_server.py` renders Markdown with the `markdown` package (pinned in
`requirements-docs.txt`, installed on container start) and serves the repository's other
files — `docs/*.png`, `LICENSE`, etc. — so relative image links resolve. Any `*.md` path
is rendered (`/`, `/README.md`, `/SECURITY.md`, `/docs/README.md`, `/docs/`), everything
else is served as-is, and anything outside the checkout is a 404.

Markdown is read on every request, so an edit is visible on reload with no restart and no
build step.

## Quirks and environment notes

- No credentials, database or external service is needed; the app does not read any
  secrets and has no `/run/base44/app.env` wiring.
- No sandbox-specific overrides are needed: `http.server` does not validate `Host` or
  `Origin`, so nothing depends on `BASE44_PREVIEW_MODE`.
- The container installs its one dependency at startup because nothing is baked into the
  image; the image stays a plain runtime so the bind-mounted source is always live.

## Verifying

- `curl -s http://localhost:3000/ | grep -q "Remote Repositories"` — the compose
  healthcheck does the same check against `/`.
- `curl -s -o /dev/null -w '%{http_code}\n' http://localhost:3000/docs/continue-on.png`
  should be `200`.
