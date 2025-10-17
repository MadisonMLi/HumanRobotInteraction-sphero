// Function to scroll a word letter by letter
async function scrollWord(word, color = [0, 255, 0], delay = 500) {
  for (let i = 0; i < word.length; i++) {
    const char = word[i];

    await fetch('http://127.0.0.1:5000/set_matrix_character', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ character: char, color })
    });

    // Wait before showing the next letter
    await new Promise(resolve => setTimeout(resolve, delay));
  }
}

// Scroll "HELLO" in green every 2 seconds
async function loopScroll() {
  const word = "HELLO";
  while (true) {
    await scrollWord(word, [0, 255, 0], 500);
  }
}

loopScroll();
