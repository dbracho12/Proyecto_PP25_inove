document.querySelector("#ingresar").onclick = async () => {
    const username = document.querySelector("#username").value;

    if(username == "" ) {   
        alert("Indique su usuario");
        return;
    }
    localStorage.blogUsername = username
    window.location.href = "/";
}

document.querySelector("#username").onkeypress = (e) => {
    // Si el usuario presionó "enter"
    // ejecutar la rutina del boton
    if (e.key === "Enter") {
        // Cancel the default action, if needed
        e.preventDefault();
        // Trigger the button element with a click
        document.querySelector("#ingresar").click();
      }   
};
