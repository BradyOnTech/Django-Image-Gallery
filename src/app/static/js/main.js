const nav = document.querySelector('.main-nav');

const topOfNav = nav.offsetTop; //tells us where the nav bar is on page load;
//figure out where the top of the nav bar is on page load and 2.) then when we scroll we need to figure out how far we have scrolled.3.)as soon as we have hit the point where we have scrolled farther than the top of the nav bar, the event listener will be triggered causing the fixNav function to run.
function fixNav() {
  //saying that once the window.scrollY and the top of the nav bar are equal or you have scrolled past the nav, scrollY is > now, the classList fixed-nav will be added; 
  if(window.scrollY >= topOfNav) {
    document.body.style.paddingTop = nav.offsetHeight + 'px';
    document.body.classList.add('fixed-nav');
  } else {
    document.body.style.paddingTop = 0;
    document.body.classList.remove('fixed-nav');
  }
}

window.addEventListener('scroll', fixNav);