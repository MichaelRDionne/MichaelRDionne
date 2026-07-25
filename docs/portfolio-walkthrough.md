# Portfolio Walkthrough

This is the fastest path through the public portfolio if you are reviewing it for an interview, consulting conversation, or AI workflow role.

## 60-Second Review Path

1. Start with [`prompt-eval-harness`](https://github.com/MichaelRDionne/prompt-eval-harness).
   Evaluation-first prompt development: weighted deterministic rubrics score a prompt's
   output like a regression test, not a vibe check. The demo suite is the argument —
   a mock output that reads better than the faithful one still scores 9% because it
   drops a fact, invents one, and launders a precise figure into vagueness. A live
   weekly CI job scores the current model and publishes the results, untouched, to a
   [public dashboard](https://michaelrdionne.github.io/prompt-eval-harness/).

2. Open [`clinical-agent-skills`](https://github.com/MichaelRDionne/clinical-agent-skills).
   Agent skills and slash commands built from real clinical-automation practice,
   pseudonymized for public reuse. Shows gate-with-incident change control (every hard
   rule paired with the failure that created it), GREEN/YELLOW/RED multi-agent autonomy
   with a no-daemon fence, and a payload-reality check discipline ("mechanics-green
   does not mean content-correct") — the operational judgment layer, not just code.

3. View [`caption-canary`](https://github.com/MichaelRDionne/caption-canary).
   Catches machine transcripts that failed silently: fluent output with the domain
   vocabulary quietly swapped for phonetic soundalikes. It scores a transcript against
   the vocabulary its own topic predicts, so a transcript that "sounds fine" but drifted
   off-topic gets caught without a human re-listening to it. Stdlib only.

4. Read [`tremor-ruler`](https://github.com/MichaelRDionne/tremor-ruler).
   Coin-calibrated hand-tremor quantification from smartphone video — a US quarter in
   frame supplies the pixel-to-mm scale. The interesting part is the QC discipline: every
   gate refuses with a named reason (short clip, tracking dropout, sub-Nyquist frame
   rate, non-rhythmic movement) instead of emitting a number the footage cannot support.

## What Each Repo Proves

- `prompt-eval-harness`: I can turn "does this output look right" into a rubric a machine
  can score consistently, and I keep that score honest by publishing it live and unedited.
- `clinical-agent-skills`: I can design change-control gates for an autonomous system that
  are grounded in a real failure, not a hypothetical one.
- `caption-canary`: I can build a small, dependency-light tool that catches a specific,
  easy-to-miss failure mode instead of a generic quality score.
- `tremor-ruler`: I know the difference between a measurement-grade number and a
  screening-grade one, and I build the tool to refuse rather than blur that line.

## Interview Framing

The public portfolio favors small, runnable tools with public tests over broad claims.
Each repo above ships with unit tests and a CI badge — the demo is not a screenshot, it is
something you can clone and run.

The through-line: practical AI systems for healthcare-adjacent and operational work should
show their evaluation criteria, refuse gracefully when they cannot support a claim, and keep
a human accountable for judgment calls the tool itself should not make.
