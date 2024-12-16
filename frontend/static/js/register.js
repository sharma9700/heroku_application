$(document).ready(function() {
    $("#register-form").submit(async function(event) {
        event.preventDefault();
		
        // Fetch field values
        const username = $('#username').val();
        const email = $('#email').val();
        const pswd = $('#pswd').val();
        const ppswd = $('#ppswd').val();
        const full_name = $('#name').val();
        const phone_number = $('#phno').val();
        const dob = $('#dobInput').val();
		
        let isValid = true;
        let errorMessages = [];

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email && !emailRegex.test(email)) {
            isValid = false;
            errorMessages.push("Please enter a valid email address.");
        }

        // Password validation
        const passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        if (pswd && !passwordRegex.test(pswd)) {
            isValid = false;
            errorMessages.push("Password must be at least 8 characters long, include one uppercase letter, one number, and one special character.");
        }

        // Confirm Password Matching
        if (pswd && ppswd && pswd !== ppswd) {
            isValid = false;
            errorMessages.push("Passwords do not match.");
        }

        // Phone Number Validation
        if (phone_number) {
            const phoneRegex = /^\d{10}$/;
            if (!phoneRegex.test(phone_number)) {
                isValid = false;
                errorMessages.push("Please enter a valid 10-digit phone number.");
            }
        }

        // Date of Birth Validation
        if (dob) {
            const dobDate = new Date(dob);
            const today = new Date();
            const age = today.getFullYear() - dobDate.getFullYear();
            const monthDifference = today.getMonth() - dobDate.getMonth();
            if (
                age < 17 ||
                (age === 17 && monthDifference < 0) ||
                (age === 17 && monthDifference === 0 && today.getDate() < dobDate.getDate())
            ) {
                isValid = false;
                errorMessages.push("You must be at least 17 years old to register.");
            }
        }

        // Display errors or proceed with submission
        if (!isValid) {
            alert(errorMessages.join("\n"));
            return;
        }
		
        const data = {
            username: username,
            email: email,
            password: ppswd,
            full_name: full_name,
            phone_number: phone_number,
            dob: dob
        };
		
        try {
			const response = await fetch('https://login-webpage-309e19837628.herokuapp.com/auth/register', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(data)
			});

            if (response.ok) {
                const result = await response.json();
                console.log("Success:", result);
                alert("Registration successful!");
                // Clear the form or redirect
                window.location.href = "/login";
            } else {
                const errorData = await response.json();
                console.error("Error:", errorData);
                alert("Registration failed: " + (errorData.message || "Unknown error."));
            }
        } catch (error) {
            console.error("Request failed:", error);
            alert("An error occurred while processing your request. Please try again later.");
        }
    });
});
