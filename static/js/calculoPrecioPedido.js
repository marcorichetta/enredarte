// Funciones para calcular el precio del pedido

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

// Como no vas a tener una función para hacer sleep JS
const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
}


async function calcularPrecio() {

    const spinner = document.getElementById("spinner");

    spinner.removeAttribute("hidden");

    let productosFiltrados = filtrarFormsetsBorrados()

    let productos = obtenerIDProductos(productosFiltrados);

    let cantidades = obtenerCantidades(productosFiltrados);

    // Merge de los arrays en uno solo para enviar al back
    let datosAEnviar = [ ...zip(productos, cantidades) ]
    
    let datosProductos = await enviarDatosAjax(datosAEnviar);

    await sleep(500)

    crearHTMLProductos(datosProductos)

    spinner.setAttribute('hidden', '');

    return true
}

/**
 * Selecciona los formsets creados
 * Filtra los borrados => `display: "none"`
 * 
 * Devuelve un `Array` de formsets
 */
function filtrarFormsetsBorrados() {
    let formsetsProductos = document.querySelectorAll(".formset_row-productos_pedidos")

    let productosFiltrados = Array.from(formsetsProductos).filter(e => e.style.display !== "none")

    return productosFiltrados
}

/**
 * Obtiene el pk de los productos seleccionados
 * 
 * @param {Element[]} formsets Array de elementos HTML de los formsets
 * 
 * @returns {Array}
 */
function obtenerIDProductos(formsets) {
    // Extraer ids de los elementos hijos de cada formset
    const idProductos = Array.from(formsets).map(elem => elem.querySelector(".producto").value);

    return idProductos;
}

/**
 * Obtiene la cantidad de los productos seleccionados
 * 
 * @param {Element[]} elementos Array de elementos HTML de los formsets
 * 
 * @returns {Array}
 */
function obtenerCantidades(elementos) {
    // Extraer ids de los elementos hijos de cada formset
    const cantidades = Array.from(elementos).map(elem => elem.querySelector(".cantidad").value);

    return cantidades
}

/**
 * 
 * Envía un array con los ids al backend,
 * donde se calculan los precios de los productos.
 * 
 * Devuelve un Json
 * @param {Array} datosAEnviar Array con los IDs y las cantidades de los productos seleccionados
 */
async function enviarDatosAjax(datosAEnviar) {
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
                body: JSON.stringify({ 'dataProductos': datosAEnviar })
            },
        )
        
        return response.json()
        
    } catch (error) {
        console.log(`Hubo un error al enviar los datos: ${error}`)
    }
}

/**
 * Crea los elementos HTML para los productos
 * y los anexa al listado.
 * @param {Object} precios Objeto que contiene los precios y cantidades de los productos
 * @param {Array} formsets Productos a mostrar en el listado de precios
 */
function crearHTMLProductos(datosProductos) {

    // Crear nodos para productos
    const productosNuevos = Object.entries(datosProductos).map(producto => {

        const { nombre, precio, cantidad } = producto[1]

        let precioTotal = precio * cantidad

        let nuevoProducto = document.createElement("li")
        nuevoProducto.id = "li-producto"
        nuevoProducto.classList = "list-group-item d-flex justify-content-between"

        nuevoProducto.innerHTML = 
        `<div>
                <h6 class="my-0" id="nombre_producto">${nombre}</h6>
            </div>
            <span class="text-muted" id="precio_producto">$ ${precioTotal.toFixed()}</span>
        `

        return nuevoProducto
    })
    
    
    // Calculo de precios

    let porcentajeDescuento = document.querySelector("#id_descuento").value

    let totalPedido = Object.entries(datosProductos).map(p => {
        const { precio, cantidad } = p[1]
      return precio * cantidad
    }).reduce((a, b) => a + b, 0)

    let precioDescuento = totalPedido * (parseInt(porcentajeDescuento)/100)
    
    let totalPedidoConDescuento = parseInt(totalPedido) - parseInt(precioDescuento)

    // Crear nodo para descuento
    let liDescuento = document.createElement("li")
    liDescuento.id = "li-descuento"
    liDescuento.classList = "list-group-item d-flex justify-content-between bg-light"

    liDescuento.innerHTML = 
    `<div class="text-success">
        <h6 class="my-0">Descuento</h6>
    </div>
    <span class="text-success">-$ ${precioDescuento.toFixed()}</span>
    `

    // Crear nodo para precio total
    let liTotalPedido = document.createElement("li")
    liTotalPedido.id = "li-total-pedido"
    liTotalPedido.classList = "list-group-item d-flex justify-content-between"

    liTotalPedido.innerHTML = 
    `<span>Total</span>
    <strong>$ ${totalPedidoConDescuento.toFixed()}</strong>
    </li>`

    // Seleccionar elemento padre
    const listadoProductos = document.querySelector("#listado-productos")

    // Reemplazar listado anterior con nuevo listado
    listadoProductos.replaceChildren(...productosNuevos, liDescuento, liTotalPedido);

}
