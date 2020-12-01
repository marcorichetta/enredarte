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


async function calcularPrecio() {

    let productosFiltrados = filtrarElementosBorrados()

    let productos = obtenerIDProductos(productosFiltrados);

    let cantidades = obtenerCantidades(productosFiltrados);

    // Merge de los arrays en uno solo para enviar al back
    let dataProductos = [ ...zip(productos, cantidades) ]
    
    let precios = await obtenerPrecio(dataProductos);

    mostrarPreciosProductos(precios, productosFiltrados);

    calcularPrecioPedido(precios);

}

/**
 * Selecciona los formsets creados
 * Filtra los borrados => display: "none"
 * 
 * Devuelve un [] de elementos HTML
 */
function filtrarElementosBorrados() {
    let formsetsProductos = document.querySelectorAll(".formset_row-productos_pedidos")

    let productosFiltrados = Array.from(formsetsProductos).filter(e => e.style.display !== "none")

    return productosFiltrados
}

/**
 * Toma un array de precios, reemplaza el valor en los elementos
 * y los hace visibles
 * @param {Object} listaPrecios Array con precios a mostrar
 */
function mostrarPreciosProductos(listaPrecios, elementos) {

    divPrecios = Array.from(elementos).map(elem => elem.querySelector("#div_precio"));
    boxPrecios = Array.from(elementos).map(elem => elem.querySelector("#precio_producto"));

    // Por cada "input" del precio
    calcularPrecioProducto(boxPrecios);

    // Mostrar los elementos que contienen el precio
    Array.from(divPrecios).map(elem => elem.removeAttribute("hidden"))


    function calcularPrecioProducto(boxPrecios) {
        Array.from(boxPrecios).map(elem => {

            // Sacar el id
            let key = elem.dataset.id;

            // Matchear array de precio - cantidad dentro del object precios 
            // con el Id del producto siendo iterado
            let arrPrecioQty = listaPrecios[key];

            // precio * cantidad
            let precioProducto = arrPrecioQty[0] * arrPrecioQty[1];

            elem.textContent = precioProducto;
        });
    }
}

/**
 * Multiplicar arrays [precio, cantidad] 
 * Sumar todos los valores
 * Asignar total
 * Sacar descuento
 * Mostrar valores en los precios
 * @param {Object} listaPrecios Objeto con id de productos { [ precio, cantidad ]}
 */
function calcularPrecioPedido(listaPrecios) {
    let totalPedido = Object.values(listaPrecios)
        .map(p => p[0] * p[1])
        .reduce((a, b) => a + b, 0);

        
    let porcentajeDescuento = document.querySelector("#id_descuento").value
    
    let precioDescuento = totalPedido * (parseInt(porcentajeDescuento)/100)
    
    let totalPedidoConDescuento = parseInt(totalPedido) - parseInt(precioDescuento)
    
    // Asignar precios y mostrar los elementos

    document.querySelector("#precio_pedido").textContent = totalPedido.toFixed(0);
    document.querySelector("#div_precio_pedido").removeAttribute("hidden");

    document.querySelector("#descuento_pedido").textContent = precioDescuento.toFixed(0);
    document.querySelector("#div_descuento_pedido").removeAttribute("hidden");

    document.querySelector("#precio_pedido_descuento").textContent = totalPedidoConDescuento.toFixed(0);
    document.querySelector("#div_precio_pedido_descuento").removeAttribute("hidden");
    
}

/**
 * 
 * Envía un array con los ids al backend,
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

/**
 * Obtiene el pk de los productos seleccionados
 * Asigna el atributo [data-id = pk] a los "input" de precio de cada producto
 * 
 * @param {Element[]} elementos Array de elementos HTML de los formsets
 * 
 * @returns {Array}
 */
function obtenerIDProductos(elementos) {

    // Seleccionar formsets
    // Filtrar los que no estén ocultos
    // Extraer ids de los elementos

    // let formsetsProductos = document.querySelectorAll(".formset_row-productos_pedidos")

    // let productosFiltrados = Array.from(formsetsProductos).filter(e => e.style.display !== "none")

    // Extraer ids de los elementos hijos de cada formset
    let idProductos = Array.from(elementos).map(elem => elem.querySelector(".producto").value);

    // Buscar los el box del precio de cada elemento seleccionado
    // Setearle un atributo data-id == al pk del producto seleccionado
    Array.from(elementos).map(prod => {
        let idProducto = prod.querySelector(".producto").value
        prod.querySelector("#precio_producto").dataset.id = parseInt(idProducto)
    });
    // Array.from(productosFiltrados).map(prod => {
    //     parentDivProducto = prod.parentElement.parentElement.parentElement // Que sucio me siento escribiendo esto
    //     parentDivProducto.querySelector("#precio_producto").dataset.id = prod.value
    // });

    return idProductos
}

/**
 * Obtiene la cantidad de los productos seleccionados
 * 
 * @param {Element[]} elementos Array de elementos HTML de los formsets
 * 
 * @returns {Array}
 */
function obtenerCantidades(elementos) {
    
    // let formsetsProductos = document.querySelectorAll(".formset_row-productos_pedidos")

    // let productosFiltrados = Array.from(formsetsProductos).filter(e => e.style.display !== "none")
    
    // Extraer ids de los elementos hijos de cada formset
    let cantidadProductos = Array.from(elementos).map(elem => elem.querySelector(".cantidad").value);

    // let cantidadNodeList = document.querySelectorAll(".cantidad");

    // let cantidadProductos = Array.from(cantidadNodeList).map(cantidad => parseInt(cantidad.value));

    return cantidadProductos
}
