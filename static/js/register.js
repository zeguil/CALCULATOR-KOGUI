document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.errorlist').forEach(errorList => {
        errorList.classList.add('error-list');
        errorList.classList.remove('errorlist');
    });
});