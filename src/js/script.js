function showLogsWithTag(tag) {
  var items = document.querySelectorAll('.item');
  items.forEach(function(item, key) {
    var itemTags = item.querySelectorAll('.item-tags .tag');
    var flag = 0;
    itemTags.forEach(function(tagElem, key) {
      if (
        tagElem.innerHTML.toLowerCase() === tag.toLowerCase() ||
        tagElem.innerHTML.toLowerCase().indexOf(tag.toLowerCase()) !== -1
      ) {
        flag++;
      }
    });
    if (flag === 0) {
      item.style.display = 'none';
    } else {
      item.style.display = 'block';
    }
  });
}

function tagClickHandler(event) {
  var tag = event.target.innerHTML;
  showLogsWithTag(tag);
}

function searchFormHandler(event) {
  event.preventDefault();
  var tag = document.querySelector('#query-tag').value;
  console.log(tag);
  showLogsWithTag(tag);
}

window.onload = function() {
  var tags = document.querySelectorAll('.item-tags .tag')
  tags.forEach(function(tag, key) {
    tag.addEventListener('click', tagClickHandler);
  });
  document.getElementById('search-form').addEventListener('submit', searchFormHandler);
}