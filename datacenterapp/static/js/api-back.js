document.addEventListener('DOMContentLoaded', () =>{
    // Get the button that opens the modal
    const btn = document.getElementById('scan-btn');
    const confirmButton = document.getElementById('Confirm');
    const cancelButton = document.getElementById('Cancel');
    // Get the 'Confirm' and 'Fake alert' buttons for the 'fireModal'
    const confirFiremButton = document.getElementById('fire-confirm');
    const fakeButton = document.getElementById('fire-fake');
    // Get the 'Confirm' and 'Fake alert' buttons for the 'faceModal'
    const confirFaceButton = document.getElementById('face-confirm');
    const faceFakeButton = document.getElementById('face-fake');
    var firearea = document.getElementById('firearea1')
    // Get the 'Black-White', 'Names' and img
    var black_white = document.getElementById('black-white');
    var names = document.getElementById('face-name');
    var img_face = document.getElementById('face-img-modal');
    // Get the data from face modal
    var currentName = "";
    var currentStatus = "";
    var currentImageUrlface = "";
    // fire
    var img_fire = document.getElementById('fire-img-modal');
    var fire_img =  document.getElementById('fire-img-id');
    var currentImageUrlfire = "";
  
    // When the user clicks the button, open the modal 
    btn.onclick = function() {
        const modal = document.getElementById('gameModal');
        modal.style.display = "block";
    };

    // Function to initialize event listeners
    function initializeEventListeners() {
        const scanButton = document.getElementById('scanButton'); 
        scanButton.addEventListener('click', handleScanButtonClick);
    }
    
    // Function to handle click event on the 'SCAN' button
    function handleScanButtonClick() {
        const cabinetCode = document.getElementById('cabinetCodeInput').value; // Assuming an ID is assigned to the cabinet code input
        if (cabinetCode === "A20") {
        closeModal('gameModal');
        updateCabinetDetails();
        clearErrorMessage();
        sendScanData(cabinetCode);
        } else {
        displayErrorMessage(cabinetCode === "" ? "Please enter the cabinet code" : "There is no cabinet with this code");
        }
    }
    
    // Function to close any modal by ID
    function closeModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
        modal.style.display = "none";
        } else {
        console.error(`Modal with ID '${modalId}' not found.`);
        }
    }

    function showModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
          modal.style.display = 'block';
        } else {
          console.error(`Modal with ID '${modalId}' not found.`);
        }
    }
  
    // Function to update cabinet details in the UI
    function updateCabinetDetails() {
        const cabinetContent = document.getElementById('cabinetContent'); // Assuming an ID is assigned to the cabinet content container
        cabinetContent.innerHTML = `
        <p class="title pt-1">Details Panel</p>
                <p class="QSS ">QSS Cabinet</p>
                <p class="sum px-2">Cabinet serves as a hub for critical data management with three HDDs, 
                    all connected through an efficient cable management system ensuring secure and organized operations </p>


                <div class="row">
                    <div class="col-12 hdd">
                    <div class="row">
                        <div class="col-1  ">
                            <img src="/static/img/nic/hdd1.png" alt="" class="hdd1-img  ">
                        </div>

                        <div class="col-10  ">
                            <p class="hdd-title px-3">Software Info HDD</p>
                            <p class="sum-hdd">Central storage for system and application software, ensuring efficient software distribution and management</p>
                            <p class="serial-title">Serial number: <span class="serial">WX11DC9H2A4 </span></p>
                            <p class="serial-title">Last Update:: <span class="serial">10-5-2030 </span></p>
                            
                        </div>


                        <div class="col-1 ">
                            <img src="/static/img/nic/circle.png" alt="" class="circle" id="circle-1">
                        </div>
                    </div>

                    </div>
                </div>

                <div class="row">
                    <div class="col-12 hdd">
                    <div class="row">
                        <div class="col-1 ">
                            <img src="/static/img/nic/hdd2.png" alt="" class="hdd1-img">
                        </div>
                        <div class="col-10 ">
                            <div class="col-12  ">
                                <p  class="hdd-title px-3 ">Hardware Info HDD</p>
                                <p class="sum-hdd">Dedicated to storing logs and information pertinent to hardware specifications and configurations</p>
                                <p class="serial-title">Serial number: <span class="serial">WX11DC9H2S8V </span></p>
                                <p class="serial-title">Last Update:: <span class="serial">10-5-2030 </span></p>

                                
                            </div>
                        </div>
                        <div class="col-1 ">
                            <img src="/static/img/nic/circle.png" alt="" class="circle" id="circle-2">
                        </div>
                    </div>

                    </div>
                </div>

                <div class="row">
                    <div class="col-12 hdd">
                    <div class="row">
                        <div class="col-1">
                            <img src="/static/img/nic/hdd.png" alt="" class="hdd1-img">
                        </div>
                        <div class="col-10">
                            <p class="hdd-title px-3">Database HDD</p>
                            <p class="sum-hdd "> Houses critical databases, offering robust storage solutions for data integrity and quick access</p>
                            <p class="serial-title">Serial number: <span class="serial">WCC7K7FXD2 </span></p>
                            <p class="serial-title">Last Update:: <span class="serial">10-5-2030 </span></p>


                        </div>
                        <div class="col-1">
                            <img src="/static/img/nic/circle.png" alt="" class="circle" id="circle-3">
                        </div>
                    </div>

                    </div>
                </div>
        `;
    }
    
    // Function to clear any error message
    function clearErrorMessage() {
        const errorMessage = document.getElementById('errorMessage'); 
        errorMessage.style.display = 'none';
        errorMessage.textContent = '';
    }
    
    // Function to display an error message
    function displayErrorMessage(message) {
        const errorMessage = document.getElementById('errorMessage'); 
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
    }
    
    // Function to send scan data using AJAX
    function sendScanData(cabinetCode) {
        const dataToSend = { dataItem: "scan", cabinetCode: cabinetCode };
        $.ajax({
        url: '/start_scanning/',
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(dataToSend),
        dataType: 'json',
        success: function(response) {
            console.log('Success: ' + response.message);
        },
        error: function(xhr, textStatus, errorThrown) {
            console.log('Error: ' + xhr.responseText);
        }
        });
    }

    // Utility function to perform AJAX request with given action
    async function performSwapAction(action) {
        const dataToSend = { dataItem: action };
        response = await $.ajax({
        url: '/start_swapping/', // The URL to your Django view
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(dataToSend),
        dataType: 'json'
        }).done(function(response) {
        console.log('Success:', response.message);
        }).fail(function(xhr, textStatus, errorThrown) {
        console.log('Error:', xhr.responseText);
        });
        return response
    }
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    // Event listener for the 'Confirm swapping' button
    confirmButton.addEventListener('click', function() {
        performSwapAction("swap").then(() => {
        sleep(2000);
        addNotification("The swapping has been confirmed.");
        closeModal('redModal');

        });
    });
    
    // Event listener for the 'Cancel swapping' button
    cancelButton.addEventListener('click', function() {
        performSwapAction("cancel").then(() => {
        addNotification("The swapping has been canceled.");
        closeModal('redModal');

        });
    });
    
    // Reusable function for performing AJAX requests
    function performAjaxRequest(action, message) {
        $.ajax({
            url: '/faical_recog/',  // Assuming this is a generic endpoint that handles various actions
            type: 'POST',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({ dataItem: action }),
            dataType: 'json'
        }).done(function(response) {
            console.log('Success:', response.message);
        }).fail(function(xhr, textStatus, errorThrown) {
            console.log('Error:', xhr.responseText);
        });

        // Add notification and handle common modal behavior
        addNotification(message);
        closeModal('fireModal');  // Assuming 'fireModal' is the correct ID for the fire modal
    }

    function performAjaxRequestCancel() {
        $.ajax({
            url: '/faical_recog_cancel/',  // Assuming this is a generic endpoint that handles various actions
            type: 'POST',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json'
        }).done(function(response) {
            console.log('Success:', response.message);
        }).fail(function(xhr, textStatus, errorThrown) {
            console.log('Error:', xhr.responseText);
        });
    }

    // Reusable function to close modals by ID
    function closeModal(modalId) {
        document.getElementById(modalId).style.display = "none";
    }

    // Confirm fire button listener
    confirFiremButton.addEventListener('click', function() {
        performAjaxRequest("Confirm fire", "The fire detected in the AL3 area has been confirmed.");
        firearea.textContent = "AL3"; // Assuming 'firearea' is correctly defined elsewhere
        fire_img.src = currentImageUrlfire; // Ensure 'fire_img' is defined and accessible
        img_fire.style.width = '170px'; // Assuming 'img_fire' is correctly defined elsewhere
    });

    // Fake fire button listener
    fakeButton.addEventListener('click', function() {
        performAjaxRequest("fake fire", "The fire detected in the AL3 area is a fake alert.");
    });

    // Confirm Face button listener
    confirFaceButton.addEventListener('click', function() {
        closeModal('faceModal');
        updateFaceRecognitionResults();
        performAjaxRequestCancel()

    });

    // Cancel Face fire button listener
    faceFakeButton.addEventListener('click', function() {
        closeModal('faceModal');
        addNotification("False alert regarding face recognition.");
        performAjaxRequestCancel()
    });

    // Function to update elements with global variables for face recognition
    function updateFaceRecognitionResults() {
        const statusElement = document.getElementById('Status'); // Ensure this is the correct ID
        const nameElement = document.getElementById('theName'); // Ensure this is the correct ID
        document.getElementById('face-img').src = currentImageUrlface; // Assuming 'face-img' is the correct ID

        statusElement.textContent = currentStatus + ' List'; // Assuming 'currentStatus' is defined and accessible
        nameElement.textContent = currentName; // Assuming 'currentName' is defined and accessible

        // Assuming the comparison should be against the text content of the 'Status' element, not the variable itself
        if (statusElement.textContent.includes('Black')) {
            addNotification("An unauthorized person has been detected.");
        } else if (statusElement.textContent.includes('White')) {
            addNotification("An authorized person has been detected.");
        }
    }

    // Function to fetch and update counts from the server, then display modal based on conditions
    async function updateCounts() {
    let redHard1 = "Issue detected on hard disk with serial number: WX11DC9H2S8V";
    let redHard2 = "";
    try {
        const response = await fetch('/Red_Green/');
        const data = await response.json();
        // Check specific condition to update status and display modal
        if (data.objects.red == 1 && redHard1 !== redHard2) {
            updateCircleStatus('/static/img/nic/circle-green.png', '/static/img/nic/circle-red.png', '/static/img/nic/circle-green.png');
            addNotification(redHard1)
            showModal('redModal')
            redHard2 = redHard1;
        }
    } catch (error) {
        console.error('Error:', error);
    }
    }

    // Function to update the status of circles with given image sources
    function updateCircleStatus(circle1Src, circle2Src, circle3Src) {
    const circle1 = document.getElementById('circle-1');
    const circle2 = document.getElementById('circle-2');
    const circle3 = document.getElementById('circle-3');

    if (circle1) circle1.src = circle1Src;
    if (circle2) circle2.src = circle2Src;
    if (circle3) circle3.src = circle3Src;
    }

    function fire_detection() {
        let fireDetection1 = "Fire Detected in AL3 area";
        let fireDetection2 = "";
        // Make an AJAX request to the Django server
        fetch('/fire/')
            .then(response => response.json())
            .then(data => {
                var keys = Object.keys(data.face).map(key => capitalizeFirstLetter(key));
                var values = Object.values(data.face)
                var length = keys.length; // Gets the length of the keys array
             if (data.fire == 'fire' && fireDetection1 !== fireDetection2) {
                    let original_fire_img_path = data.path
                    let new_fire_img_path = "";
                    new_fire_img_path = original_fire_img_path.replace(/\\/g, '/').replace('datacenterapp', '');
                    addNotification(fireDetection1);
                    img_fire.src = new_fire_img_path;
                    currentImageUrlfire = new_fire_img_path;   
                    showModal('fireModal')
                    // Update fireDetection2 to match fireDetection1
                    fireDetection2 = fireDetection1;
                }

            if (length > 0){
                black_white.innerHTML = '<span class="status">Status:</span> ' + keys.join(', ') + ' List';
                names.innerHTML = '<span class="status">Name:</span> ' + values.join(', ');
                currentStatus = keys.join(', ');
                currentName = values.join(', ');
                img_face.src = determineImageSource(values); // Function to determine the image source
                currentImageUrlface = determineImageSource(values); // Implement this function as needed

                // showModalface()
                showModal('faceModal')
                }
            })
            
            .catch(error => console.error('Error:', error));
    }

    function capitalizeFirstLetter(string) {
        if (!string) {
            return '';
        }
        return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
    }
    
    function determineImageSource(values) {
        const basePath = '/static/img/persons/';
        const imagePath = `${basePath}${values}.png`;
        return imagePath;
    }

    function addNotification(message) {
        let notificationContainer = document.getElementById('notificationContainer');
        // Get the current date and time
        let now = new Date();
        let timestamp = now.toLocaleString(); // Formats the date and time as a string
    
        // Create notification HTML structure
        let notificationHtml = `
            <div class="container">
                <div class="row">
                    <div class="col-1 text-center pb-1">
                        <img src="/static/img/nic/bell1.png" alt="" width="25" class="">
                    </div>
                    <div class="col-8">
                        <p class="note">${message}</p> 
                    </div>
                    <div class="col-3 date text-center">
                        ${timestamp}
                    </div>
                    <p class="line"></p>
                </div>
            </div>`;
    
        // Append new notification to the container
        notificationContainer.innerHTML = notificationHtml + notificationContainer.innerHTML;

    }

    // Periodically update counts
    setInterval(updateCounts, 1000);
    setInterval(fire_detection, 500);
    // Call the function to initialize event listeners
    initializeEventListeners();
});


