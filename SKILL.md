---
name: arxiv-paper-digest
description: 每日 arXiv 论文追踪。Python-only pipeline：抓取 cs.AI + cs.CV，按 diffusion / autoregressive / image_compression / visual_tokenizer_1d / diffusion_visual_encoder 分类，写入 gongshangzheng.github.io/data/daily-papers，并生成 html-blog 文章到 gongshangzheng.github.io/src/pages/arxiv-digest-YYYY-MM-DD.html。
---

# arxiv-paper-digest

本 skill 是 `~/.hanako/skills` 下的独立 submodule。代码已经扁平化，爬虫直接位于本目录，不再使用嵌套爬虫目录。

## Python 环境

必须使用本 skill 自带虚拟环境：

```bash
~/.hanako/skills/arxiv-paper-digest/.venv/bin/python
```

不要使用系统 `python`。

## 运行入口

```bash
cd ~/.hanako/skills/arxiv-paper-digest
.venv/bin/python run.py --once
```

持续运行：

```bash
.venv/bin/python run.py --continuous
```

launchd 应直接调用：

```text
~/.hanako/skills/arxiv-paper-digest/.venv/bin/python
~/.hanako/skills/arxiv-paper-digest/run.py --once
```


## 直接关键词搜索

可以直接在本 skill 里调用 arXiv 关键词检索。原独立 arXiv 查询能力已合并到这里。

### Python API

```python
from src.arxiv_search import Query, Taxonomy, build_query, search_by_keywords

q = build_query(
    ["diffusion", "autoregressive"],
    field="title",
    categories=Taxonomy.cs,
    since="20250520",
)
results = search_by_keywords("visual tokenizer", field="abstract", max_results=20)
```

### 支持能力

- `Query.title / abstract / author / category / all`
- `Query.submitted_date(start, end)`
- `&` / `|` / `~` 组合布尔查询
- `search_by_keywords(...)` 直接执行搜索
- `Taxonomy.cs / stat / eess / math / physics / econ`

## Pipeline

1. `src/cli.py`：命令行入口
2. `src/crawler_pipeline.py`：流程编排
3. `src/rule_runtime.py`：规则运行时构建
4. `src/crawl_output_writer.py`：分类 raw JSON 写入
5. `src/html_blog_digest.py`：生成 html-blog 页面

## 输出

- Raw 数据：`~/gongshangzheng.github.io/data/daily-papers/<category>/YYYY-MM-DD.json`
- HTML-blog 源文：`~/gongshangzheng.github.io/src/pages/arxiv-digest-YYYY-MM-DD.html`

## 测试

```bash
cd ~/.hanako/skills/arxiv-paper-digest
.venv/bin/python -m unittest discover -s tests -v
```
