/*
Animate a container `el` by taking its first child (given by `selector') using a
slideUp animation for `animate` milliseconds. After the animation, the selected item
is removed from DOM and appended to `el`.
 */
function animateSlideUp(el, selector, animate) {
    var item = el.children(selector).first();
    item.slideUp(animate, function() {
        item.remove();
        el.append(item);
        item.fadeIn(animate);
    });
}
