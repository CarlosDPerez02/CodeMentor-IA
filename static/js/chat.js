
const boton = document.getElementById("send-btn");    
const input = document.getElementById("message");
const chat = document.querySelector(".chat-messages");

boton.addEventListener("click", enviarMensaje);

    input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        enviarMensaje();
    }
});

async function enviarMensaje() {
    const mensaje = input.value.trim();
    if (mensaje === "") return;

    try {    
        chat.innerHTML += ` 
            <div class="message user">
                <p>${mensaje}</p>
                <span class="message-time">${obtenerHora()}</span>
            </div>    
        `;
        input.value = "";

        console.log(window.location.href);
        console.log("/preguntas/preguntas");

        const response = await fetch(`${window.location.origin}/preguntas/preguntas`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },


            body: JSON.stringify({
                pregunta: mensaje
            })
        });

        const data = await response.json();
        chat.innerHTML += `
            <div class="message ai">
                <div class="message-content">
                    ${marked.parse(data.respuesta)}
                </div>
                <span class="message-time">${obtenerHora()}</span>
            </div>
    `;
} catch (error) {
    console.log(error);
        chat.innerHTML += `
            <div class="message ai">
                <p>❌ Error al comunicarse con el servidor.</p>
                <span class="message-time">${obtenerHora()}</span>
            </div>
        `;
    }
    chat.scrollTop = chat.scrollHeight;
}


function obtenerHora() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("hora-inicial").textContent = obtenerHora();
});