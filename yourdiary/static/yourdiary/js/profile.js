function switchBetween(links, forms) {
  for (var i = 0; i < links.length; i++) {
    if (links[i].firstChild !== null) {
      links[i].addEventListener('click', function(e) {
        for (var i=0; i < forms.length; i++) {
          if (forms[i].firstChild !== null) {
            forms[i].style.display = 'none';
          }
        }
        document.getElementById(e.target.getAttribute("data-container")).style.display = "block";
        for (var j = 0; j < links.length; j++) {
            if (links[j].firstChild !== null) {
                links[j].className = "nav-item profile-item";
            }
        }
        e.target.className = "nav-item profile-item profile-item__active";
      });
    }
  }
}

var section = document.getElementById("sections").childNodes;
var link = document.getElementById("switchBox").childNodes;

switchBetween(link, section);

var coll = document.getElementsByClassName("collapsible");
var chboxes = document.getElementsByClassName("checkbox-task");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle('active-collapse');
    var content = this.previousElementSibling;
    var taskText = content.parentNode;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
    if (taskText.style.height){
      taskText.style.height = null;
      taskText.style.marginTop = null;
    } else {
      taskText.style.height = content.scrollHeight * 2.2 + "px";
      taskText.style.marginTop = content.scrollHeight * 0.3 + "px";
    }

  });
}

for (i = 0; i < chboxes.length; i++) {
  chboxes[i].addEventListener('click', function() {
    this.dataset.checkedCheckbox *= -1;
  })
}
