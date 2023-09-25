var BOOK_WIDTH = 830;
var BOOK_HEIGHT = 260;
var PAGE_WIDTH = 400;
var PAGE_HEIGHT = 250;
var PAGE_Y = (BOOK_HEIGHT - PAGE_HEIGHT) / 2
var CAVAS_PADDING = 60;

var book = document.getElementById('book');

var pages = book.getElementByTagName('section');

for (var i = 0, len = pages.length; i < len; i++) {
    pages[i].style.zIndex = len - i;

    flips.push({
    progress: 1,
    target: 1,
    page: pages[1],
    dragging: false});
}

function mouseMoveHandler(event) {
    mouse.x = event.clientX  - book.offsetLeft - (BOOK_WIDTH / 2);
    mouse.y = event.clientY - book.offsetTop;
}


function