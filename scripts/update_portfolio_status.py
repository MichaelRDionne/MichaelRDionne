from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


OWNER = "MichaelRDionne"
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "portfolio-status.md"

ACTIVE_REPOS = [
    "clinical-ai-workflow-sandbox",
    "whatsapp-care-coordination-sandbox",
    "ai-site-build-showcase",
    "medical-ai-consulting-playbook",
    "bootcamp-learning-archive",
    "Cybersecurity-Portfolio",
]

PRIORITY_REPOS = {
    "clinical-ai-workflow-sandbox": "Clinical AI workflow demo",
    "whatsapp-care-coordination-sandbox": "Healthcare operations routing demo",
    "ai-site-build-showcase": "Live AI-assisted site gallery",
    "medical-ai-consulting-playbook": "Consulting guardrails and review templates",
    "bootcamp-learning-archive": "Older coursework index",
    "Cybersecurity-Portfolio": "Cybersecurity background",
}


def github_json(path: str) -> Any:
    token = os.environ.get("GITHUB_TOKEN")
    request = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "MichaelRDionne-portfolio-status",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API failed for {path}: {exc.code} {detail}") from exc


def open_issue_count(repo: str) -> int:
    issues = github_json(f"/repos/{OWNER}/{repo}/issues?state=open&per_page=100")
    return sum(1 for issue in issues if "pull_request" not in issue)


def latest_check_summary(repo: str) -> str:
    runs = github_json(f"/repos/{OWNER}/{repo}/actions/runs?per_page=5")
    workflow_runs = runs.get("workflow_runs", [])
    if not workflow_runs:
        return "no workflow"
    latest = workflow_runs[0]
    status = latest.get("status") or "unknown"
    conclusion = latest.get("conclusion") or "pending"
    return f"{status}/{conclusion}"


def repo_row(repo: str) -> dict[str, str]:
    data = github_json(f"/repos/{OWNER}/{repo}")
    license_info = data.get("license") or {}
    homepage = data.get("homepage") or ""
    return {
        "repo": repo,
        "role": PRIORITY_REPOS[repo],
        "pushed": data.get("pushed_at", "")[:10],
        "issues": str(open_issue_count(repo)),
        "workflow": latest_check_summary(repo),
        "license": license_info.get("spdx_id") or "none",
        "homepage": homepage or "-",
    }


def render(rows: list[dict[str, str]]) -> str:
    lines = [
        "# Portfolio Status",
        "",
        "This file is refreshed by the weekly portfolio maintenance workflow. It summarizes real public repo state and is committed only when the generated status changes.",
        "",
        "## Active Repos",
        "",
        "| Repo | Role | Last Push | Open Issues | Latest Workflow | License | Homepage |",
        "| --- | --- | --- | ---: | --- | --- | --- |",
    ]
    for row in rows:
        repo_link = f"[{row['repo']}](https://github.com/{OWNER}/{row['repo']})"
        homepage = row["homepage"]
        homepage_link = f"[live]({homepage})" if homepage.startswith("https://") else homepage
        lines.append(
            f"| {repo_link} | {row['role']} | {row['pushed']} | {row['issues']} | {row['workflow']} | {row['license']} | {homepage_link} |"
        )

    lines.extend(
        [
            "",
            "## Weekly Maintenance Rules",
            "",
            "- Keep current portfolio repos visible and old course/fork clutter archived.",
            "- Update only real status, roadmap, docs, tests, or demo links.",
            "- Do not create empty commits just to change activity graphs.",
            "- Do not add PHI, real patient examples, production clinical exports, credentials, or private operational details.",
            "- Prefer small branches and pull requests for meaningful changes.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    rows = [repo_row(repo) for repo in ACTIVE_REPOS]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render(rows), encoding="utf-8")
    print(f"Updated {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
