function clearInput() {
    var i;
    var textareas = document.getElementsByClassName('ginput-tarea');
    
    for (i = 0; i < textareas.length; ++i) {
        textareas[i].value = '';
    }
}