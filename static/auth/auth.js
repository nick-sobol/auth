function onUserSubmit(request_route, redirect_route, form) {

    fetch(request_route, {
        method: 'post',
        body: form,
    }).then(response => {
        window.history.pushState({}, "", redirect_route);
        window.location.reload();
        console.log('success');
    }).catch(error => {
        alert(error);
    });
}