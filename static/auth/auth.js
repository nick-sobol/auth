function redirect(redirect_route) {
    window.history.pushState({}, "", redirect_route);
    window.location.reload();
    console.log('success');
}