# prompt-injection-ci

Prompt-injection attack tests that run on every pull request.

- `app.py` — a summarizer with a guarded prompt (the thing under test)
- `attacks.yaml` — attack documents; add a case = add a test
- `.github/workflows/injection-tests.yml` — runs `pytest` on each PR

Run locally: `export ANTHROPIC_API_KEY=...; pip install -r requirements.txt; pytest -v`

Demo: weaken the prompt in a PR (delete the "untrusted DATA" line) and watch CI go red.

Sources: [OWASP LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) · [GitHub Actions docs](https://docs.github.com/en/actions)
