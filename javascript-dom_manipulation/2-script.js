const redHeader = document.querySelector('#red_header');
const header = document.querySelector('header');
function changeColor(){
    header.classList.add('red');
}
redHeader.addEventListener("click", changeColor);
