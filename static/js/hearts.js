function createHeart() {
  const heart = document.createElement('div');
  heart.classList.add('heart');
  heart.innerText = '💗';
  heart.style.left = Math.random() * 100 + 'vw';
  heart.style.fontSize = (Math.random() * 1.5 + 1) + 'rem';
  heart.style.animationDuration = (Math.random() * 2 + 3) + 's';

  document.getElementById('floating-hearts-container').appendChild(heart);
  setTimeout(() => heart.remove(), 6000);
}

setInterval(() => {
  createHeart();
}, Math.random() * 1000 + 500);