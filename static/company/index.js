function mostrarInteresados(postId) {
    fetch('/get_aspirants', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `post_id=${postId}`
    })
    .then(response => response.json())
    .then(data => {
        // Lógica para mostrar los aspirantes en el panel derecho
        const detalle = document.getElementById('detalle-oferta');
        detalle.innerHTML = ''; // Limpiar contenido anterior

        if (data.error) {
            detalle.innerHTML = `<p class="text-red-500">${data.error}</p>`;
            return;
        }

        if (data.length === 0) {
            detalle.innerHTML = '<p class="text-gray-600">No hay aspirantes para esta oferta.</p>';
            return;
        }

        // Construir lista de aspirantes
        const list = document.createElement('ul');
        list.className = 'space-y-4';

        data.forEach(aspirant => {
            const item = document.createElement('li');
            item.className = 'bg-white p-4 rounded-lg shadow';
            item.innerHTML = `
                <h3 class="font-bold">${aspirant.name}</h3>
                <p class="text-gray-600">${aspirant.email}</p>
                <button class="mt-2 bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600">
                    Ver perfil
                </button>
                <button onclick="deny_request(${aspirant.id} , ${postId})" class="mt-2 bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600">
                    Denegar Solicitud
                </button>
            `;
            list.appendChild(item);
        });

        detalle.appendChild(list);
    })
    .catch(error => console.error('Error:', error));
}

function openModal() {
    fetch('create_vacant')
        .then(res => {
            if (!res.ok) throw new Error("Error al cargar el formulario");
            document.getElementById("createVacantModal").classList.remove("hidden");})
        .catch(error => alert(error));
}

function closeModal() {
    document.getElementById("createVacantModal").classList.add("hidden");
}

function deny_request(applicant_id, post_id) {
    fetch('/deny_applicant', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `applicant_id=${applicant_id}&post_id=${post_id}` }) // Envía ambos IDs    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();  // Solo intenta parsear JSON si la respuesta es OK
    })
    .then(data => console.log(data))
    .catch(error => {
        console.error('Error:', error);
        alert("Error al procesar la solicitud");
    });
}
