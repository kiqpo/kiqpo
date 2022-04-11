function snackbarShow(name,message){
    console.log(name)
    var snackbarContainer = document.getElementById(name);
    var data = {message};
    snackbarContainer.MaterialSnackbar.showSnackbar(data);

}