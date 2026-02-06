const character = document.getElementById('character');
fetch('https://swapi-api.hbtn.io/api/people/4/?format=json')
    .then(res => res.json())
    .then(data => {
        character.textContent = data.name;
    })
    .catch(error => {
        console.error("Error:", error);
    })