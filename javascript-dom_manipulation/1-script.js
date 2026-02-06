const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');
function redHeaderAction(){
    header.style.color = 'red';
}
redHeader.addEventListener("click",redHeaderAction)