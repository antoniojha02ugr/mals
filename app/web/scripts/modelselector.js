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
    var models = document.getElementsByClassName("model-card");

    if (n > models.length - 1) {modelIndex = 0}
    if (n < 0) {modelIndex = models.length - 1}

    for (i = 0; i < models.length; ++i) {
        models[i].style.display = "none";
    }

    models[modelIndex].style.display = "block";
}
