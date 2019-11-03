document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#localidad-form').addEventListener('submit', (e) => {
        e.preventDefault()

        let token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'POST',
            url: '/localidad/new/',
            data: {
                csrfmiddlewaretoken: token,
                cod_postal: $('#InputCodPostal').val(),
                localidad: $('#InputLocalidad').val(),
                provincia: $('#InputProvincia').val(),
            },
            dataType: 'json',
            success: (nuevaLocalidad) => {
                    window.alert('Se creó la nueva localidad con éxito');

                    // Esconder modal
                    $('#exampleModal').modal('hide');

                    // Seleccionar select del formulario de cliente
                    localidadSelect = document.getElementById('id_localidad');

                    // Crear una nueva opción para ese select
                    localidadSelect.options.add(
                        new Option(
                            nuevaLocalidad.localidad,
                            nuevaLocalidad.cod_postal
                        )
                    )

                    // Actualizar el select con la opción creada
                    localidadSelect.value = nuevaLocalidad.cod_postal

            }
        })
    })

})