from datetime import date
import re

START_DATE = date(2026, 11, 9)
END_DATE = date(2028, 7, 31)
README_PATH = "README.md"


def build_progress_bar(pct: int, length: int = 10) -> str:
    filled = round((pct / 100) * length)
    return f"`{'█' * filled}{'░' * (length - filled)}` {pct}%"


def main() -> None:
    today = date.today()
    total_days = (END_DATE - START_DATE).days
    elapsed_days = (today - START_DATE).days

    pct = max(0, min(100, round((elapsed_days / total_days) * 100)))
    status = "Completato" if pct >= 100 else "In corso"
    bar = build_progress_bar(pct)

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = (
        r"(\|\s*\*\*ITS Sicurezza delle Reti e dei Sistemi\*\*\s*\|\s*[^|]+\|\s*[^|]+\|\s*)"
        r"`[█░]+`\s*\d+%\s*\|\s*[^|]+\|"
    )
    replacement = rf"\g<1>{bar} | {status} |"

    updated_content, count = re.subn(pattern, replacement, content)
    if count == 0:
        raise RuntimeError("Riga ITS non trovata in README.md")

    if updated_content != content:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(updated_content)


if __name__ == "__main__":
    main()