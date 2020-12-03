
'use strict';
let inject_btn = document.getElementById('inject');

chrome.storage.sync.get('color', function(data) {
  inject_btn.style.backgroundColor = data.color;
  inject_btn.setAttribute('value', data.color);
});

var script = `
    // do stuff
    console.log(document.getElementsByTagName("input"));
    var input = document.getElementsByTagName("input").item(0);
    console.log(input);
    if (input) {
        //do something
        if (input.getAttribute('data-event-fileinput') !== 'true') {
            input.addEventListener('change', function() {
                alert("Uh oh, you uploaded an uncloaked image");
            });
            input.setAttribute('data-event-fileinput', 'true');
        }
        else {
            console.log("Already have this listener attached");
        }
    }
`;

inject_btn.onclick = function(element) {
  let color = element.target.value;
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.executeScript(
        tabs[0].id,
        {code: script});
  });
};
