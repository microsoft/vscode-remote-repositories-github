#!/usr/bin/env python3
"""Documentation server for this repository.

This repository is documentation only: there is no application to build. This
server renders its Markdown files as HTML and serves the repository's other
assets (for example the images under ``docs/``), so the docs can be browsed in a
browser.

Every Markdown file is read on each request, so editing one shows up on reload
without restarting the process.
"""

from __future__ import annotations

import html
import http.server
import mimetypes
import os
import pathlib
import urllib.parse

import markdown

ROOT = pathlib.Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "3000"))
EXTENSIONS = ["fenced_code", "tables", "sane_lists"]
NAV = ["README.md", "SECURITY.md", "CODE_OF_CONDUCT.md", "docs/README.md"]

PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 16px;
      line-height: 1.6;
      color: #1f2328;
      background: #f6f8fa;
    }}
    .layout {{
      display: flex;
      align-items: flex-start;
      gap: 32px;
      max-width: 1080px;
      margin: 0 auto;
      padding: 24px 24px 8px;
    }}
    nav {{
      flex: 0 0 220px;
      position: sticky;
      top: 24px;
      background: #ffffff;
      border: 1px solid #d0d7de;
      border-radius: 8px;
      padding: 16px;
    }}
    nav h2 {{
      margin: 0 0 8px;
      font-size: 12px;
      letter-spacing: .06em;
      text-transform: uppercase;
      color: #59636e;
    }}
    nav a {{ display: block; padding: 4px 0; color: #0969da; text-decoration: none; }}
    nav a:hover {{ text-decoration: underline; }}
    nav a[aria-current="page"] {{ color: #1f2328; font-weight: 600; }}
    main {{
      flex: 1 1 auto;
      min-width: 0;
      overflow-wrap: anywhere;
      background: #ffffff;
      border: 1px solid #d0d7de;
      border-radius: 8px;
      padding: 32px 40px 48px;
    }}
    main > :first-child {{ margin-top: 0; }}
    h1, h2, h3, h4 {{ line-height: 1.25; margin: 32px 0 12px; }}
    h1 {{ font-size: 2em; padding-bottom: .3em; border-bottom: 1px solid #d8dee4; }}
    h2 {{ font-size: 1.5em; padding-bottom: .3em; border-bottom: 1px solid #d8dee4; }}
    h3 {{ font-size: 1.2em; }}
    a {{ color: #0969da; }}
    code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: .9em;
      background: #eff1f3;
      border-radius: 6px;
      padding: .2em .4em;
    }}
    pre {{ background: #f6f8fa; border-radius: 6px; padding: 16px; overflow: auto; }}
    pre code {{ background: none; padding: 0; }}
    img {{ max-width: 100%; height: auto; }}
    ul, ol {{ padding-left: 24px; }}
    li {{ margin: 4px 0; }}
    hr {{ border: 0; border-top: 1px solid #d8dee4; margin: 32px 0; }}
    footer {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 24px 32px;
      color: #59636e;
      font-size: 13px;
    }}
    @media (max-width: 720px) {{
      .layout {{ flex-direction: column; align-items: stretch; gap: 16px; }}
      nav {{ position: static; }}
      main {{ padding: 24px 20px 32px; }}
    }}
  </style>
</head>
<body>
  <div class="layout">
    <nav>
      <h2>Docs</h2>
      {nav}
    </nav>
    <main>
{body}
    </main>
  </div>
  <footer>Rendered from <code>{source}</code> &mdash; edit the file and reload this page.</footer>
</body>
</html>
"""


def page_title(text: str, source: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return source


def nav_html(current: str) -> str:
    links = []
    for rel in NAV:
        if not (ROOT / rel).is_file():
            continue
        label = "Overview" if rel == "README.md" else rel
        current_attr = ' aria-current="page"' if rel == current else ""
        links.append(f'<a href="/{rel}"{current_attr}>{html.escape(label)}</a>')
    return "\n      ".join(links)


class DocsHandler(http.server.BaseHTTPRequestHandler):
    server_version = "docs-server"
    protocol_version = "HTTP/1.1"

    def do_GET(self) -> None:  # noqa: N802
        self._respond(include_body=True)

    def do_HEAD(self) -> None:  # noqa: N802
        self._respond(include_body=False)

    def _respond(self, include_body: bool) -> None:
        target = self._resolve(urllib.parse.urlparse(self.path).path)
        if target is None:
            self.send_error(404, "Not found")
            return

        if target.suffix == ".md":
            body = self._render_markdown(target)
            content_type = "text/html; charset=utf-8"
        else:
            body = target.read_bytes()
            content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if include_body:
            self.wfile.write(body)

    def _resolve(self, request_path: str):
        """Map a URL path to a file inside the repository, or None."""
        rel = urllib.parse.unquote(request_path).lstrip("/") or "README.md"
        if rel.endswith("/"):
            rel += "README.md"
        candidate = (ROOT / rel).resolve()
        if ROOT not in candidate.parents or not candidate.is_file():
            return None
        return candidate

    def _render_markdown(self, path) -> bytes:
        source = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        body = markdown.markdown(text, extensions=EXTENSIONS, output_format="html5")
        page = PAGE.format(
            title=html.escape(page_title(text, source)),
            nav=nav_html(source),
            body=body,
            source=html.escape(source),
        )
        return page.encode("utf-8")

    def log_message(self, format, *args) -> None:  # noqa: A002
        if args and str(args[1]) != "200":
            super().log_message(format, *args)


def main() -> None:
    server = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), DocsHandler)
    print(f"Docs server listening on http://0.0.0.0:{PORT}/ (serving {ROOT})", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
