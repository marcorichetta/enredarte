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

    let cantidades = obtenerCantidades()

    // Merge de los arrays en uno solo
    let dataProductos = [ ...zip(productos, cantidades) ]
    
    let precios = await obtenerPrecio(dataProductos)

    mostrarPrecios(precios)
}

/**
 * Toma un array de precios, reemplaza el valor en los elementos
 * y los hace visibles
 * @param {Object} listaPrecios Array con precios a mostrar
 */
function mostrarPrecios(listaPrecios) {
    divPrecios = document.querySelectorAll("#div_precio")
    boxPrecios = document.querySelectorAll("#precio_producto")


    // Por cada "input" del precio
    Array.from(boxPrecios).map(elem => {
        
        // Sacar el id
        let key = elem.dataset.id

        // Matchear array de precio - cantidad dentro del object precios 
        // con el Id del producto siendo iterado
        let arrPrecioQty = listaPrecios[key]

        // precio * cantidad
        let precioProducto = arrPrecioQty[0] * arrPrecioQty[1]

        elem.textContent = precioProducto
    })

    // Mostrar los elementos que contienen el precio
    Array.from(divPrecios).map(elem => elem.removeAttribute("hidden"))

    // Multiplicar arrays [precio, cantidad] 
    // Sumar todos los valores
    // Asignar total
    let totalPedido = Object.values(listaPrecios)
                            .map(p => p[0] * p[1])
                            .reduce( (a, b) => a + b, 0)

    document.querySelector("#div_precio_pedido").removeAttribute("hidden")
    document.querySelector("#precio_pedido").textContent = totalPedido.toFixed(0)

}

/**
 * 
 * Esta función envía un array con los ids al backend,
 * donde se calculan los precios de los productos.
 * 
 * Devuelve un Json
 * @param {Array} dataProductos Array con los IDs de los productos seleccionados
 */
async function obtenerPrecio(dataProductos) {
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
                body: JSON.stringify({ 'dataProductos': dataProductos })
            },
        )
        
        return response.json()
        
    } catch (error) {
        console.log(`Hubo un error al enviar los datos: ${error}`)
    }
}

function obtenerIDProductos() {

    let productosNodeList = document.querySelectorAll(".producto");

    let idProductos = Array.from(productosNodeList).map(prod => prod.value);

    // Buscar los el box del precio de cada elemento seleccionado
    // Setearle un atributo data-id == al pk del producto seleccionado
    Array.from(productosNodeList).map(prod => {
        parentDivProducto = prod.parentElement.parentElement.parentElement // Que sucio me siento escribiendo esto
        boxPrecio = parentDivProducto.querySelector("#precio_producto").dataset.id = prod.value
    });

    return idProductos
}


function obtenerCantidades() {
    let cantidadNodeList = document.querySelectorAll(".cantidad");

    let cantidadProductos = Array.from(cantidadNodeList).map(cantidad => parseInt(cantidad.value));

    return cantidadProductos
}
