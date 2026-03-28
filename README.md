# ⚽ Football KBC — Kaun Banega Crorepati

A fully playable **Football Quiz Game** inspired by Kaun Banega Crorepati, built in Python with a web version hosted on GitHub Pages.

> Answer 15 football questions correctly to win ₹1,00,00,000!

---

## 🌐 Play Online

👉 **[Play the Web Version](https://yourusername.github.io/kbc-game/)**

---

## 🎮 Features

- 15 football questions across Easy, Medium & Hard difficulty
- 3 lifelines — 50/50, Audience Poll, Phone a Friend
- Safe havens at Q5 (₹10,000) and Q10 (₹3,20,000)
- Prize ladder tracking your progress
- Leaderboard — top 10 scores saved locally
- Quit anytime and walk away with your winnings
- Fully playable in browser (no install needed)
- Terminal version with animated intro & dramatic effects

---

## 🖥️ Terminal Version — How to Run

### 1. Clone the repository
```bash
git clone https://github.com/InsightAdi/Football-KBC-game.git
cd kbc-game
```

### 2. Run the game
```bash
python main.py
```

> No external dependencies required. Uses Python standard library only.

---

## 📁 Project Structure

```
kbc-game/
│
├── main.py              # Entry point — main menu
├── game.py              # Core game logic & KBCGame class
├── questions.py         # Load & filter questions from JSON
├── lifelines.py         # 50-50, Audience Poll, Phone a Friend
├── leaderboard.py       # Save & display top 10 scores
├── utils.py             # Timer, formatting, input validation
│
├── data/
│   └── questions.json   # Football question bank (15 questions)
│
├── tests/
│   └── test_game.py     # 30 unit tests across all modules
│
├── index.html           # Web version (playable in browser)
└── README.md            # You are here
```

---

## 🧠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Data Storage | JSON |
| Web Frontend | HTML, CSS, Vanilla JS |
| Testing | Python `unittest` |
| Hosting | GitHub Pages |

---

## 🎯 Lifelines

| Lifeline | How it works |
|---|---|
| ✂️ **50 / 50** | Removes 2 wrong options — 2 remain |
| 👥 **Audience Poll** | Shows percentage votes for each option |
| 📞 **Phone a Friend** | A football expert friend gives you a hint |

---

## 🔒 Prize Ladder

| Question | Prize | Note |
|---|---|---|
| Q1 | ₹1,000 | |
| Q2 | ₹2,000 | |
| Q3 | ₹3,000 | |
| Q4 | ₹5,000 | |
| Q5 | ₹10,000 | 🔒 Safe Haven |
| Q6 | ₹20,000 | |
| Q7 | ₹40,000 | |
| Q8 | ₹80,000 | |
| Q9 | ₹1,60,000 | |
| Q10 | ₹3,20,000 | 🔒 Safe Haven |
| Q11 | ₹6,40,000 | |
| Q12 | ₹12,50,000 | |
| Q13 | ₹25,00,000 | |
| Q14 | ₹50,00,000 | |
| Q15 | ₹1,00,00,000 | 🏆 Grand Prize |

---

## 🧪 Running Tests

```bash
python -m unittest tests/test_game.py -v
```

**30 unit tests** covering:
- Question loading & filtering
- Answer checking (correct, wrong, case-insensitive)
- Safe haven & prize tracking
- Lifeline usage & reuse prevention
- Leaderboard save, sort & limit
- Utility formatting functions

---

## 📸 Screenshots

### Terminal Version
```
=======================================================
  🏆  KAUN BANEGA CROREPATI — FOOTBALL EDITION  🏆
=======================================================
  Answer 15 football questions to win ₹1,00,00,000!
  Safe havens at Q5 (₹10,000) and Q10 (₹3,20,000)
=======================================================

  Enter your name: Aditya

  Welcome, Aditya! Let's play! ⚽

=======================================================
  ❓ Question 1 of 15  |  Prize: ₹1,000
=======================================================
  🏆 Prize so far  : ₹0
  🔒 Safe haven   : ₹0
  🎯 Lifelines    : 5️⃣0️⃣-5️⃣0️⃣ | 👥 Audience Poll | 📞 Phone a Friend

  Which country won the first ever FIFA World Cup in 1930?
  A) Brazil   B) Argentina   C) Uruguay   D) Italy
```

---

## 🗺️ Controls

| Key | Action |
|---|---|
| `A` `B` `C` `D` | Answer the question |
| `L` | Use a lifeline |
| `P` | View prize ladder |
| `Q` | Quit & take winnings |

---

## 👨‍💻 Author

**Aditya Yadav**
- GitHub: [@InsightAdi](https://github.com/InsightAdi)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
