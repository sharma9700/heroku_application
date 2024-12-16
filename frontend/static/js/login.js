$(document).ready(function() {
    $('#login-form').submit(async function(event) {
        event.preventDefault(); // Prevent the default form submission

        var username = $('#user').val();
        var password = $('#password').val();

        // Print the username and password to the console (for testing)
        console.log('Username: ' + username);
        console.log('Password: ' + password);
		
		document.getElementById('overlay').style.display = 'flex';
        try {
            // Send POST request to the server
            const response = await fetch('https://login-webpage-309e19837628.herokuapp.com/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'datatype': 'json'
                },
                body: JSON.stringify({ username, password }),
                credentials: 'include'  // If you are using cookies or authentication
            });

            const data = await response.json();
			console.log('data', data);

            switch (response.status) {
                case 200:
                    window.location.href = "aws"; // Redirect on success
                    console.log(data.body || "Login Successful");
                    break;
                case 400:
                    alert(data.body || "Invalid Credentials");
                    console.log(data.body || "Invalid Credentials");
                    break;
                case 404:
                    alert(data.body || "Email is not Registered");
                    console.log(data.body || "Email is not Registered");
                    break;
                default:
                    alert("An unknown error occurred, please try again");
                    console.log("Unknown error");
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        }
    });
});
