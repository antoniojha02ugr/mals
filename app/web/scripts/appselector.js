function loadAppInterface(file) {
    var container = document.getElementById('app-interface');
    var xhr = new XMLHttpRequest();

    xhr.open('GET', file, true);

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            container.innerHTML = xhr.responseText;
        }
    };

    xhr.send();
}

loadAppInterface("/static/html/ginput.html")