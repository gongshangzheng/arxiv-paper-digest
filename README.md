# arxiv-paper-digest

Python-only daily arXiv digest pipeline. This repository is a flat Hanako skill submodule; there is no nested crawler project.

```bash
cd ~/.hanako/skills/arxiv-paper-digest
.venv/bin/python run.py --once
```

Outputs:

- `~/gongshangzheng.github.io/data/daily-papers/<category>/YYYY-MM-DD.json`
- `~/gongshangzheng.github.io/src/pages/arxiv-digest-YYYY-MM-DD.html`
