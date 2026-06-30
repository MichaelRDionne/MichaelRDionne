# Repo Learning Shortlist

These are high-value repositories to study or fork selectively. The rule is simple: star and study first; fork only when there is a specific small contribution, local experiment, or portfolio-adjacent learning goal.

## Best Fits

1. `synthetichealth/synthea`
   Synthetic patient population simulator. Best for learning realistic synthetic healthcare data generation and FHIR-style export patterns.

2. `medplum/medplum`
   TypeScript healthcare platform built around FHIR, app development, and compliant workflows. Best for understanding modern healthcare developer platforms.

3. `smart-on-fhir/client-js`
   JavaScript client for SMART on FHIR. Best for learning the app-launch and authorization side of healthcare integrations.

4. `medspacy/medspacy`
   Clinical NLP library built on spaCy. Best for learning how clinical text processing pipelines are structured.

5. `HumanSignal/label-studio`
   Human-in-the-loop data labeling and annotation tool. Best for learning review queues, labeling workflows, and human judgment surfaces.

6. `promptfoo/promptfoo`
   LLM evaluation, prompt testing, and red-team tooling. Best for adding eval discipline to the clinical AI sandbox repos.

7. `langfuse/langfuse`
   LLM observability, prompt management, traces, and evaluation. Best for understanding how AI workflow quality is monitored over time.

8. `guardrails-ai/guardrails`
   LLM output validation and structured guardrails. Best for learning validation patterns around generated summaries and routing outputs.

9. `streamlit/streamlit`
   Fast Python data app framework. Best for building local queue dashboards and demo surfaces quickly.

10. `openai/openai-cookbook`
    Practical OpenAI API examples and implementation patterns. Best for learning reference-grade examples before building new AI demo features.

## Forking Rules

- Fork only one or two at a time.
- Prefer docs fixes, small examples, or local adapters over big feature attempts.
- Keep public forks archived unless actively contributing.
- Do not run any of these tools against real clinical data in public or non-BAA contexts.

## First Learning Targets

- Study `synthetichealth/synthea` and add a note on how synthetic patient fixtures could improve `clinical-ai-workflow-sandbox`.
- Study `promptfoo/promptfoo` and design one expected-output evaluation for summary quality.
- Study `streamlit/streamlit` and sketch a local follow-up queue view.
