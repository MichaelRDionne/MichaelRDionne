# Michael R Dionne

**PMHNP | Clinical AI workflow automation | Healthcare ops tooling | Human-in-the-loop AI systems**

![PMHNP](https://img.shields.io/badge/PMHNP-0F766E?style=for-the-badge&labelColor=134E4A)
![Clinical AI](https://img.shields.io/badge/Clinical_AI-1D4ED8?style=for-the-badge&labelColor=1E3A8A)
![Healthcare Ops](https://img.shields.io/badge/Healthcare_Ops-9A3412?style=for-the-badge&labelColor=7C2D12)
![Synthetic Data Only](https://img.shields.io/badge/Synthetic_Data_Only-15803D?style=for-the-badge&labelColor=166534)
![Human in the Loop](https://img.shields.io/badge/Human_in_the_Loop-B45309?style=for-the-badge&labelColor=92400E)

I build practical AI-assisted tools for clinical and operational workflows: intake summarization, care-team routing, follow-up tracking, website prototypes, and safety checklists for using AI in healthcare settings.

My work sits at the intersection of psychiatric practice, product thinking, and hands-on automation. The common thread is simple: AI systems should reduce cognitive load, preserve human judgment, and make the next safe action easier to see.

## Snapshot

<a href="https://github.com/anuraghazra/github-readme-stats">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=MichaelRDionne&show_icons=true&hide_border=true&rank_icon=github&title_color=0F766E&icon_color=B45309&text_color=334155&bg_color=00000000" alt="Michael Dionne GitHub stats" />
</a>
<a href="https://github.com/DenverCoder1/github-readme-streak-stats">
  <img height="170" src="https://streak-stats.demolab.com?user=MichaelRDionne&hide_border=true&ring=B45309&fire=B45309&currStreakLabel=0F766E&sideLabels=475569&dates=64748B&currStreakNum=1E293B&sideNums=1E293B&background=FFFFFF00" alt="Michael Dionne GitHub streak" />
</a>

## Contribution Trail

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MichaelRDionne/MichaelRDionne/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MichaelRDionne/MichaelRDionne/output/github-contribution-grid-snake.svg">
  <img alt="GitHub contribution snake animation" src="https://raw.githubusercontent.com/MichaelRDionne/MichaelRDionne/output/github-contribution-grid-snake.svg">
</picture>

## Quick Signal

- Licensed psychiatric clinician building hands-on AI workflow prototypes.
- Comfortable translating messy operational work into structured queues, checks, and review loops.
- Focused on synthetic demos, PHI safety, and responsible human-in-the-loop design.
- Currently building toward medical AI consulting, clinical operations automation, and practical evaluation of AI tools in healthcare environments.

## Stack

[![Core tools](https://skillicons.dev/icons?i=python,ts,html,css,react,git,github,vscode,md&perline=9)](https://skillicons.dev)

## Builder Proof

[![Clinical workflow tests](https://github.com/MichaelRDionne/clinical-ai-workflow-sandbox/actions/workflows/tests.yml/badge.svg)](https://github.com/MichaelRDionne/clinical-ai-workflow-sandbox/actions/workflows/tests.yml)
[![Care coordination tests](https://github.com/MichaelRDionne/whatsapp-care-coordination-sandbox/actions/workflows/tests.yml/badge.svg)](https://github.com/MichaelRDionne/whatsapp-care-coordination-sandbox/actions/workflows/tests.yml)

- Runnable Python demos with public unit tests and GitHub Actions checks.
- Synthetic workflow visuals for clinical AI, care coordination, site builds, and consulting review.
- Public safety boundary: synthetic data only, no PHI, no production clinical exports.
- Fast review path: [`docs/portfolio-walkthrough.md`](docs/portfolio-walkthrough.md)
- Weekly status: [`docs/portfolio-status.md`](docs/portfolio-status.md)
- Learning shortlist: [`docs/repo-learning-shortlist.md`](docs/repo-learning-shortlist.md)

## Visual Showcase

<a href="https://github.com/MichaelRDionne/clinical-ai-workflow-sandbox">
  <img width="31%" src="https://raw.githubusercontent.com/MichaelRDionne/clinical-ai-workflow-sandbox/main/assets/clinical-workflow-demo.svg" alt="Clinical workflow sandbox visual" />
</a>
<a href="https://github.com/MichaelRDionne/whatsapp-care-coordination-sandbox">
  <img width="31%" src="https://raw.githubusercontent.com/MichaelRDionne/whatsapp-care-coordination-sandbox/main/assets/message-triage-board.svg" alt="Care coordination sandbox visual" />
</a>
<a href="https://github.com/MichaelRDionne/medical-ai-consulting-playbook">
  <img width="31%" src="https://raw.githubusercontent.com/MichaelRDionne/medical-ai-consulting-playbook/main/assets/consulting-review-matrix.svg" alt="Medical AI consulting playbook visual" />
</a>

## Current Focus

- Clinical workflow automation with synthetic data and human review gates.
- Healthcare operations tooling for follow-up queues, message triage, and documentation support.
- AI-assisted site and app builds for small teams that need fast, usable prototypes.
- Safety patterns for PHI handling, synthetic demo data, prompt evaluation, and clinical escalation.

## Now Building

- [tremor-ruler](https://github.com/MichaelRDionne/tremor-ruler): video-based tremor measurement with a coin as the physical scale reference — next up is the MediaPipe extraction layer validation and an AIMS-adjacent movement screen.
- Synthetic clinical workflow tools with clearer review gates and better demo polish.
- Care coordination routing patterns that separate operations from clinician review.
- Medical AI consulting artifacts that show decision quality, safety boundaries, and workflow judgment.
- AI-assisted site and app prototypes that feel usable, not just generated.

## Featured Work

- [tremor-ruler](https://github.com/MichaelRDionne/tremor-ruler)  
  Coin-calibrated hand-tremor quantification from smartphone video. MediaPipe landmark trajectories → band-pass → Welch PSD for tremor frequency (the measurement-grade output); a US quarter in frame supplies the pixel-to-mm scale for a screening-grade amplitude. QC gates refuse with a named reason — short clip, tracking dropout, sub-Nyquist frame rate, non-rhythmic movement — instead of emitting a number the footage can't support. Unit-tested against synthetic ground truth, including a 1/f drift-rejection case that caught a real detector bug.

- [prompt-eval-harness](https://github.com/MichaelRDionne/prompt-eval-harness)  
  Evaluation-first prompt development: weighted deterministic rubrics (JSONL cases, pure-function checks, CI gate) that regression-test prompt edits like code edits. The demo is the test suite — a mock output that reads *better* than the faithful one scores 9% because it dropped an allergy, swapped a med, and laundered an alcohol history into vagueness.

- [caption-canary](https://github.com/MichaelRDionne/caption-canary)  
  Detects machine transcripts that failed silently — fluent output with the domain vocabulary quietly replaced by phonetic soundalikes ("close a pin" for clozapine). Scores transcripts against the vocabulary their topic predicts; stdlib only.

- [clinical-ai-workflow-sandbox](https://github.com/MichaelRDionne/clinical-ai-workflow-sandbox)  
  Synthetic clinical workflow demo for intake summaries, longitudinal snapshots, follow-up queues, and safety checks.

- [whatsapp-care-coordination-sandbox](https://github.com/MichaelRDionne/whatsapp-care-coordination-sandbox)  
  Synthetic care-team messaging demo for routing operational messages into human-reviewed action queues.

- [ai-site-build-showcase](https://github.com/MichaelRDionne/ai-site-build-showcase)  
  Case-study gallery of AI-assisted website and app builds, focused on fast iteration and usable interfaces.

- [medical-ai-consulting-playbook](https://github.com/MichaelRDionne/medical-ai-consulting-playbook)  
  Practical checklists for AI workflow risk review, PHI safety, human-in-the-loop design, and model evaluation.

- [bootcamp-learning-archive](https://github.com/MichaelRDionne/bootcamp-learning-archive)  
  Organized index of older FinTech, ML, cybersecurity, and blockchain coursework retained as learning history.

## Interview Talking Points

- I know the clinical workflow from the inside, which helps me spot where AI should support judgment rather than replace it.
- I build small proof-of-concept tools first, then evaluate whether they reduce ambiguity, save time, or create new risk.
- I treat synthetic data, auditability, and escalation rules as product requirements, not afterthoughts.
- I am especially interested in AI systems for healthcare operations, clinician productivity, and candidate/workflow evaluation.

## Safety Boundary

Public repositories use synthetic or generalized examples only. I do not publish patient data, private clinical records, production credentials, private operational exports, or vendor-specific internal workflows.

## What I Like Building

- Small tools that turn messy work into clear queues.
- Clinical-facing summaries that show uncertainty instead of hiding it.
- AI workflows that keep final responsibility with a human reviewer.
- Lightweight prototypes that prove an idea before a team overbuilds it.

## Trophy Shelf

[![trophy](https://github-profile-trophy.vercel.app/?username=MichaelRDionne&theme=flat&no-frame=true&margin-w=12&row=1&column=6)](https://github.com/ryo-ma/github-profile-trophy)

## Current Build Roadmap

See `docs/current-build-roadmap.md` for the next set of public upgrades I am actively building across the portfolio.

See `docs/weekly-portfolio-maintenance.md` for the automated weekly maintenance rules.

## Recent Public Builds & Thinking

- [Medical AI Consulting Playbook](https://github.com/MichaelRDionne/medical-ai-consulting-playbook) — checklists, templates, and real sanitized examples of tools I've built:
  - Full clinic-day EHR automation suite: kickoff from pasted schedule, post-visit handoff with content-validity, new-patient intake, backfill, token-efficient rewrites.
  - "Magic paste" utility (pasted-text.ts) for intelligently detecting and handling long pasted content (schedules, notes) as separate blocks in command UIs.

These show the engineering: safety gates for PHI/encrypted volumes, human review at every irreversible step, v2 structured charts as source of truth, and UI affordances that make daily work faster while keeping the clinician in control.

All examples use synthetic or generalized data. Full internal versions stay private.

## One Clinician-Builder Confession

I used to think "if the model is good enough, the workflow will just work." 

Then I watched a perfectly generated summary get ignored because the clinician couldn't find the safety flag in 8 seconds flat.

So now I build the boring parts: the queue that won't let you forget the AIMS, the paste handler that knows when a schedule is too long to inline, the checklist that forces you to look at the actual drive mount before you touch PHI.

It's not sexy. It ships.

(And yes, the snake graph is my favorite part of this whole README. Fight me.)

