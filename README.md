# 🎯 Guess The Number Game

A simple number guessing game with a terminal version and a standalone static website.

---

## 🌐 Live Website

- 👉 [Play Guess The Number Online!](https://mohanraj9342.github.io/Guess_The_Number_Game/)

---

## ✨ Features

- Fast, responsive, and accessible UI (keyboard-friendly, focus styles)
- 10 attempts to guess a number between 1 and 100
- Smart hints unlock after 5 attempts (−5 points)
- Live score and attempts left
- Guess history panel
- Works fully offline as a static site

## 🕹️ How to play

1. Enter a number between 1 and 100 and submit your guess.
2. You’ll see feedback: Too low / Too high.
3. After 5 attempts, you can optionally use hints (costs 5 points total).
4. You win when you guess the secret number or lose after 10 attempts.

## 🧮 Scoring & hints

- Base score = attempts left × 10
- If you used hints, subtract 5 points once (not per hint line)
- Minimum score is 0
- Hints provided:
	- Even or odd
	- Range bucket (e.g., 30–40)
	- Divisible by 5/10, or multiples of 3/4/7 (or none)

## Contents

- `Guess_The_Number.py` — Terminal version (play in your console)
- `docs/` — Static site (HTML/CSS/JS)

## Setup

### Terminal Version

```bash
python3 Guess_The_Number.py
```

### Quick start (Static site locally)

Option 1: Just open `docs/index.html` in your browser.

Option 2: Serve locally (for clean routing/cache behavior):

```bash
# From the project root
python3 -m http.server 8000
# Then open http://localhost:8000/docs/
```

### Customize the website

The static site lives in the `docs/` folder. Edit these files to tweak the game:

- `docs/index.html`
- `docs/styles.css`
- `docs/script.js`

## 🛠️ Development

- UI: `docs/index.html` (structure), `docs/styles.css` (styling)
- Game logic: `docs/script.js`
- Terminal game: `Guess_The_Number.py`

Tips:
- Keep logic changes consistent between the terminal and web versions.
- Use your browser devtools (Console) to quickly test changes to `script.js`.

## Project structure

```
Guess_The_Number_Game/
├─ Guess_The_Number.py            # Terminal game
├─ README.md                      # Project documentation
├─ docs/                          # Static website
│  ├─ index.html                  # Game UI markup
│  ├─ styles.css                  # Visual styles
│  └─ script.js                   # Game logic (attempts, score, hints)
```