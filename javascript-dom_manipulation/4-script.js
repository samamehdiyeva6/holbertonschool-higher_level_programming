const item = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

function add() {
    const li = document.createElement('li');
    li.textContent = 'Item';
    list.append(li);
}
item.addEventListener("click", add);
