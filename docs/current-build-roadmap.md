# Current Build Roadmap

Near-term public build targets.

## Prompt Eval Harness

- harden the frontier suite so the baseline lands in a discriminating range, then settle the provisional 0.75 gate. The hardened prompt sits one test case from the ceiling: the live series clusters at 0.9615, with one run at 1.0. A suite where one test case separates a good run from a perfect one has little room left to show a regression or an improvement, and this item is the fix for that. Current rows, each with the baseline it ran against, are in `benchmarks/results.jsonl`.
- keep the weekly live eval and dashboard current (automated; watch for drift)

## AI Site Build Showcase

- add more visual examples
- add before/after iteration notes for each case study ([tracked in issue #1](https://github.com/MichaelRDionne/ai-site-build-showcase/issues/1))
- add one richer app-like workflow page

## Medical AI Consulting Playbook

- add more sample case reviews
- package a short executive briefing format

## Shipped since the last revision

- The weekly eval broke and was repaired. A 1.0 release of the model SDK dropped `temperature` from the client signature, and an unpinned install picked it up mid-series, so the job raised a `TypeError` before any request went out. The setting moved to `extra_body` rather than being deleted — every live row in the results series was measured at temperature 0, and dropping it would have kept the job green while silently changing the measurement. The install is now pinned to the major version. The eval has produced a live row every week since, with no further breaks.
- The eval and test workflows moved to Node 24 action versions.
- Five agent skills and a session-handoff command were re-synced from their private originals, and the change-control skill gained a regression-harness gate.
- The captain command retracted its read-only-sandbox claim. A worker dispatched read-only edited three files in the live tree, twice reproduced, so the text now asks for structural containment and treats every dispatch as write-capable. That one was a correctness fix to advice other people are running.
- The site showcase's static gallery is live on GitHub Pages — linked from [portfolio status](portfolio-status.md).
- The consulting playbook's vendor-review template shipped as [`templates/vendor-review.md`](https://github.com/MichaelRDionne/medical-ai-consulting-playbook/blob/main/templates/vendor-review.md), closing the issue that tracked it. It had been sitting in the target list above for a month after the work was done.

## Removed from this roadmap

- The two workflow sandboxes (clinical queue triage, care-coordination routing) went private and are no longer public build targets.

## Portfolio Goal

Ship real increments to the public work. Each roadmap entry should end as inspectable commits in one of the repos above.
