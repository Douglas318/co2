from flask import Flask, request, jsonify
from emissao import calcula_emissao


def calculadora_co2():
    request_data = request.get_json()
    tipo_de_combustivel = request_data['tipo_de_combustivel']
    distancia = request_data['distancia']

    emissiao_data = calcula_emissao(tipo_de_combustivel, distancia)
    emissao = f"""A quantidade de co² emitida é de: {emissiao_data['co2_emissao']:.2f}g"""

    return jsonify({"message": emissao})


def register_routes(app):
    app.route('/co2', methods=['POST'])(calculadora_co2)
