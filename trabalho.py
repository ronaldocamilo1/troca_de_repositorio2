def calcular(operando1, operando2, operacao):
    try:
        operando1 = float(operando1)
        operando2 = float(operando2)
        if operacao == "soma":
            return operando1 + operando2
        elif operacao == "subtracao":
            return operando1 - operando2
        elif operacao == "multiplicacao":
            return operando1 * operando2
        elif operacao == "divisao":
            if operando2 != 0:
                return operando1 / operando2
            else:
                return "Erro: Divisão por zero"
        else:
            return "Operação inválida"
    except ValueError:
        return "Erro: Valores inválidos"

# Rota para exibir o formulário da calculadora
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        operando1 = request.form["operando1"]
        operando2 = request.form["operando2"]
        operacao = request.form["operacao"]
        resultado = calcular(operando1, operando2, operacao)
    return render_template("calculator.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)