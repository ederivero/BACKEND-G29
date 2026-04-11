const crearCancha = document.getElementById('btnCrear')
const nombreCancha = document.getElementById('nombreCanchaInput')
const canchasData = document.getElementById('canchasData')

const BASE_URL='http://localhost:5000'

crearCancha.addEventListener('click',async (e)=>{
    e.preventDefault()


    const resultado = await fetch(`${BASE_URL}/canchas`,{
        method:'POST',
        body: JSON.stringify({nombre:nombreCancha.value}), 
        headers:{'Content-Type':'application/json'}
    })

    console.log(resultado)
    obtenerData()
})

const obtenerData = () => {
    canchasData.innerHTML= ``
    fetch(`${BASE_URL}/canchas`,{method:'GET'}).then((respuesta)=> 
        respuesta.json()
).then((data)=> {
    for (const cancha of data.content) {
        const fila = document.createElement('tr')
        fila.innerHTML=`
        <th scope="row">${cancha.id}</th>
        <td>${cancha.nombre}</td>
        `
        canchasData.appendChild(fila)
    } 
    
})
}

obtenerData()