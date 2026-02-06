const toggle = document.querySelector('#toggle_header');
const header = document.querySelector('header');
function reverse() {
    header.classList.toggle('red');
    header.classList.toggle('green');
}
toggle.addEventListener("click", reverse);
