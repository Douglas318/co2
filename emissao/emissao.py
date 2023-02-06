def calcula_emissao(tipo_de_combustivel, distancia):
    if tipo_de_combustivel == 'diesel':
        carbono = 35
    elif tipo_de_combustivel == 'gasolina':
        carbono = 30
    else:
        raise ValueError("Tipo de combustivel não reconhecido")

    eficiencia = 20
    co2_emissao = carbono * eficiencia * distancia / 1000

    return {
        'tipo_de_combustivel': tipo_de_combustivel,
        'distancia': distancia,
        'eficiencia': eficiencia,
        'co2_emissao': co2_emissao
    }
