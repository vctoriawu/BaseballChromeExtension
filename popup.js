function myFunction() {
  return Math.floor((Math.random() * 60) + 1);
}

imgs = myFunction();

document.documentElement.style.backgroundImage = 'url(baseballimg' + imgs + '.png)';
