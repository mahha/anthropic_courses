#!/usr/bin/env python3
"""
Translate article*.txt files to Japanese and write *_JP.txt next to them.

- Preserves blank lines.
- Translates paragraph-by-paragraph to avoid upstream length limits.
- Uses Google Translate via deep-translator (network required).
"""

from __future__ import annotations

import argparse
import pathlib
import time
from typing import Iterable, List


def split_preserve_blank_lines(text: str) -> List[str]:
    """Split into blocks where each block is either '\n' (blank line) or a paragraph."""
    lines = text.splitlines(keepends=True)
    blocks: List[str] = []
    buf: List[str] = []

    def flush_buf():
        nonlocal buf
        if buf:
            blocks.append("".join(buf))
            buf = []

    for line in lines:
        if line.strip() == "":
            flush_buf()
            # preserve blank line as its own block
            blocks.append(line)
        else:
            buf.append(line)
    flush_buf()
    return blocks


def chunk_text(text: str, max_chars: int = 4500) -> List[str]:
    """Chunk a long paragraph into <= max_chars pieces, trying to split on sentences."""
    if len(text) <= max_chars:
        return [text]

    chunks: List[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        if end < len(text):
            # try to backtrack to a sentence boundary
            backtrack = max(text.rfind(". ", start, end), text.rfind("。\n", start, end), text.rfind("。", start, end))
            if backtrack > start + 200:
                end = backtrack + 1
        chunks.append(text[start:end])
        start = end
    return chunks


def translate_blocks(blocks: Iterable[str], translator) -> str:
    out_parts: List[str] = []
    for b in blocks:
        if b.strip() == "":
            out_parts.append(b)
            continue

        # Preserve trailing newline behavior from original paragraph block
        ends_with_nl = b.endswith("\n")
        paragraph = b.rstrip("\n")

        translated_chunks: List[str] = []
        for chunk in chunk_text(paragraph):
            translated_chunks.append(translator.translate(chunk))
            # be gentle to upstream
            time.sleep(0.1)

        translated = "".join(translated_chunks)
        if ends_with_nl:
            translated += "\n"
        out_parts.append(translated)

    return "".join(out_parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="Directory containing article*.txt")
    ap.add_argument("--start", type=int, default=2)
    ap.add_argument("--end", type=int, default=8)
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    from deep_translator import GoogleTranslator

    base = pathlib.Path(args.dir)
    translator = GoogleTranslator(source="en", target="ja")

    for i in range(args.start, args.end + 1):
        src = base / f"article{i}.txt"
        dst = base / f"article{i}_JP.txt"
        if not src.exists():
            raise FileNotFoundError(str(src))
        if dst.exists() and not args.overwrite:
            print(f"skip (exists): {dst}")
            continue

        print(f"translating: {src.name} -> {dst.name}")
        text = src.read_text(encoding="utf-8")
        blocks = split_preserve_blank_lines(text)
        ja = translate_blocks(blocks, translator)
        dst.write_text(ja, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


