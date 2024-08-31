
document.addEventListener('DOMContentLoaded', function() {
    const menuLinks = document.querySelectorAll('#menu a');
    const pages = document.querySelectorAll('.page');
    const loginLink = document.getElementById('login-link');
    const logoutLink = document.getElementById('logout-link');

    menuLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const pageId = this.getAttribute('data-page');

            menuLinks.forEach(l => l.classList.remove('active'));
            pages.forEach(p => p.classList.remove('active'));

            this.classList.add('active');
            document.getElementById(pageId).classList.add('active');
        });
    });

    // Activate the first page by default
    menuLinks[0].click();

    // Simulating login/logout functionality
    loginLink.addEventListener('click', function(e) {
        e.preventDefault();
        loginLink.style.display = 'none';
        logoutLink.style.display = 'inline';
    });

    logoutLink.addEventListener('click', function(e) {
        e.preventDefault();
        logoutLink.style.display = 'none';
        loginLink.style.display = 'inline';
    });
});
