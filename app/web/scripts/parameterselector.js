// Updates the content of the outbox_id element with value
function updateParameterValue(value, outputbox_id) {
    document.getElementById(outputbox_id).value = value;
}

// Set the initial content of each parameter's output box to the slider value
updateParameterValue(document.getElementById('mt-r').value, 'mt-v');
updateParameterValue(document.getElementById('te-r').value, 'te-v');
updateParameterValue(document.getElementById('tp-r').value, 'tp-v');
updateParameterValue(document.getElementById('tk-r').value, 'tk-v');
