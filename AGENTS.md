# Repository Guidelines & Agent Constraints

This repository hosts a public GitHub Profile `README.md` (written in Italian) and an automated Python script executed via GitHub Actions to update academic progress.

## 1. Security & OpSec Rules (CRITICAL)
This is a **public** repository. When editing `README.md` or any other file:
- **NEVER** include real internal IPv4/IPv6 addresses, custom ports, custom DNS-over-HTTPS/TLS query paths, hostnames, or internal domain names.
- **NEVER** enumerate specific containers running inside the isolated VPN LXC stack (keep it abstracted as "Isolated VPN Stack").
- Keep infrastructure descriptions architectural and high-level.

## 2. Automation Contract (`scripts/update_progress.py`)
`scripts/update_progress.py` updates `README.md` every Monday via regex matching.
- **DO NOT** alter the title string `**ITS Sicurezza delle Reti e dei Sistemi**` or the column structure of its row in the `Formazione` table.
- The progress cell **MUST** keep the exact format `` `██████████` XX% `` (10 block characters using `█` and `░`).
- Whenever you modify `README.md` or `scripts/update_progress.py`, run `python3 scripts/update_progress.py` locally to verify the regex still matches without raising `RuntimeError`.

## 3. Content & Formatting Conventions
- **Language:** Italian for prose, headings, and table descriptions; keep standard networking/sysadmin terminology in English (e.g., *Prefix Delegation*, *Dual-Stack*, *Reverse Proxy*).
- **Badges:** All technology badges in `Stack Tecnologico` must use `https://img.shields.io/badge/...` with `?style=flat-square` and SimpleIcons logos.
- **Tables:** Ensure no blank lines break Markdown tables.

## 4. Git Workflow
- Keep commits atomic and use Conventional Commits (`docs:`, `feat:`, `fix:`, `chore:`).
- Do not modify `.github/workflows/update-readme.yml` permissions (`contents: write`) unless explicitly requested.

## 5. Language
- Keep the final output language the "Italian" language.
- Write in english only the tecnical name.

## 6. Ask
- If you do not have enough information to take action, ask the user for clarification.
- If you are a small-scale model (under 20 billion parameters), first outline the work to be done and then ask for confirmation.