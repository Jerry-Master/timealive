const button = document.getElementById('compute-schedules-btn');
const loading = document.getElementById('loading');

button.addEventListener('click', () => {
  button.style.display = 'none';
  loading.style.display = 'block';
  
  // Simulate some processing time
  setTimeout(() => {
    button.style.display = 'block';
    loading.style.display = 'none';
    window.location.href = '/schedule';
  }, 3000);
});
