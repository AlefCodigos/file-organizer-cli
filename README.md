# File Organizer CLI

A command-line tool to organize files in a directory into folders based on file type.
It has a dry-run mode and never deletes files.

## Features
- Organize files by type (images, documents, videos, etc.)
- Dry-run mode to simulate the re-organization
- Renames files with identical names for safe file transfer (no deletion, no overwrite)

## Requirements
- Python 3.x
- Pytest

## Usage
On the organizer folder, run:

```bash
python organizer.py -h
```

Example:

```bash
python organizer.py -d ./downloads
```

## Testing
On the tests folder, run:

```bash
pytest
```

This project was developed as a learning exercise to practice Python, testing, and CLI tool design.