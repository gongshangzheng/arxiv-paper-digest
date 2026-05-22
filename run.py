#!/usr/bin/env python3
from __future__ import annotations
import argparse, sys
from pathlib import Path
project_root=Path(__file__).parent; sys.path.insert(0,str(project_root))
from src.cli import main
RULE_FILES=["rules/arxiv_rss.yaml","rules/arxiv_cv_rss.yaml"]
def parse_args():
    p=argparse.ArgumentParser(description="arxiv-paper-digest"); g=p.add_mutually_exclusive_group(); g.add_argument("-c","--continuous",action="store_true",help="持续运行模式"); g.add_argument("--once",action="store_true",help="只运行一次并生成 html-blog 简报"); p.add_argument("-r","--repair",action="store_true",help="持续运行前先补跑一次"); return p.parse_args()
if __name__=="__main__":
    a=parse_args(); main(continuous=a.continuous and not a.once,repair=a.repair,rule_files=RULE_FILES)
