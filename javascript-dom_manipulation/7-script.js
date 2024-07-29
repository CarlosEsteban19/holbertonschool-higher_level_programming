const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const movieList = document.getElementById('list_movies');
fetch(url)
.then((response) => response.json())
.then((data) => {
    data.results.forEach(movie => {
        const item = document.createElement('li');
        item.textContent = movie.title;
        movieList.appendChild(item);
    });
})
.catch((error) => {
    console.error("Error: ", error);
});
