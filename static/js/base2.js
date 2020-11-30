// Utility functions para calcular precio del pedido

/**
 *
 * @param {Array} arr1 Array con precio de productos
 * @param {Array} arr2 Array con cantidad de productos
 * @param {int} i Contador
 *
 * Uso: [ ...zip([1,2], [3,4]) ] => [ [1,3], [2,4] ]
 */
function* zip(arr1, arr2, i = 0) {
    while (arr1[i])
        yield [arr1[i], arr2[i++]];
}


async function calcularPrecio() {
    let productos = obtenerIDProductos()

    let precios = obtenerPrecio(productos)

    let cantidades = obtenerCantidades()

    // Combinar precio y cantidad de cada producto
    let data = [ ...zip(await precios, cantidades) ]
    
    // Multiplicar precios con cantidades y devolverlos a un array con los precios finales
    let listaPrecios = data.map(p => p[0] * p[1])

    mostrarPrecios(listaPrecios)

}

/**
 * Toma un array de precios, reemplaza el valor en los elementos
 * y los hace visibles
 * @param {Array} listaPrecios Array con precios a mostrar
 */
function mostrarPrecios(listaPrecios) {
    divPrecios = document.querySelectorAll("#div_precio")
    boxPrecios = document.querySelectorAll("#precio_producto")

    function showHTML(elem, index) {
        elem.querySelector("#precio_producto").textContent = listaPrecios[index]
        elem.removeAttribute("hidden")
    }

    // Aplicar a cada elemento de divPrecios la función showHTML
    divPrecios.forEach(showHTML)

    // Sumar y mostrar total
    let totalPedido = listaPrecios.reduce( (acc, precio) => acc + precio, 0)

    document.querySelector("#div_precio_pedido").removeAttribute("hidden")
    document.querySelector("#precio_pedido").textContent = totalPedido

}

/**
 * 
 * Esta función envía un array con los ids al backend,
 * donde se calculan los precio de los productos.
 * 
 * Devuelve un Json
 * @param {Array} arrayProductos Array con los IDs de los productos seleccionados
 */
async function obtenerPrecio(arrayProductos) {
    let url = "/productos/precio/"

    const csrftoken = $("[name=csrfmiddlewaretoken]").val()

    try {
        let response = await fetch(
            url,
            {
                
                headers: {
                    "X-CSRFToken": csrftoken,
                    'Accept': 'application/json',
                    "Content-Type": "application/json",
                },
                method: "POST",
                body: JSON.stringify({ 'id_productos': arrayProductos })
            },
        )
        
        return response.json()
        
    } catch (error) {
        console.log(error)
    }
}

function obtenerIDProductos() {

    let productosNodeList = document.querySelectorAll(".producto");

    let idProductos = Array.from(productosNodeList).map(prod => prod.value);

    return idProductos
}


function obtenerCantidades() {
    let cantidadNodeList = document.querySelectorAll(".cantidad");

    let cantidadProductos = Array.from(cantidadNodeList).map(cantidad => parseInt(cantidad.value));

    return cantidadProductos
}
