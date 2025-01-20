document.getElementById('loginForm').addEventListener('submit', function(e) {
        e.preventDefault();  // Prevent form from submitting traditionally

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // Send data to the Flask backend via AJAX (Fetch API)
        fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',  // Ensure the Content-Type is set to application/json
            },
            body: JSON.stringify({ email, password })  // Convert data to JSON format
        })
        .then(response => response.json())  // Parse JSON response from Flask
        .then(data => {
            if (!data.success) {
                document.getElementById('alert').innerHTML = data.error;
            }
        })
        .catch(error => {
            console.error('Error during login:', error);
        });
    });

document.getElementById('email').onfocus = function() {
    document.getElementById('alert').innerHTML = '';
}