# Weekly Portfolio Maintenance

This is the source-of-truth note for the weekly profile updater.

## Purpose

Keep the public portfolio accurate and current without creating fake activity.

The weekly workflow checks the active portfolio repos and regenerates `docs/portfolio-status.md`. It commits only when the generated status file changes.

## Active Portfolio Repos

- `clinical-ai-workflow-sandbox`
- `whatsapp-care-coordination-sandbox`
- `ai-site-build-showcase`
- `medical-ai-consulting-playbook`
- `bootcamp-learning-archive`
- `Cybersecurity-Portfolio`

## Weekly Checklist

- Confirm CI is passing on runnable repos.
- Confirm the live site showcase URL still responds.
- Keep roadmap issues current and close completed ones.
- Keep old course and fork repos archived unless there is a specific reason to feature one.
- Use branches and pull requests for meaningful updates.

## Do Not Do

- Do not create empty commits to make GitHub activity look busy.
- Do not publish PHI, real patient details, production clinical exports, private URLs, tokens, or vendor-sensitive workflow details.
- Do not fork repos publicly unless there is a real learning goal, issue, or small PR plan.

## Good Weekly Update Examples

- Add a case study for a real synthetic demo improvement.
- Close a completed roadmap issue after merging the relevant PR.
- Add tests or expected-output fixtures.
- Update a live demo link after a Pages deployment change.
- Add notes from studying a relevant open-source healthcare or AI workflow project.
