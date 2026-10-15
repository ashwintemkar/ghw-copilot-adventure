"""
Choose-your-own-adventure CLI game.
Built for the GHW challenge: Use GitHub Copilot to Build a Simple Application.
Run: python adventure.py
"""

from __future__ import annotations

SCENES = {
    "start": {
        "text": (
            "You wake up in the MLH Discord lobby. A glowing terminal "
            "offers three doors labeled CURSOR, TIGER, and GROK."
        ),
        "choices": {
            "1": ("Enter the Cursor door", "cursor"),
            "2": ("Enter the Tiger door", "tiger"),
            "3": ("Enter the Grok door", "grok"),
        },
    },
    "cursor": {
        "text": (
            "Inside Cursor HQ, an agent asks you to ship a tip calculator "
            "before the closing ceremony. Do you accept?"
        ),
        "choices": {
            "1": ("Accept and ship it", "win_cursor"),
            "2": ("Ask for one more feature first", "cursor_extra"),
            "3": ("Go back to the lobby", "start"),
        },
    },
    "cursor_extra": {
        "text": "You add dark mode. The agent high-fives you in the sidebar.",
        "choices": {"1": ("Submit the challenge", "win_cursor")},
    },
    "tiger": {
        "text": (
            "Tiger Cloud Console boots up. A hypertable waits for sensor data. "
            "What do you do first?"
        ),
        "choices": {
            "1": ("Insert IoT samples", "win_tiger"),
            "2": ("Create a continuous aggregate", "win_tiger"),
            "3": ("Go back", "start"),
        },
    },
    "grok": {
        "text": (
            "Grok Bot appears with a Teach Task button. Campus events scroll by."
        ),
        "choices": {
            "1": ("Teach a weather routine", "win_grok"),
            "2": ("Build a campus opportunities table", "win_grok"),
            "3": ("Go back", "start"),
        },
    },
    "win_cursor": {
        "text": "Challenge complete: Mini App with Cursor. Points inbound!",
        "choices": {},
    },
    "win_tiger": {
        "text": "Challenge complete: Tiger Cloud pipeline humming. Points inbound!",
        "choices": {},
    },
    "win_grok": {
        "text": "Challenge complete: Grok Bot skill saved. Points inbound!",
        "choices": {},
    },
}


def play() -> None:
    scene_id = "start"
    print("\n=== Campus Relay Adventure ===\n")
    while True:
        scene = SCENES[scene_id]
        print(scene["text"])
        if not scene["choices"]:
            print("\nThanks for playing.\n")
            break
        print()
        for key, (label, _) in scene["choices"].items():
            print(f"  [{key}] {label}")
        choice = input("\nYour choice: ").strip()
        if choice not in scene["choices"]:
            print("Pick a listed number.\n")
            continue
        scene_id = scene["choices"][choice][1]
        print()


if __name__ == "__main__":
    play()
