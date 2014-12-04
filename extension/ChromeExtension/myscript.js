  chrome.storage.sync.get({
    favoriteColor: 'red',
    likesColor: true,
    box: 'testfcn,1;'
  }, function(items, test) {
     scr = document.createElement('SCRIPT');
     scr.setAttribute('type', 'text/javascript');
     scr.innerText = "/*LEZ"+items.box+" */";
     head = document.getElementsByTagName('head')[0];
     head.insertBefore(scr, head.childNodes[0]);
  });
