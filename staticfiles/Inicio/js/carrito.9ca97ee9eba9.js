// static/js/carrito.js

document.addEventListener("DOMContentLoaded", function () {
    const botonesAgregar = document.querySelectorAll(".btn-agregar");
    const botonesRestar = document.querySelectorAll(".btn-restar");
    const botonesEliminar = document.querySelectorAll(".btn-eliminar");

    botonesAgregar.forEach(boton => {
        boton.addEventListener("click", () => {
            alert("Producto agregado al carrito.");
        });
    });

    botonesRestar.forEach(boton => {
        boton.addEventListener("click", () => {
            alert("Cantidad reducida.");
        });
    });

    botonesEliminar.forEach(boton => {
        boton.addEventListener("click", () => {
            alert("Producto eliminado del carrito.");
        });
    });
});