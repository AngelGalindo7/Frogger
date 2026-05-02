// Patch String.repeat to clamp negative counts (int32 overflow bug in pygbag's pollReady)
const _repeat = String.prototype.repeat;
String.prototype.repeat = function(n) { return _repeat.call(this, n < 0 ? 0 : n); };

const btn     = document.getElementById('playBtn');
const status  = document.getElementById('overlayStatus');
const fade    = document.getElementById('fade');
const overlay = document.getElementById('overlay');
const loadBar = document.getElementById('overlayLoadBar');
let   waiting = false;

function animateDots() {
  if (waiting || window.pygame_ready) { status.textContent = ''; return; }
  status.textContent = 'Loading' + '.'.repeat(Math.floor(Date.now() / 450) % 4);
  setTimeout(animateDots, 250);
}
animateDots();

function launchGame() {
  fade.classList.add('out');
  setTimeout(() => {
    overlay.classList.add('fade-out');
    setTimeout(() => { fade.style.display = 'none'; }, 50);
  }, 680);
}

btn.addEventListener('click', () => {
  if (window.pygame_ready) {
    launchGame();
  } else {
    waiting = true;
    btn.disabled = true;
    btn.textContent = 'LOADING';
    status.textContent = '';
    loadBar.classList.add('active');
    (function waitForReady() {
      if (window.pygame_ready) { launchGame(); }
      else { setTimeout(waitForReady, 100); }
    })();
  }
});
