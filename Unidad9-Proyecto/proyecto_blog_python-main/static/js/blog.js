
const username = localStorage.blogUsername? localStorage.blogUsername : ""

if(username == "") {
    window.location.href = "/login";
}

document.querySelector("#username").innerHTML = `¡Hola ${username}!`;

document.querySelector("#salir").onclick = () => {
    localStorage.blogUsername = "";
    window.location.href = "/login";
}

document.querySelector("#publicar").onclick = async () => {
    let formData = new FormData();
    const titulo = document.querySelector("#titulo").value;
    const texto = document.querySelector("#texto").value;
    const url = document.querySelector("#publicar").getAttribute("path");
    
    formData.append("titulo", titulo);
    formData.append("texto", texto);
    
    fetch(`${url}/${username}`, {
        method: 'POST',
        body: formData,
    })
    .then(response => window.location.reload(true))
    .catch(error => console.error('Error:', error))
}


const url = document.querySelector("#publicar").getAttribute("path");

fetch(`${url}/${username}`)
    .then(response => response.json())
    .then(data => data)
    .then(posts => {
        let accumulator = ""
        
        posts.forEach(post => {
            accumulator += 
                `
                <div>
                    <p id="titulo">${post.titulo}</p>
                    <p id="texto">${post.texto}</p>
                    <hr>
                </div>
                `
        });
        const section = document.querySelector("#posteos");
        section.innerHTML = accumulator;
    })

