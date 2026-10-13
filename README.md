# COMPAKT Service

Modernisierte Website mit Leistungsseiten, regionalen Informationen und Blogarchiv.

## Build

Python 3.12, `pip install -r requirements.txt`, `python build.py`, `python verify.py`.

`dist/` enthält die fertige Website für Hetzner. Die primäre Domain ist https://www.compakt-service.de/.

## Deployment

GitHub Actions veröffentlicht bei Push auf `main` ausschließlich den Inhalt von `dist/` per SFTP. Vorhandene Dateien werden nicht gelöscht. Erforderliche Repository-Secrets: `HETZNER_HOST`, `HETZNER_USER`, `HETZNER_PASSWORD`, `HETZNER_TARGET_DIR`. Optional: `HETZNER_PORT` (Standard 22).

Das Zielverzeichnis muss explizit gesetzt sein. Das Kontaktformular bereitet eine E-Mail im E-Mail-Programm vor; es versendet nicht serverseitig.
