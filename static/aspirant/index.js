function mostrarDetalle(id_offer, title, content) {
    document.getElementById("detalle-oferta").innerHTML = `
        <div class="text-gray-700">
            <h2 class="text-2xl font-bold mb-4">${title}</h2>
            <p class="text-sm mb-2"><strong>ID:</strong> ${id_offer}</p>
            <p class="text-base mb-6">${content}</p>
            <button 
                class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition duration-200"
                onclick="sendRequest(${id_offer} )">
                📩 Enviar Solicitud de Puesto
            </button>
        </div>
    `;
}

function sendRequest(id_offer){
    fetch('accept_offer', {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({id_offer: id_offer})
    })
        .then(rs => {
        if (!rs.ok) throw new Error("Error al enviar la solicitud");
        return rs.json();
        })
        .then(data => {
            console.log(data);
            alert("✅ Solicitud enviada con éxito");
        })
        .catch(error => {
            console.error(error);
            alert("❌ Ocurrió un error al enviar la solicitud");
        });
}