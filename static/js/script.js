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

function applySettings() {
    const rotor1 = document.getElementById("rotor1").value;
    const rotor2 = document.getElementById("rotor2").value;
    const rotor3 = document.getElementById("rotor3").value;

    const start1 = document.getElementById("start1").value.toUpperCase() || "A";
    const start2 = document.getElementById("start2").value.toUpperCase() || "A";
    const start3 = document.getElementById("start3").value.toUpperCase() || "A";

    const reflector = document.getElementById("reflector").value;
    
    if (!/^[A-Z]$/.test(start1) || !/^[A-Z]$/.test(start2) || !/^[A-Z]$/.test(start3)) {
        alert("Rotor positions must be a single letter (A-Z)!");
        return;
    }

    document.getElementById("rotor1-label").textContent = start1;
    document.getElementById("rotor2-label").textContent = start2;
    document.getElementById("rotor3-label").textContent = start3;

    fetch('/set_enigma', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            rotor1, start1,
            rotor2, start2,
            rotor3, start3,
            reflector
        })
    }).then(response => response.json()).then(data => {
        console.log("Settings saved:", data);
    }).catch(error => console.error("Error:", error));
}

function pressKey(letter) {
    document.querySelectorAll(".lamp").forEach(lamp => lamp.classList.remove("active"));

    fetch("/decrypt", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ letter })
    })
    .then(response => response.json())
    .then(data => {
        if (data.decrypted) {
            const lamp = document.getElementById(`L-${data.decrypted}`);
            if (lamp) {
                lamp.classList.add("active");
                setTimeout(() => lamp.classList.remove("active"), 500);
            }
        }
    })
    .catch(error => console.error("Error:", error));
}


