"""
Mini-project: Simple Notes App (File I/O)

Usage:
  - Run and follow prompts to add/list notes.
  - Notes are stored in `notes.json` in the same folder.
"""
import json
from pathlib import Path

NOTES_FILE = Path(__file__).with_name("notes.json")


def load_notes():
    if not NOTES_FILE.exists():
        return []
    return json.loads(NOTES_FILE.read_text())


def save_notes(notes):
    NOTES_FILE.write_text(json.dumps(notes, indent=2))


def add_note():
    notes = load_notes()
    title = input("Title: ").strip()
    body = input("Body: ").strip()
    notes.append({"title": title, "body": body})
    save_notes(notes)
    print("Saved.")


def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes yet.")
        return
    for i, n in enumerate(notes, 1):
        print(f"{i}. {n['title']} - {n['body']}")


def main():
    while True:
        cmd = input("(add/list/quit) > ").strip().lower()
        if cmd == "add":
            add_note()
        elif cmd == "list":
            list_notes()
        elif cmd in ("q", "quit", "exit"):
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
