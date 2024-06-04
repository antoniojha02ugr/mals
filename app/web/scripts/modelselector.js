var modelIndex = 0;
showModel(modelIndex);

function prevModel() {
    showModel(modelIndex -= 1);
}

function nextModel() {
    showModel(modelIndex += 1);
}

function showModel(n) {
    var i;
    var models = document.getElementsByClassName('model-card');

    if (n > models.length - 1) {
        modelIndex = 0
    }

    if (n < 0) {
        modelIndex = models.length - 1
    }

    for (i = 0; i < models.length; ++i) {
        models[i].style.display = 'none';
    }

    models[modelIndex].style.display = 'block';
}

async function selectModel() {
    var models = document.getElementsByClassName('model-card');

    const spinner_container = document.createElement('div');
    const spinner_text = document.createElement('div');

    spinner_container.classList.add('spinner-container');
    spinner_text.classList.add('spinner-text');

    spinner_text.textContent = 'Loading model, this can take a long';

    spinner_container.appendChild(spinner_text);
    document.body.appendChild(spinner_container);

    await fetch('/api/select-model', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: models[modelIndex].id })
    });

    var model_display = document.getElementById('model-display')
    model_display.textContent = models[modelIndex].dataset.modelName;

    document.body.removeChild(spinner_container);
}