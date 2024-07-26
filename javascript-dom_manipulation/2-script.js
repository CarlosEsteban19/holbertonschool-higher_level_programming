const header = document.getElementById("red_header");
header.addEventListener('click', setRedClass);
function setRedClass() {
    header.classList.add('red');
}
