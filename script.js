let currentInput = "";
let operator = "";
let display = document.getElementById("display");

function appendNumber(number) {
    currentInput += number;
    updateDisplay();
}

function setOperator(op) {
    operator = op;
    currentInput += " " + op + " ";
    updateDisplay();
}

function clearDisplay() {
    currentInput = "";
    operator = "";
    updateDisplay();
}

function calculate() {
    try {
        let result = Function('"use strict";return (' + currentInput + ')')();
        currentInput = result.toString();
        updateDisplay();
    } catch (error) {
        currentInput = "Error";
        updateDisplay();
    }
}

function updateDisplay() {
    display.value = currentInput;
}

function updateDisplay() {
    document.getElementById("display").value = currentInput;
}
