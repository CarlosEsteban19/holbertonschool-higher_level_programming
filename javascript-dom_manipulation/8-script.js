function fetchHello() {
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
const displayHello = document.getElementById('hello');
fetch(url)
.then((response) => response.json())
.then((data) => {
    displayHello.textContent = data.hello;
})
.catch((error) => {
    console.error("Error: ", error);
});
}
document.addEventListener('DOMContentLoaded', fetchHello);
