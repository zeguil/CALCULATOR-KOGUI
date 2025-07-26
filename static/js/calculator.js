document.addEventListener('DOMContentLoaded', () => {
    const display = document.getElementById('display');
    const buttons = document.querySelectorAll('.calculator-grid button');
    const num1Input = document.getElementById('num1');
    const operadorInput = document.getElementById('operador');
    const num2Input = document.getElementById('num2');
    const calculatorForm = document.getElementById('calculatorForm');
    const submitButton = document.getElementById('submitButton');

    let currentInput = '';
    let previousInput = '';
    let operation = null;
    let resetDisplay = false;

    if (display.textContent === 'Erro') {
        display.classList.add('error');
    } else if (display.textContent !== '0' && display.textContent !== '') {
        display.classList.add('has-result');
        resetDisplay = true;
    }

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const value = button.dataset.value;

            if (value === 'C') {
                currentInput = '';
                previousInput = '';
                operation = null;
                display.textContent = '0';
                display.classList.remove('error', 'has-result');
                resetDisplay = false;
            } else if (value === 'negate') { 
                if (currentInput !== '') {
                    currentInput = String(parseFloat(currentInput) * -1);
                } else if (previousInput !== '') {
                    previousInput = String(parseFloat(previousInput) * -1);
                }
            } else if (value === 'percent') { 
                if (currentInput !== '') {
                    currentInput = String(parseFloat(currentInput) / 100);
                } else if (previousInput !== '') {
                    previousInput = String(parseFloat(previousInput) / 100);
                }
            } else if (['+', '-', '*', '/'].includes(value)) {
                if (currentInput === '' && previousInput === '') {
                    if (display.classList.contains('has-result')) {
                        previousInput = display.textContent;
                    } else {
                        return;
                    }
                } else if (currentInput !== '' && previousInput !== '' && operation !== null) {
                    performCalculation(false);
                } else if (currentInput !== '') {
                     previousInput = currentInput;
                }
                operation = value;
                currentInput = '';
                resetDisplay = true;
            } else if (value === '=') {
                if (currentInput === '' || previousInput === '' || operation === null) return;
                performCalculation(true);
                return;
            } else { 
                if (resetDisplay || display.classList.contains('has-result')) {
                    currentInput = value;
                    resetDisplay = false;
                    display.classList.remove('has-result', 'error');
                } else {
                    if (value === '.' && currentInput.includes('.')) return;
                    currentInput += value;
                }
            }
            updateDisplay();
        });
    });

    function updateDisplay() {
        if (operation && currentInput === '' && previousInput !== '') {
            display.textContent = `${previousInput} ${getOperatorSymbol(operation)}`;
        } else {
            display.textContent = currentInput || previousInput || '0';
        }
        display.classList.remove('error', 'has-result');
    }

    function getOperatorSymbol(op) {
        switch (op) {
            case '*': return '×';
            case '/': return '÷';
            case '+': return '+';
            case '-': return '-';
            default: return op;
        }
    }

    function performCalculation(resetForNewOperation) {
        num1Input.value = previousInput;
        operadorInput.value = operation;
        num2Input.value = currentInput;
        
        calculatorForm.submit();
    }
});