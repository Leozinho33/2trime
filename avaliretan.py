def retangulo(tipo_retorno, largura, altura):
    r = 0
    if tipo_retorno == "area":
        r = largura * altura
    elif tipo_retorno == "perimetro":
        r = 2* (largura+altura)
    return r 
    
def circulo (tipo_retorno, raio):
    r = 0
    if tipo_retorno.lower() == "area":
        r = 3.14 * raio ** 2
    elif tipo_retorno.lower() == "circuferencia":
        r = int( 2 * raio * 3.14)
    return r 
    
def verificar_resultados(largura, altura, raio):
    print(circulo ("area", raio))
    print(circulo ("circuferencia", raio))
    print(retangulo("area", largura, altura))
    print(retangulo("perimetro", largura, altura))

verificar_resultados (20, 30, 5)
