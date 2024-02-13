
const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

document.getElementById('runScriptArm').addEventListener('click', function() {
    // Send an AJAX request using fetch
    fetch('/armController/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: 'command=runScriptArm',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Print the response from the server
        console.log("armController- run Script Arm")
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


document.getElementById('StopScriptArm').addEventListener('click', function() {
    // Send an AJAX request using fetch
    fetch('/armController/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: 'command=StopScriptArm',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Print the response from the server
        console.log("armController- StopScriptArm")
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


document.getElementById('emergencyStopArm').addEventListener('click', function() {
    // Send an AJAX request using fetch
    fetch('/armController/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: 'command=emergencyStopArm',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Print the response from the server
        console.log("armController- emergencyStopArm")
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


document.getElementById('enableRobotArm').addEventListener('click', function() {
    // Send an AJAX request using fetch
    fetch('/armController/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: 'command=enableRobotArm',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Print the response from the server
        console.log("armController- enableRobotArm")
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('disableRobotArm').addEventListener('click', function() {
    // Send an AJAX request using fetch
    fetch('/armController/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: 'command=disableRobotArm',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Print the response from the server
        console.log("armController- disableRobotArm")
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


// AMR

document.getElementById('runScriptAmr').addEventListener('click', function() {
    // Send an AJAX request using fetch
    fetch('/amrController/', {
        method: 'POST',
        headers: {
             'Content-Type': 'application/x-www-form-urlencoded',
             'X-CSRFToken': csrftoken,
        },
        body: 'command=runScriptAmr',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Print the response from the server
        console.log("armController- runScriptAmr")
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('stopScriptAmr').addEventListener('click', function() {
    // Send an AJAX request using fetch
    fetch('/amrController/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
             'X-CSRFToken': csrftoken,
        },
        body: 'command=stopScriptAmr',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Print the response from the server
        console.log("armController- stopScriptAmr")
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('emergencyStopAmr').addEventListener('click', function() {
    // Send an AJAX request using fetch
    fetch('/amrController/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: 'command=emergencyStopAmr',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Print the response from the server
        console.log("armController- emergencyStopAmr")
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
