function toggleTheme() {
  document.body.classList.toggle('dark-theme');

  if (document.body.classList.contains('dark-theme')) {
      localStorage.setItem('theme', 'dark');
  } else {
      localStorage.setItem('theme', 'light');
  }
}

window.onload = function() {
  const theme = localStorage.getItem('theme');
  if (theme === 'dark') {
      document.body.classList.add('dark-theme');
      document.getElementById('toggle').checked = true;
  }
};
function toggleTheme() {
  document.body.classList.toggle('dark-theme');
}
