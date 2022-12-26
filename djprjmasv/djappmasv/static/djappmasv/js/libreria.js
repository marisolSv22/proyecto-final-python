var bttnCerrar = document.getElementById("cerrar");
var dlg_libro = document.getElementById("libros");

bttnCerrar.addEventListener('click', function (event) {
    event.preventDefault();
    dlg_libro.close();
});