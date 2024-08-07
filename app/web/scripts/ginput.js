// Clear the input and output textareas of general input app
function clearGinput() {
    var i;

    // Get a reference to the textareas to be cleared
    var textareas = document.getElementsByClassName('text-area');
    
    // Set its value (text) to the empty string 
    for (i = 0; i < textareas.length; ++i) {
        textareas[i].value = '';
    }
}


async function runGinput() {
    // Get references to the input and output textareas
    const inputTextArea = document.getElementById('ginput-input-tarea');
    const outputTextArea = document.getElementById('ginput-output-tarea');

    // Get the input message from the input textarea
    const inputMessage = inputTextArea.value;

    // Check if the input message is empty
    if (!inputMessage) {
        outputTextArea.classList.add('error');
        outputTextArea.value = 'Please, enter an input...';
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
        // Get the values of the parameter sliders
        const mt = parseInt(document.getElementById('mt-r').value);
        const te = parseFloat(document.getElementById('te-r').value);
        const tp = parseFloat(document.getElementById('tp-r').value);
        const tk = parseInt(document.getElementById('tk-r').value);

        // Make an API call to /api/run-ginput with the input message
        const response = await fetch('/api/run-ginput', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ inpt: inputMessage, parameters: {max_tokens: mt, temperature: te, top_p: tp, top_k: tk} })
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