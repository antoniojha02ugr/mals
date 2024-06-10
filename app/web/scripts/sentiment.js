// Clear output and the selected dataset for sentiment analysis
function clearSentiment() {
    // Get a reference to the left and right input textareas and clear its value
    const inputLeftTextArea = document.getElementById('sentiment-left-input-tarea');
    const inputRightTextArea = document.getElementById('sentiment-right-input-tarea');
    inputLeftTextArea.value = '';
    inputRightTextArea.value = '';

    // Get a reference to the output textarea and clear its value
    const outputTextArea = document.getElementById('sentiment-output-tarea');
    outputTextArea.value = '';

    // Get a reference to the number of instances input and clear its value
    const instances = document.getElementById('s-instances');
    instances.value = '';

    selectedDataset = null;

    // Get all elements with the class name 'dataset'
    var datasets = document.getElementsByClassName('dataset');
    
    // Convert the HTMLCollection to an array for easier manipulation
    datasets = Array.from(datasets);

    // Remove the 'selected-dataset' class from all datasets
    datasets.forEach(function(dataset) {
        dataset.classList.remove('selected-dataset');
    });
}


// Run a sentiment analysis on a selected dataset (handled by the var selectedDataset defined on dataset.js)
async function runSentiment() {
    // Get references to the input left and right textareas, output textarea and the input for the number of instances
    const inputLeftTextArea = document.getElementById('sentiment-left-input-tarea');
    const inputRightTextArea = document.getElementById('sentiment-right-input-tarea');
    const outputTextArea = document.getElementById('sentiment-output-tarea');
    const inputInstances = document.getElementById('s-instances');

    // Check if the input message is empty
    if (selectedDataset == null) {
        outputTextArea.classList.add('error');
        outputTextArea.value = 'Please, select a dataset...';
        return;
    }

    // Check if the input for the number of instances is an int
    var instancesNumber = parseInt(inputInstances.value);

    if (isNaN(instancesNumber)) {
        outputTextArea.classList.add('error');
        outputTextArea.value = 'Number of selected instances must be an integer...';
        return;
    }

    // Check if the selected number of instances is correct (<= than the dataset's number of instances)
    if (instancesNumber < 1 || instancesNumber > parseInt(selectedDataset.dataset.ninstances)) {
        outputTextArea.classList.add('error');
        outputTextArea.value = 'Number of selected instances must be in range [1, instances of dataset]...';
        return;
    }

    // Check if a model is loaded, modelLoaded variable is handled in modelselect.js
    if (!modelLoaded) {
        outputTextArea.classList.add('error');
        outputTextArea.value = 'Please, select a model...';
        return;
    }

    // Creates a loading screen with a message in it
    const spinner_container = document.createElement('div');
    const spinner_text = document.createElement('div');

    // Asign a class (and its style) to each element
    spinner_container.classList.add('spinner-container');
    spinner_text.classList.add('spinner-text');

    spinner_text.textContent = 'Generating output, this might take a while...';

    // Include the text in the father container and it in the main document
    spinner_container.appendChild(spinner_text);
    document.body.appendChild(spinner_container);

    // Clear the error (if exists)
    outputTextArea.classList.remove('error');
    outputTextArea.value = '';

    try {
        // Make an API call to /api/run-sentiment with the input message
        const response = await fetch('/api/run-sentiment', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ dataset: selectedDataset.id, instances: instancesNumber , left: inputLeftTextArea.value, right: inputRightTextArea.value})
        });
    
        // Check if the API call was successful (status code 200)
        if (!response.ok) {
          throw new Error(`API call failed with status: ${response.status}`);
        }
    
        // Parse the JSON response from the API
        const responseData = await response.json();

        // Update the output textarea with the response message
        outputTextArea.value = responseData.output;

    } catch (error) {
        console.error('Error sending message:', error);
    } finally {
        // Remove the loading screen regardless of success or error
        document.body.removeChild(spinner_container);
    }
}