#!/usr/bin/env python3
"""Minimal Reddit posting CLI used for the launch.

Reads credentials from .env.reddit (gitignored) or the process environment.

Supported auth:
  script app:   REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET,
                REDDIT_USERNAME, REDDIT_PASSWORD
  refresh token: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_REFRESH_TOKEN

Usage:
  reddit_post.py --check
  reddit_post.py --subreddit privacy --title "..." --body-file post.md
  reddit_post.py --subreddit OSINT --title "..." --url https://example.com
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

import praw
from praw.exceptions import RedditAPIException

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env.reddit"
USER_AGENT = "awesome-spyware-detection-launch/0.1"


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def make_reddit() -> praw.Reddit:
    client_id = os.environ.get("REDDIT_CLIENT_ID")
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
    if not client_id or not client_secret:
        sys.exit(
            "Missing REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET.\n"
            "Copy .env.reddit.example to .env.reddit and fill it in."
        )

    refresh_token = os.environ.get("REDDIT_REFRESH_TOKEN")
    username = os.environ.get("REDDIT_USERNAME")
    password = os.environ.get("REDDIT_PASSWORD")

    if refresh_token:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
            user_agent=USER_AGENT,
        )
    elif username and password:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            user_agent=USER_AGENT,
        )
    else:
        sys.exit("Set either REDDIT_REFRESH_TOKEN or REDDIT_USERNAME + REDDIT_PASSWORD.")

    reddit.validate_on_submit = True
    return reddit


def main() -> int:
    parser = argparse.ArgumentParser(description="Post to Reddit for the launch.")
    parser.add_argument("--subreddit", help="Subreddit name without r/")
    parser.add_argument("--title", help="Post title")
    parser.add_argument("--body", help="Self-post body")
    parser.add_argument("--body-file", help="Read the self-post body from a file")
    parser.add_argument("--url", help="Link post URL (instead of a self post)")
    parser.add_argument("--check", action="store_true", help="Verify auth and print the user")
    parser.add_argument("--dry-run", action="store_true", help="Print the payload without posting")
    args = parser.parse_args()

    load_env(ENV_FILE)
    reddit = make_reddit()

    if args.check:
        me = reddit.user.me()
        print(f"authenticated as u/{me}")
        return 0

    if not args.subreddit or not args.title:
        parser.error("--subreddit and --title are required unless --check is used")

    body = args.body
    if args.body_file:
        body = Path(args.body_file).read_text()
    if not args.url and not body:
        parser.error("Provide --body, --body-file, or --url")

    payload = {
        "subreddit": args.subreddit,
        "title": args.title,
        "kind": "link" if args.url else "self",
        "url": args.url,
        "body_chars": len(body or ""),
        "body_preview": (body or "")[:160].replace("\n", " "),
    }
    print("payload:", payload)

    if args.dry_run:
        return 0

    subreddit = reddit.subreddit(args.subreddit)
    try:
        if args.url:
            submission = subreddit.submit(title=args.title, url=args.url)
        else:
            submission = subreddit.submit(title=args.title, selftext=body)

        # Reddit may rate-limit immediately after submit; poll briefly for the URL.
        for _ in range(10):
            if getattr(submission, "shortlink", None):
                break
            time.sleep(1)

        print(f"posted: https://www.reddit.com{submission.permalink}")
        print(f"id: {submission.id}  author: u/{submission.author}")
        return 0
    except RedditAPIException as exc:
        for item in exc.items:
            print(f"error: {item.error_type}: {item.message}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
