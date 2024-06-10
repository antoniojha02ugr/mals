// Initialize a variable to store the currently selected dataset
var selectedDataset = null;

// Function to set up dataset selection behavior, called on each app selection (appselector.js function loadAppInterface)
function setupDatasetSelection() {
    // Get all elements with the class name 'dataset'
    var datasets = document.getElementsByClassName('dataset');
    
    // Convert the HTMLCollection to an array for easier manipulation
    datasets = Array.from(datasets);

    selectedDataset = null;

    // Add a click event listener to each element with the class 'dataset'
    datasets.forEach(function(dataset) {
        dataset.addEventListener('click', function() {
            // Remove the 'selected-dataset' class from all datasets
            datasets.forEach(function(d) {
                d.classList.remove('selected-dataset');
            });
            // Add the 'selected-dataset' class to the clicked dataset
            this.classList.add('selected-dataset');

            // Update the selectedDataset variable to the clicked dataset
            selectedDataset = this;

            // Select instances input (if exists) and set its value to dataset's instances
            var instances = document.getElementsByClassName('instances');
            if (instances.length > 0) {
                instances[0].value = this.dataset.ninstances;
            }
        });
    });
}
