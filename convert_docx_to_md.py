import argparse
import os
import re
import mammoth

LESSON_HEADING_RE = re.compile(r"^#{1,6}\s*(lesson\s*\d*|lesson\b|Lesson\s*\d*|Lesson\b)", re.IGNORECASE)


def convert_docx_to_markdown(docx_path: str) -> str:
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_markdown(docx_file)
        return result.value


def split_lessons(markdown_text: str) -> list[str]:
    lines = markdown_text.splitlines()
    sections = []
    current_section = []

    def flush_current():
        if current_section:
            sections.append("\n".join(current_section).strip() + "\n")

    for line in lines:
        if LESSON_HEADING_RE.match(line):
            flush_current()
            current_section = [line]
        else:
            current_section.append(line)

    flush_current()
    if not sections:
        return [markdown_text.strip() + "\n"]
    return sections


def write_lessons(sections: list[str], output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    for index, section in enumerate(sections, start=1):
        filename = os.path.join(output_dir, f"note{index}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(section)
        print(f"Wrote {filename}")


def find_next_note_name(output_dir: str) -> str:
    existing = [f for f in os.listdir(output_dir) if f.lower().startswith("note") and f.lower().endswith(".md")]
    if not existing:
        return "note1.md"
    return "note1.md"


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a DOCX file into lesson markdown files named note1.md, note2.md, ...")
    parser.add_argument("docx_file", nargs="?", default="101笔记.docx", help="Path to the DOCX file")
    parser.add_argument("--output-dir", default=".", help="Directory where note files will be written")
    args = parser.parse_args()

    if not os.path.isfile(args.docx_file):
        raise FileNotFoundError(f"DOCX file not found: {args.docx_file}")

    markdown = convert_docx_to_markdown(args.docx_file)
    sections = split_lessons(markdown)
    if not sections:
        raise RuntimeError("No lesson sections found in the document.")

    write_lessons(sections, args.output_dir)
    print(f"Converted {len(sections)} lesson(s) from {args.docx_file}.")


if __name__ == "__main__":
    main()
