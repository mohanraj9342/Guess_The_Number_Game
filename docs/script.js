(() => {
  // State
  const maxAttempts = 10;
  let secret = randInt(1, 100);
  let attempts = 0;
  let score = maxAttempts * 10;
  let hintUsed = false;
  let gameOver = false;

  // Elements
  const attemptsLeftEl = document.getElementById('attemptsLeft');
  const scoreEl = document.getElementById('score');
  const messageEl = document.getElementById('message');
  const guessInput = document.getElementById('guessInput');
  const guessBtn = document.getElementById('guessBtn');
  const hintGate = document.getElementById('hintGate');
  const hintBtn = document.getElementById('hintBtn');
  const hintsEl = document.getElementById('hints');
  const historyList = document.getElementById('historyList');
  const playAgainBtn = document.getElementById('playAgainBtn');
  const resetBtn = document.getElementById('resetBtn');

  updateUI();

  guessBtn.addEventListener('click', onGuess);
  hintBtn.addEventListener('click', onHint);
  playAgainBtn.addEventListener('click', resetGame);
  resetBtn.addEventListener('click', hardReset);
  guessInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') onGuess();
  });

  function onGuess() {
    if (gameOver) return;
    const val = Number(guessInput.value);
    if (!Number.isInteger(val) || val < 1 || val > 100) {
      setMessage('🚫 Please enter a number between 1 and 100.', 'warn');
      return;
    }

    attempts += 1;
    addHistory(val);

    if (val < secret) setMessage('📉 Too low!');
    else if (val > secret) setMessage('📈 Too high!');
    else {
      const base = (maxAttempts - attempts) * 10;
      score = base - (hintUsed ? 5 : 0);
      score = Math.max(score, 0);
      endGame(`🎉 Congratulations! You guessed ${secret} in ${attempts} attempts. 🏆 Your score: ${score}`);
      return;
    }

    if (attempts === 5 && !hintUsed) {
      hintGate.classList.remove('hidden');
    }

    if (attempts >= maxAttempts) {
      endGame(`❌ Game Over! The correct number was ${secret}. 😢 Better luck next time!`);
      return;
    }

    updateUI();
    guessInput.select();
  }

  function onHint() {
    if (hintUsed || gameOver) return;
    hintUsed = true;
    score = Math.max(score - 5, 0);
    hintGate.classList.add('hidden');
    hintsEl.classList.remove('hidden');
    hintsEl.innerHTML = '';

    // Hint 1: Even or Odd
    addHint(`🤔 Hint 1: The number is ${secret % 2 === 0 ? 'EVEN' : 'ODD'}.`);

    // Hint 2: Range bucket (e.g., 30-40)
    const lower = Math.floor(secret / 10) * 10;
    const upper = Math.min(lower + 10, 100);
    addHint(`📏 Hint 2: The number is between ${lower} and ${upper}.`);

    // Hint 3: Divisibility / multiples
    if (secret % 5 === 0) addHint('➗ Hint 3: The number is divisible by 5.');
    else if (secret % 10 === 0) addHint('➗ Hint 3: The number is divisible by 10.');
    else {
      const mults = [3, 4, 7].filter((n) => secret % n === 0);
      if (mults.length) addHint(`➗ Hint 3: The number is a multiple of ${mults.join(', ')}.`);
      else addHint('➗ Hint 3: The number is NOT a multiple of 3, 4, or 7.');
    }

    updateUI();
  }

  function endGame(text) {
    gameOver = true;
    setMessage(text, 'success');
    playAgainBtn.hidden = false;
    guessBtn.disabled = true;
    guessInput.disabled = true;
    updateUI();
  }

  function resetGame() {
    secret = randInt(1, 100);
    attempts = 0;
    score = maxAttempts * 10;
    hintUsed = false;
    gameOver = false;
    messageEl.textContent = "I'm thinking of a number between 1 and 100.";
    clearHints();
    historyList.innerHTML = '';
    guessBtn.disabled = false;
    guessInput.disabled = false;
    playAgainBtn.hidden = true;
    updateUI();
    guessInput.focus();
  }

  function hardReset() {
    resetGame();
  }

  function updateUI() {
    attemptsLeftEl.textContent = Math.max(maxAttempts - attempts, 0);
    scoreEl.textContent = Math.max((maxAttempts - attempts) * 10 - (hintUsed ? 5 : 0), 0);
  }

  function setMessage(text, kind) {
    messageEl.textContent = text;
    messageEl.style.color = kind === 'warn' ? '#ffd48a' : kind === 'success' ? '#a7f3d0' : '#cdd6f4';
  }

  function addHint(text) {
    const p = document.createElement('div');
    p.textContent = text;
    p.className = 'hint';
    hintsEl.appendChild(p);
  }
  function clearHints() {
    hintsEl.classList.add('hidden');
    hintsEl.innerHTML = '';
    hintGate.classList.add('hidden');
  }

  function addHistory(val) {
    const li = document.createElement('li');
    li.textContent = `#${attempts}: ${val} ${val < secret ? '↘️ too low' : val > secret ? '↗️ too high' : '✅ correct'}`;
    historyList.appendChild(li);
  }

  function randInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
})();
