document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('form input').forEach(input => {
        const type = input.getAttribute('type');
        if (type === 'text' || type === 'password' || type === 'email' || type === 'number') {
            input.classList.add('form-control');
        }
    });
});