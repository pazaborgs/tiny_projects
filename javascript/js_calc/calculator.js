var display_box = document.getElementById("calculation")

function UserClickBtn(input) {
    var lastinput = display_box.value;
    var newinput = lastinput + input;
    display_box.value = newinput;
}

function CalculateValue() {
    var result = eval(display_box.value)
    console.log(result)
}

function ClearData() {
    display_box.value = ""
}

