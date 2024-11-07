const redirectToTweetIndex = function(){
    const url = 
    document.getElementById('redirectButton').getAttribute('data-url')
    console.log(url)
    window.location.href = url
}



document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('#mobile-menu');
    const profileMenuButton = document.querySelector('.profile-menu-button');
    const profileDropdown = document.querySelector('.profile-dropdown');

    mobileMenuButton.addEventListener('click', () => {
      const expanded = mobileMenuButton.getAttribute('aria-expanded') === 'true' || false;
      mobileMenuButton.setAttribute('aria-expanded', !expanded);
      mobileMenu.classList.toggle('hidden');
      mobileMenuButton.querySelector('svg').classList.toggle('hidden');
    });

    profileMenuButton.addEventListener('click', () => {
      profileDropdown.classList.toggle('hidden');
    });

    document.addEventListener('click', (event) => {
      if (!profileMenuButton.contains(event.target) && !profileDropdown.contains(event.target)) {
        profileDropdown.classList.add('hidden');
      }
    });
  });