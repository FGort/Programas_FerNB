import tkinter as tk
from tkinter import messagebox

# Valida que el numero pertenezca a la base dada
def IsValidNumber(value, base):
    digits = "0123456789ABCDEF"[:base]
    value = value.upper().lstrip('-')  
    return all(char in digits or char == '.' for char in value)

def ConvertNumber(value, fromBase, toBase):

    def ToDecimal(numStr, base):
        negative = numStr.startswith('-') # Verifica si el numero es negativo
        if negative:
            numStr = numStr[1:]
        parts = numStr.split('.')
        intPart = int(parts[0], base) # Conversion a base 10
        if len(parts) == 1:
            decimalValue = intPart
        else:
            fracPart = sum(int(digit, base) * base ** (-i) for i, digit in enumerate(parts[1], start=1))
            decimalValue = intPart + fracPart
        return -decimalValue if negative else decimalValue

    def FromDecimal(num, base):
        negative = num < 0
        if negative:
            num = -num
        digits = "0123456789ABCDEF"
        intPart = int(num)
        fracPart = num - intPart
        res = []
        if intPart == 0:
            res.append('0')
        while intPart > 0:
            res.append(digits[intPart % base])
            intPart //= base
        res.reverse()
        if fracPart > 0:
            res.append('.')
            count = 0
            while fracPart > 0 and count < 10:
                fracPart *= base
                digit = int(fracPart)
                res.append(digits[digit])
                fracPart -= digit
                count += 1
        return ('-' if negative else '') + ''.join(res)

    decimalNumber = ToDecimal(value, fromBase)
    result = FromDecimal(decimalNumber, toBase)
    return result

def Convertir():
    valor = entradaNumero.get()
    try:
        baseInicial = int(entradaBaseInicial.get())
        baseFinal = int(entradaBaseFinal.get())
        
        if not IsValidNumber(valor, baseInicial):
            messagebox.showerror("Error", "El número ingresado no pertenece a la base indicada.")
            return
        
        resultado = ConvertNumber(valor, baseInicial, baseFinal)
        etiquetaResultado.config(text=f"Resultado: {resultado}", fg="white", bg="#4CAF50")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores válidos.")

app = tk.Tk()
app.title("Conversor de Sistemas Numéricos")
app.geometry("400x350")
app.configure(bg="#333")

estiloLabel = {"fg": "white", "bg": "#333", "font": ("Arial", 12, "bold")}
estiloEntry = {"font": ("Arial", 12), "bg": "#555", "fg": "white", "insertbackground": "white"}
estiloBoton = {"font": ("Arial", 12, "bold"), "bg": "#008CBA", "fg": "white", "bd": 3}

tk.Label(app, text="Número a convertir:", **estiloLabel).pack(pady=5)
entradaNumero = tk.Entry(app, **estiloEntry)
entradaNumero.pack(pady=5)

tk.Label(app, text="Base inicial:", **estiloLabel).pack(pady=5)
entradaBaseInicial = tk.Entry(app, **estiloEntry)
entradaBaseInicial.pack(pady=5)

tk.Label(app, text="Base final:", **estiloLabel).pack(pady=5)
entradaBaseFinal = tk.Entry(app, **estiloEntry)
entradaBaseFinal.pack(pady=5)

tk.Button(app, text="Convertir", command=Convertir, **estiloBoton).pack(pady=10)

etiquetaResultado = tk.Label(app, text="Resultado:", **estiloLabel)
etiquetaResultado.pack(pady=10)

app.mainloop()