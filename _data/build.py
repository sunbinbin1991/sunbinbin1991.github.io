# -*- coding: utf-8 -*-
"""Standalone builder: fetch user + repos + recent public events, write data.js.

Works locally and inside GitHub Actions (repo root = script's parent's parent).
"""
import collections
import json
import os
import sys
import time
import urllib.request

BASE = "https://api.github.com"
LOGIN = "sunbinbin1991"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data.js")

HEADERS = {
    "User-Agent": "portfolio-builder",
    "Accept": "application/vnd.github+json",
}


def get(path):
    req = urllib.request.Request(BASE + path, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_user():
    return get(f"/users/{LOGIN}")


def fetch_repos():
    repos = []
    page = 1
    while True:
        batch = get(f"/users/{LOGIN}/repos?per_page=100&page={page}&sort=updated&type=all")
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
        time.sleep(0.2)
    return repos


def fetch_events():
    """Map public events to a display-friendly summary list."""
    try:
        evs = get(f"/users/{LOGIN}/events/public?per_page=30")
    except Exception:
        return []
    out = []
    for e in evs:
        t = e.get("type", "")
        repo = e.get("repo", {}).get("name", "")
        if not repo:
            continue
        repo_url = "https://github.com/" + repo
        payload = e.get("payload", {}) or {}
        item = {
            "type": t,
            "repo": repo,
            "repo_url": repo_url,
            "created_at": e.get("created_at", ""),
        }
        if t == "PushEvent":
            n = len(payload.get("commits", []) or [])
            ref = (payload.get("ref") or "").replace("refs/heads/", "")
            item["text"] = f"推送 {n} 个提交到 {repo} @ {ref}"
        elif t == "CreateEvent":
            rt = payload.get("ref_type", "")
            item["text"] = f"创建了 {rt}: {repo}"
        elif t == "DeleteEvent":
            rt = payload.get("ref_type", "")
            item["text"] = f"删除了 {rt}: {repo}"
        elif t == "ForkEvent":
            item["text"] = f"Fork 了 {repo}"
        elif t == "WatchEvent":
            item["text"] = f"Star 了 {repo}"
        elif t == "ReleaseEvent":
            item["text"] = f"发布了 Release: {repo}"
        elif t == "PullRequestEvent":
            item["text"] = f"{payload.get('action', '')} 了 PR: {repo}"
        elif t == "IssuesEvent":
            item["text"] = f"{payload.get('action', '')} 了 Issue: {repo}"
        elif t == "IssueCommentEvent":
            item["text"] = f"评论了 Issue: {repo}"
        elif t == "PublicEvent":
            item["text"] = f"开源了新项目: {repo}"
        elif t == "GollumEvent":
            item["text"] = f"更新了 Wiki: {repo}"
        else:
            item["text"] = f"{t}: {repo}"
        out.append(item)
    return out


def clean_repo(r):
    return {
        "name": r["name"],
        "description": (r.get("description") or "").strip(),
        "html_url": r["html_url"],
        "homepage": r.get("homepage") or "",
        "language": r.get("language") or "",
        "stars": r["stargazers_count"],
        "forks": r["forks_count"],
        "topics": r.get("topics") or [],
        "created_at": r["created_at"],
        "updated_at": r["updated_at"],
        "fork": bool(r["fork"]),
        "archived": bool(r.get("archived", False)),
        "is_profile": r["name"] == LOGIN,
    }


def main():
    user = fetch_user()
    repos = fetch_repos()
    events = fetch_events()

    cleaned = [clean_repo(r) for r in repos]
    originals = [r for r in cleaned if not r["fork"]]
    lang_counter = collections.Counter(r["language"] for r in cleaned if r["language"])

    data = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "user": {
            "login": user["login"],
            "name": user.get("name") or user["login"],
            "bio": user.get("bio") or "",
            "company": user.get("company") or "",
            "location": user.get("location") or "",
            "blog": user.get("blog") or "",
            "followers": user["followers"],
            "following": user["following"],
            "public_repos": user["public_repos"],
            "created_at": user["created_at"],
            "joined_year": int(user["created_at"][:4]),
            "avatar_url": user["avatar_url"],
            "html_url": user["html_url"],
        },
        "stats": {
            "total": len(cleaned),
            "original": len(originals),
            "forks": len(cleaned) - len(originals),
            "total_stars": sum(r["stars"] for r in cleaned),
            "total_forks": sum(r["forks"] for r in cleaned),
            "languages": dict(lang_counter.most_common()),
            "top_original": sorted(originals, key=lambda r: -r["stars"])[:6],
        },
        "events": events,
        "repos": cleaned,
    }

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("window.PORTFOLIO_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write(";\n")

    print(f"data.js written: {len(cleaned)} repos, {len(events)} events")
    print("generated_at:", data["generated_at"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
