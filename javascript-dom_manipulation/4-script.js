const item = document.getElementById('add_item');
const myList = document.querySelector('ul.my_list');
item.addEventListener('click', addTheItem);
function addTheItem() {
    const listItem = document.createElement('li');
    listItem.textContent = 'Item';
    myList.appendChild(listItem);
}
