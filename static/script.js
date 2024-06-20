function appendSymbol(symbol) {
    document.getElementById('display').value += symbol;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculate() {
    let expression = document.getElementById('display').value;
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression: expression })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('display').value = data.result;
    })
    .catch(error => console.error('Error:', error));
}
