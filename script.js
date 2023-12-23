document.addEventListener('DOMContentLoaded', function() {
    fetch('links.csv')
    .then(response => response.text())
    .then(text => {
        const data = parseCSV(text);
        createTable(data);
    })
    .catch(error => console.error('Error fetching the CSV:', error));
});

function parseCSV(text) {
    const lines = text.split('\n');
    return lines.map(line => line.split(','));
}

function createTable(data) {
    const table = document.getElementById('csvTable');
    data.forEach((row, rowIndex) => {
        const tr = document.createElement('tr');
        row.forEach((cell, cellIndex) => {
            const td = document.createElement('td');
            if (rowIndex > 0 && cellIndex === 1) { // Assuming second column contains URLs
                const a = document.createElement('a');
                a.href = cell;
                a.textContent = cell;
                td.appendChild(a);
            } else {
                td.textContent = cell;
            }
            tr.appendChild(td);
        });
        table.appendChild(tr);
    });
}
