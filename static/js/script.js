document.addEventListener("DOMContentLoaded", () => {
    const lampboard = document.querySelector(".lampboard");
    const keyboard = document.querySelector(".keyboard");
    const plugboard = document.querySelector(".plugboard");

    const enigmaLayout = [
        "QWERTZUIO",  
        "ASDFGHJK",   
        "PYXCVBNML"  
    ];

    function createRow(container, row) {
        const rowDiv = document.createElement("div");
        rowDiv.classList.add("row");
    
        row.split("").forEach(letter => {
            if (letter !== " ") {
                if (container === plugboard) {
                    const plugContainer = document.createElement("div");
                    plugContainer.classList.add("plug-container");
    
                    const label = document.createElement("span");
                    label.classList.add("plug-label");
                    label.textContent = letter;
    
                    const plug = document.createElement("div");
                    plug.classList.add("plug");
                    plug.id = `P-${letter}`;
                    plug.onclick = () => togglePlug(letter);
    
                    plugContainer.appendChild(label);
                    plugContainer.appendChild(plug);
                    rowDiv.appendChild(plugContainer);
                } else {
                    const element = document.createElement("div");
                    element.classList.add(container === lampboard ? "lamp" : "key");
                    element.textContent = letter;
                    element.id = container === lampboard ? `L-${letter}` : "";
                    if (container === keyboard) element.onclick = () => pressKey(letter);
                    rowDiv.appendChild(element);
                }
            } else {
                const spacer = document.createElement("div");
                spacer.classList.add("spacer");
                rowDiv.appendChild(spacer);
            }
        });
    
        container.appendChild(rowDiv);
    }
    

    enigmaLayout.forEach(row => createRow(lampboard, row));
    enigmaLayout.forEach(row => createRow(keyboard, row));
    enigmaLayout.forEach(row => createRow(plugboard, row));
});

document.addEventListener("keydown", (event) => {
    const letter = event.key.toUpperCase();
    const keyElement = [...document.querySelectorAll(".key")].find(el => el.textContent === letter);

    if (keyElement) {
        keyElement.classList.add("active");
        keyElement.click();

        setTimeout(() => keyElement.classList.remove("active"), 500);
    }
});
function pressKey(letter) {
    document.querySelectorAll(".lamp").forEach(lamp => lamp.classList.remove("active"));
    const lamp = document.getElementById(`L-${letter}`);
    if (lamp) {
        lamp.classList.add("active");
        setTimeout(() => {
            lamp.classList.remove("active");
        }, 500);
    }
}

