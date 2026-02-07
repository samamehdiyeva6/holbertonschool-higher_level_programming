document.addEventListener('DOMContentLoaded', function () {
    const helloText = document.getElementById('hello')
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(data => data.json())
    .then(data => {
        helloText.textContent = data.hello;
    })
    .catch(error => {
        console.error("Error fetching translation:", error);
    });
})
