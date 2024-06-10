// Load the content of a fragment file into the element with the ID "app-interface"
function loadAppInterface(file) {
    // Get a reference to the element that will hold the fragment content
    var container = document.getElementById('app-interface');

    // Create a new XMLHttpRequest object to make an HTTP GET request
    var xhr = new XMLHttpRequest();

    // Open the request to get the correspondent file
    xhr.open('GET', file, true);

    // Define a function to handle the state changes of the XMLHttpRequest
    xhr.onreadystatechange = function() {
        // Check if the request is completed (readyState === 4) and successful (status === 200)
        if (xhr.readyState === 4 && xhr.status === 200) {
            container.innerHTML = xhr.responseText;
            
            // Update dataset logic and listeners
            setupDatasetSelection();
        }
    };

    // Send the asynchronous HTTP GET request
    xhr.send();
}

// Load the general input interface by default
loadAppInterface("/static/html/ginput.html")