# COMPAKT Service

Modernisierte Website mit Leistungsseiten, regionalen Informationen und Blogarchiv.

## Build

Python 3.12, `pip install -r requirements.txt`, `python build.py`, `python verify.py`.

`dist/` enthält die fertige Website für Hetzner. Die primäre Domain ist https://www.compakt-service.de/.

## Deployment

GitHub Actions veröffentlicht bei Push auf `main` ausschließlich den Inhalt von `dist/` per SFTP. Vorhandene Dateien werden nicht gelöscht. Erforderliche Repository-Secrets: `HETZNER_HOST`, `HETZNER_USER`, `HETZNER_PASSWORD`. Optional: `HETZNER_PORT` (Standard 22).

Der Hetzner-SFTP-Zugang ist für Compakt eingerichtet. Die Website wird direkt in das Startverzeichnis dieses Zugangs hochgeladen, ohne weiteren Unterordner. Ein Zielverzeichnis-Secret ist nicht erforderlich. Nach dem Upload wird die Startseite zurückgelesen und mit der lokalen Datei verglichen. Das Kontaktformular bereitet eine E-Mail im E-Mail-Programm vor; es versendet nicht serverseitig.
