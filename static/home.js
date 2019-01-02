function logout(request_route, redirect_route) {

    fetch(request_route, {
        method: 'post',
    })
        .then(response => {
            window.history.pushState({}, "", redirect_route);
            window.location.reload();
        })
        .catch(error => {
            alert(error);
        });
}