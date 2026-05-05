"""
Mini-project: Small CLI Todo app (JSON storage)

Usage:
  python 14_cli_todo.py
Commands: add, list, done <n>, quit
"""
import json
from pathlib import Path

STORE = Path(__file__).with_name("todos.json")


def load():
    if not STORE.exists():
        return []
    return json.loads(STORE.read_text())


def save(todos):
    STORE.write_text(json.dumps(todos, indent=2))


def main():
    todos = load()
    while True:
        cmd = input("(add/list/done/quit) > ").strip().split()
        if not cmd:
            continue
        if cmd[0] == "add":
            text = input("Task: ").strip()
            todos.append({"task": text, "done": False})
            save(todos)
        elif cmd[0] == "list":
            for i, t in enumerate(todos, 1):
                status = "x" if t.get("done") else " "
                print(f"{i}. [{status}] {t['task']}")
        elif cmd[0] == "done" and len(cmd) > 1 and cmd[1].isdigit():
            idx = int(cmd[1]) - 1
            if 0 <= idx < len(todos):
                todos[idx]["done"] = True
                save(todos)
        elif cmd[0] in ("q", "quit", "exit"):
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
