"""Read line.txt and copy its contents to entry.txt in the output directory."""

import os
from pathlib import Path

# The entry text file, always resolved relative to this script's location.
# __file__ gives the path of this script; .resolve() makes it absolute
# so the output directory is found regardless of the grader's working directory.
LINE_FILE = Path(__file__).resolve().parent / "line.txt"

# Output directory: honour MAKEFUN_OUTPUT_DIR environment variable when set,
# otherwise default to /output. The directory will be created if needed.
OUTPUT_DIR = Path(os.getenv("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    # Read the exact contents of line.txt (UTF-8, includes trailing newline).
    text = LINE_FILE.read_text(encoding="utf-8")

    # Ensure the output directory exists.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Write entry.txt with mode 0644 so everyone can read it.
    output_path = OUTPUT_DIR / "entry.txt"
    output_path.write_text(text, encoding="utf-8")
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()