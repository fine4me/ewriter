document.getElementById('signupForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const age = document.getElementById('age').value;
    const password = document.getElementById('password').value;
    const email = document.getElementById('email').value;

    // Show loading state
    console.log('Attempting signup...');

    fetch('http://localhost:5000/signup', {
        method: 'POST',
        headers: {  // Fixed: 'headers' instead of 'contentType'
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username,
            email,
            password,
            age
        })
    })
    .then(response => {
        console.log(`Response status: ${response.status}`);
        return response.json();
    })
    .then(data => {
        console.log('Server response:', data);

        if (data.success) {
            console.log('Signup successful!');
            // Redirect or show success message
            document.getElementById('alert').innerHTML = 'Signup successful!';
        } else {
            console.error('Signup failed:', data.error);
            document.getElementById('alert').innerHTML = data.error || 'Signup failed';
        }
    })
    .catch(error => {
        console.error('Error during signup:', error);
        document.getElementById('alert').innerHTML = 'An error occurred during signup';
    });
});