#!/usr/bin/env python3
"""Regenerate the BibTeX export from papers.yaml."""

from _common import load_papers, save_serializations

if __name__ == "__main__":
    papers = load_papers()
    save_serializations(papers)
    print(f"[BibTeX] entries={len(papers)}")

