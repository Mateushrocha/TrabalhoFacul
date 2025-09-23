from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import datetime as dt

app = Flask(__name__)
CORS(app) # Habilita o CORS para permitir requisições do seu arquivo HTML

# Nome do arquivo do banco de dados
ARQUIVO_BD = "Banco de dados.json"

# Função para carregar o banco de dados
def carregar_bd():
    if os.path.exists(ARQUIVO_BD):
        try:
            with open(ARQUIVO_BD, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except (IOError, json.JSONDecodeError):
            return [] # Retorna uma lista vazia em caso de erro de leitura ou arquivo vazio
    return []

# Função para salvar o banco de dados
def salvar_bd(data):
    with open(ARQUIVO_BD, "w", encoding="utf-8") as arquivo:
        json.dump(data, arquivo, indent=4, ensure_ascii=False)

# Endpoint para listar todos os imóveis
@app.route("/imoveis", methods=["GET"])
def listar_imoveis():
    return jsonify(carregar_bd())

# Endpoint para adicionar um novo imóvel
@app.route("/imoveis", methods=["POST"])
def adicionar_imovel():
    bd = carregar_bd()
    novo_imovel = request.json
    
    # Encontra o próximo ID
    if bd:
        novo_imovel["id"] = max(imovel["id"] for imovel in bd) + 1
    else:
        novo_imovel["id"] = 1
        
    # Adiciona a data de entrada se não for fornecida
    if "entrada" not in novo_imovel or not novo_imovel["entrada"]:
        novo_imovel["entrada"] = dt.datetime.now().strftime("%Y-%m-%d")

    bd.append(novo_imovel)
    salvar_bd(bd)
    return jsonify({"mensagem": "Imóvel adicionado com sucesso!", "imovel": novo_imovel}), 201

# Endpoint para atualizar um imóvel existente
@app.route("/imoveis/<int:imovel_id>", methods=["PUT"])
def atualizar_imovel(imovel_id):
    bd = carregar_bd()
    dados_atualizados = request.json
    for i, imovel in enumerate(bd):
        if imovel["id"] == imovel_id:
            bd[i].update(dados_atualizados)
            salvar_bd(bd)
            return jsonify({"mensagem": "Imóvel atualizado com sucesso!", "imovel": bd[i]})
    return jsonify({"erro": "Imóvel não encontrado."}), 404

# Endpoint para remover um imóvel
@app.route("/imoveis/<int:imovel_id>", methods=["DELETE"])
def remover_imovel(imovel_id):
    bd = carregar_bd()
    imovel_removido = None
    for i, imovel in enumerate(bd):
        if imovel["id"] == imovel_id:
            imovel_removido = bd.pop(i)
            break
    if imovel_removido:
        salvar_bd(bd)
        return jsonify({"mensagem": "Imóvel removido com sucesso!"})
    return jsonify({"erro": "Imóvel não encontrado."}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
