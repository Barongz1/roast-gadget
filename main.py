"""One-Line Roast: The Gadget You Use Every Day — entry for make.fun.

Writes one line to /output/entry.txt.
The line roasts a gadget or app used every day, at most 200 characters.
"""
import os

LINE = "My phone dies at 4 PM every day, which is its way of telling me to touch grass and stop scrolling."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
