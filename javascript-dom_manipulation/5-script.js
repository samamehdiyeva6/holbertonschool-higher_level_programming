const header = document.querySelector('header');
const update = document.querySelector('#update_header')
function updateText() {
    header.textContent = 'New Header!!!';
}
update.addEventListener("click", updateText);
