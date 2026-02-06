const list = document.getElementById('list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(res => res.json())
    .then(data => {
        const movies = data.results;
        movies.forEach(movie => {
            const li = document.createElement('li');
            li.textContent = movie.title;
            list.append(li);
        });
    })
    .catch(error => {
        console.error("Error:", error);
    });
