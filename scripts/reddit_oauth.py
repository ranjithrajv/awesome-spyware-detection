#!/usr/bin/env python3
"""One-time Reddit OAuth helper for the launch.

Creates a refresh token using an "installed app" so no password is stored.

Prerequisites in .env.reddit:
  REDDIT_CLIENT_ID=...
  REDDIT_CLIENT_SECRET=...
  REDDIT_REDIRECT_URI=http://localhost:8080   # optional, this is the default

Run:
  .venv-reddit/bin/python scripts/reddit_oauth.py

It prints an authorization URL, waits for the redirect on localhost, exchanges
the code, and writes REDDIT_REFRESH_TOKEN back to .env.reddit.
"""

from __future__ import annotations

import base64
import http.server
import json
import os
import secrets
import sys
import threading
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env.reddit"
USER_AGENT = "awesome-spyware-detection-launch/0.1"
SCOPES = "identity read submit"
DEFAULT_REDIRECT = "http://localhost:8080"


def load_env(path: Path) -> None:
    if not path.exists():
        sys.exit(f"Missing {path}. Copy .env.reddit.example and fill in the app credentials.")
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def write_refresh_token(token: str) -> None:
    lines = ENV_FILE.read_text().splitlines()
    out, replaced = [], False
    for line in lines:
        if line.strip().startswith("REDDIT_REFRESH_TOKEN="):
            out.append(f"REDDIT_REFRESH_TOKEN={token}")
            replaced = True
        else:
            out.append(line)
    if not replaced:
        out.append(f"REDDIT_REFRESH_TOKEN={token}")
    ENV_FILE.write_text("\n".join(out) + "\n")
    ENV_FILE.chmod(0o600)


def main() -> int:
    load_env(ENV_FILE)
    client_id = os.environ.get("REDDIT_CLIENT_ID")
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
    redirect_uri = os.environ.get("REDDIT_REDIRECT_URI", DEFAULT_REDIRECT)
    if not client_id or not client_secret:
        sys.exit("REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET must be set in .env.reddit")

    parsed = urllib.parse.urlparse(redirect_uri)
    host = parsed.hostname or "localhost"
    port = parsed.port or 8080
    state = secrets.token_urlsafe(16)

    auth_url = "https://www.reddit.com/api/v1/authorize?" + urllib.parse.urlencode(
        {
            "client_id": client_id,
            "response_type": "code",
            "state": state,
            "redirect_uri": redirect_uri,
            "duration": "permanent",
            "scope": SCOPES,
        }
    )

    result: dict[str, str] = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            result.update({k: v[0] for k, v in query.items() if v})
            body = b"Reddit authorization received. You can close this tab."
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            threading.Thread(target=self.server.shutdown, daemon=True).start()

        def log_message(self, *args) -> None:
            pass

    server = http.server.HTTPServer((host, port), Handler)
    print("Open this URL while signed in to Reddit:\n")
    print(auth_url)
    print(f"\nWaiting for the redirect on {redirect_uri} ...")
    server.serve_forever()

    if result.get("state") != state:
        sys.exit("State mismatch; aborting.")
    if "error" in result:
        sys.exit(f"Authorization error: {result['error']}")
    code = result.get("code")
    if not code:
        sys.exit(f"No code in redirect: {result}")

    data = urllib.parse.urlencode(
        {"grant_type": "authorization_code", "code": code, "redirect_uri": redirect_uri}
    ).encode()
    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    request = urllib.request.Request(
        "https://www.reddit.com/api/v1/access_token",
        data=data,
        headers={
            "Authorization": f"Basic {credentials}",
            "User-Agent": USER_AGENT,
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode())

    if "refresh_token" not in payload:
        sys.exit(f"No refresh token returned: {payload}")

    write_refresh_token(payload["refresh_token"])
    print("Refresh token saved to .env.reddit")
    print(f"scopes: {payload.get('scope', 'unknown')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
