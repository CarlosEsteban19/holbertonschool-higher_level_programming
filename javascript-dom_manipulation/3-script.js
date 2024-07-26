const header = document.getElementById('toggle_header');
if (!header.classList.contains('red') && !header.classList.contains('green')) {
    header.classList.add('red');
}
header.addEventListener('click', toggleClass);
function toggleClass() {
    if (header.classList.contains('red')) {
        header.classList.replace('red', 'green');
    } else {
        header.classList.replace('green', 'red');
    }
}
