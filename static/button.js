const button = document.getElementById('compute-schedules-btn');
const loading = document.getElementById('loading');

button.addEventListener('click', () => {
  button.style.display = 'none';
  loading.style.display = 'block'; 
  
  const data = { 
    'some_data': 'example data'
  };
  const csrftoken = getCookie('csrftoken');
  
  // Simulate some processing time
  setTimeout(() => {
    // Send a GET request to the Python function
    fetch('/schedule/compute/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
      })
    .then(response => response.json())
    .then(data => {
        // Update the CSS styling based on the response
        if (data.status === 'success') {
        loading.style.display = 'none';
        // Redirect to another page if needed
        window.location.href = '/schedule';
        } else {
        button.style.display = 'block';
        loading.style.display = 'none';
        alert('Error computing schedules');
        }
    })
    .catch(error => {
        button.style.display = 'block';
        loading.style.display = 'none';
        alert('Error computing schedules');
    });
  }, 1000);
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }