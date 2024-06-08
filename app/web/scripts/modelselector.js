// Index of the current model card shown
var modelIndex = 0;
var modelLoaded = false;
showModel(modelIndex);

// Show the previous model
function prevModel() {
    showModel(modelIndex -= 1);
}

// Show the next model
function nextModel() {
    showModel(modelIndex += 1);
}

// Show the model of correspondent to the index n
function showModel(n) {
    var i;

    // Get the reference to all model cards
    var models = document.getElementsByClassName('model-card');

    // Control the ciclic indexing
    if (n > models.length - 1) {
        modelIndex = 0
    }
    if (n < 0) {
        modelIndex = models.length - 1
    }

    // Hide all model cards except that one corresponding to the current index
    for (i = 0; i < models.length; ++i) {
        models[i].style.display = 'none';
    }
    models[modelIndex].style.display = 'block';
}

// Sends to the API the selected model and waits until the model is loaded
async function selectModel() {
    // Get the reference to all models to send the name of the one corresponding to the current index
    var models = document.getElementsByClassName('model-card');

    // Creates a loading screen with a message in it
    const spinner_container = document.createElement('div');
    const spinner_text = document.createElement('div');

    // Asign a class (and its style) to each element
    spinner_container.classList.add('spinner-container');
    spinner_text.classList.add('spinner-text');

    spinner_text.textContent = 'Loading model, this might take a while...';

    // Include the text in the father container and it in the main document
    spinner_container.appendChild(spinner_text);
    document.body.appendChild(spinner_container);

    try {
        // Asyncronous send of the model identificator to the API
        const response = await fetch('/api/select-model', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ id: models[modelIndex].id })
        });
    
        // Check for successful response
        if (!response.ok) {
          throw new Error(`API call failed with status: ${response.status}`);
        }
        
        // Display the models name in the interface
        var model_display = document.getElementById('model-display');
        model_display.textContent = models[modelIndex].dataset.modelName;

        modelLoaded = true;

    } catch (error) {
        console.error('Error selecting model:', error);
        
    } finally {
        // Remove the loading screen regardless of success or error
        document.body.removeChild(spinner_container);
    }
}