import requests
import time
import json

headers = {"Content-Type": "application/json"}
codigoTabelaReferencia = 320  # abril/2025
codigoTipoVeiculo = 2  # Moto

# Lista de marcas a serem consultadas
marcas = [
    {"Label": "HONDA", "Value": 80},
    {"Label": "YAMAHA", "Value": 101},
    {"Label": "SUZUKI", "Value": 99}
]

# Lista que irá conter todos os dados coletados
data = []

for marca in marcas:
    marca_nome = marca['Label']
    print(f"\n🔎 Marca: {marca_nome}")
    
    payload_modelos = {
        "codigoTabelaReferencia": codigoTabelaReferencia,
        "codigoTipoVeiculo": codigoTipoVeiculo,
        "codigoMarca": marca["Value"]
    }

    res_modelos = requests.post(
        "https://veiculos.fipe.org.br/api/veiculos/ConsultarModelos",
        json=payload_modelos,
        headers=headers
    )

    modelos = res_modelos.json().get("Modelos", [])

    for modelo in modelos[:2]:  # Pegando só os 2 primeiros modelos (pode remover isso depois)
        modelo_nome = modelo['Label']
        print(f"📍 Modelo: {modelo_nome}")

        payload_anos = {
            "codigoTabelaReferencia": codigoTabelaReferencia,
            "codigoTipoVeiculo": codigoTipoVeiculo,
            "codigoMarca": marca["Value"],
            "codigoModelo": modelo["Value"]
        }

        res_anos = requests.post(
            "https://veiculos.fipe.org.br/api/veiculos/ConsultarAnoModelo",
            json=payload_anos,
            headers=headers
        )
        anos = res_anos.json()

        dados_anos = []

        for ano in anos[:2]:  # Pegando só os 2 primeiros anos (pode remover isso depois)
            ano_modelo = int(ano["Value"].split("-")[0])
            tipo_comb = ano["Value"].split("-")[1]

            payload_valor = {
                "codigoTabelaReferencia": codigoTabelaReferencia,
                "codigoTipoVeiculo": codigoTipoVeiculo,
                "codigoMarca": marca["Value"],
                "codigoModelo": modelo["Value"],
                "codigoTipoCombustivel": tipo_comb,
                "anoModelo": ano_modelo,
                "tipoVeiculo": "2",
                "modeloCodigoExterno": "",
                "tipoConsulta": "tradicional"
            }

            res_valor = requests.post(
                "https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros",
                json=payload_valor,
                headers=headers
            )

            valor = res_valor.json().get("Valor", "N/A")
            print(f"   📆 Ano: {ano['Label']} - 💸 Valor: {valor}")

            dados_anos.append({
                "ano": ano['Label'],
                "valor": valor
            })

            time.sleep(0.5)

        # Adiciona os dados coletados do modelo à lista geral
        data.append({
            "marca": marca_nome,
            "modelo": modelo_nome,
            "anos": dados_anos
        })

# Envia todos os dados via POST para o webhook do n8n
res = requests.post(
    "https://primary-production-48c7.up.railway.app/webhook-test/scraping-carros",
    json=data
)

print(f"\n✅ Enviado para o n8n: {res.status_code}")
print(res.text)
