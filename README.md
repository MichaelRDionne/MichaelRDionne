# Michael R Dionne

**Board-Certified Psychiatric Nurse Practitioner | Clinical AI workflow automation | Healthcare ops tooling | Human-in-the-loop AI systems**

![Board-Certified Psychiatric NP](https://img.shields.io/badge/BOARD--CERTIFIED_PSYCHIATRIC_NP-0F766E?style=for-the-badge&labelColor=134E4A)
![Clinical AI](https://img.shields.io/badge/Clinical_AI-1D4ED8?style=for-the-badge&labelColor=1E3A8A)
![Healthcare Ops](https://img.shields.io/badge/Healthcare_Ops-9A3412?style=for-the-badge&labelColor=7C2D12)
![Synthetic Data Only](https://img.shields.io/badge/Synthetic_Data_Only-15803D?style=for-the-badge&labelColor=166534)
![Human in the Loop](https://img.shields.io/badge/Human_in_the_Loop-B45309?style=for-the-badge&labelColor=92400E)

I'm a psychiatric nurse practitioner who writes code. By day I see patients. The rest of the time I build the tools I wish my workday came with: a script that proves every record in an archive was actually read, a canary that catches an AI transcript quietly swapping "clozapine" for "close a pin," a test harness that scores prompt edits the way a test suite scores code edits.

The thread through all of it is simple. AI should carry the busywork, and the human keeps the final call. Most of what I publish here is about making that rule enforceable instead of aspirational.

Every README in this portfolio opens in plain language and gets more technical as you scroll.

## Start here

Four repos carry most of the signal:

- **[prompt-eval-harness](https://github.com/MichaelRDionne/prompt-eval-harness)** — tests for prompts. Edit a prompt and a fixed set of checks tells you whether the output got worse, before anyone has to eyeball a diff. In the demo, an AI answer that *reads better* than the correct one scores 9%, because it dropped an error code, invented a cause, and blurred the one number that mattered. A weekly job scores a live model and publishes the results, untouched, to a [public dashboard](https://michaelrdionne.github.io/prompt-eval-harness/).

- **[tremor-ruler](https://github.com/MichaelRDionne/tremor-ruler)** — measures hand tremor from a smartphone video. A US quarter in the frame is the ruler that converts pixels to millimeters. It reports tremor frequency in Hz, and when the footage can't support a number — clip too short, tracking dropped out, movement not rhythmic — it refuses and names the reason instead of guessing.

- **[clinical-agent-skills](https://github.com/MichaelRDionne/clinical-agent-skills)** — the rulebook I run AI agents under in my own clinical practice, pseudonymized for public reuse. Every hard rule ships with the real incident that created it. MIT — fork and adapt.

- **[clinical-note-eval](https://github.com/MichaelRDionne/clinical-note-eval)** — clinician-authored gold labels plus a [written preference-pair page](https://github.com/MichaelRDionne/clinical-note-eval/blob/master/reviewer/preference-pairs.md): two answers, one chosen, severity-first why. Ten synthetic notes. No live scores until you run it.

## Selected writing

**[When Not to Use a Model](when-not-to-use-a-model.md)** — Most writing about AI in healthcare argues over which model to reach for. The judgment that has paid off most for me is knowing when to take the model out of a step entirely. Three cases from my own workflow where I replaced an LLM with a deterministic local script — [records intake](https://github.com/MichaelRDionne/intake-manifest), batch registration, and the silent-transcript problem behind [caption-canary](https://github.com/MichaelRDionne/caption-canary) — with an honest account of what that cost, where it was the wrong call, and where the model stayed. The decision rule: prompts express intent, scripts express contracts.

## Proof it runs

[![prompt-eval-harness tests](https://github.com/MichaelRDionne/prompt-eval-harness/actions/workflows/tests.yml/badge.svg)](https://github.com/MichaelRDionne/prompt-eval-harness/actions/workflows/tests.yml)
[![caption-canary tests](https://github.com/MichaelRDionne/caption-canary/actions/workflows/tests.yml/badge.svg)](https://github.com/MichaelRDionne/caption-canary/actions/workflows/tests.yml)
[![tremor-ruler tests](https://github.com/MichaelRDionne/tremor-ruler/actions/workflows/tests.yml/badge.svg)](https://github.com/MichaelRDionne/tremor-ruler/actions/workflows/tests.yml)

- Runnable Python demos with public unit tests and GitHub Actions checks.
- A [weekly automated eval with a public results dashboard](https://michaelrdionne.github.io/prompt-eval-harness/), a static-site build, and consulting-review visuals.
- Public safety boundary: synthetic data only, no PHI, no production clinical exports.
- Fast review path: [`docs/portfolio-walkthrough.md`](docs/portfolio-walkthrough.md) · Status: [`docs/portfolio-status.md`](docs/portfolio-status.md) · Learning shortlist: [`docs/repo-learning-shortlist.md`](docs/repo-learning-shortlist.md)

## Visual showcase

<a href="https://github.com/MichaelRDionne/prompt-eval-harness">
  <img width="31%" src="https://raw.githubusercontent.com/MichaelRDionne/prompt-eval-harness/HEAD/assets/demo.gif" alt="Prompt eval harness demo" />
</a>
<a href="https://github.com/MichaelRDionne/ai-site-build-showcase">
  <img width="31%" src="https://raw.githubusercontent.com/MichaelRDionne/ai-site-build-showcase/HEAD/assets/site-build-dashboard-preview.svg" alt="Static-site build dashboard preview" />
</a>
<a href="https://github.com/MichaelRDionne/medical-ai-consulting-playbook">
  <img width="31%" src="https://raw.githubusercontent.com/MichaelRDionne/medical-ai-consulting-playbook/main/assets/consulting-review-matrix.svg" alt="Medical AI consulting playbook visual" />
</a>

## The rest of the shelf

- **[claude-commands](https://github.com/MichaelRDionne/claude-commands)** — seven general-purpose Claude Code slash commands, the domain-neutral layer to clinical-agent-skills. Captain-mode delegation: the root stays mechanical on whatever model the session is on, and a judge subagent writes the plan and the verdict. Lacuna prompting, which hunts for the structurally missing option instead of asking a model to "be creative." Lean-by-default effort control that spikes when the task gets hard and comes back down after. Pre-flight red-teaming. Authenticated-session relay prompts for work that has to happen inside a real logged-in browser. Report-first workspace housekeeping. No-execution quarantine vetting of untrusted repos. MIT — copy the files you want.

- **[caption-canary](https://github.com/MichaelRDionne/caption-canary)** — detects machine transcripts that failed silently: fluent output with the domain vocabulary quietly replaced by phonetic soundalikes ("close a pin" for clozapine). Scores a transcript against the vocabulary its topic predicts. Standard library only.

- **[intake-manifest](https://github.com/MichaelRDionne/intake-manifest)** — prove every file in an archive was accounted for, or fail loudly. One explicit status per file — processed, flagged, or failed — and a tripwire that refuses any manifest whose record count doesn't match the archive. `--strict` turns a silent gap into a non-zero exit. The deterministic-intake case from *When Not to Use a Model*.

- **[ai-site-build-showcase](https://github.com/MichaelRDionne/ai-site-build-showcase)** — case-study gallery of AI-assisted website and app builds, including two live shipped sites (deliberately unnamed) and a synthetic operations dashboard.

- **[medical-ai-consulting-playbook](https://github.com/MichaelRDionne/medical-ai-consulting-playbook)** — checklists and templates for deciding whether an AI workflow belongs in a clinic at all: PHI safety, human-review design, model evaluation, and sanitized examples of the clinic-day automation suite I run in my own practice.

## Now building

- [tremor-ruler](https://github.com/MichaelRDionne/tremor-ruler): the MediaPipe landmark-extraction layer is validated end-to-end on real video; next up is an AIMS-adjacent movement screen.
- Synthetic clinical workflow tools with clearer review gates and better demo polish.
- Care coordination routing patterns that separate operations from clinician review.
- Medical AI consulting artifacts that show decision quality, safety boundaries, and workflow judgment.

Roadmap detail: [`docs/current-build-roadmap.md`](docs/current-build-roadmap.md) · automated weekly maintenance rules: [`docs/weekly-portfolio-maintenance.md`](docs/weekly-portfolio-maintenance.md)

## How I work

- I know the clinical workflow from the inside, which helps me spot where AI should support judgment rather than replace it.
- I build small proof-of-concept tools first, then evaluate whether they reduce ambiguity, save time, or create new risk.
- I treat synthetic data, auditability, and escalation rules as product requirements, not afterthoughts.
- I like small tools that turn messy work into clear queues, summaries that show their uncertainty, and lightweight prototypes that prove an idea before a team overbuilds it.
- I am especially interested in AI systems for healthcare operations, clinician productivity, and workflow evaluation.

## Safety boundary

Public repositories use synthetic or generalized examples only. I do not publish patient data, private clinical records, production credentials, private operational exports, or vendor-specific internal workflows. Full internal versions of the clinical tooling stay private.
