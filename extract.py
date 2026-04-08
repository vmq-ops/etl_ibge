import requests

def extract():
    periodos = "201201|201202|201203|201204|201301|201302|201303|201304|201401|201402|201403|201404|201501|201502|201503|201504|201601|201602|201603|201604|201701|201702|201703|201704|201801|201802|201803|201804|201901|201902|201903|201904|202001|202002|202003|202004|202101|202102|202103|202104|202201|202202|202203|202204|202301|202302|202303|202304|202401|202402|202403|202404|202501|202502|202503|202504"

    url = f"https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/{periodos}/variaveis/4099"

    parametros = {
        "localidades": "N3[26]",
        "classificacao": "2[6794,4,5]"
    }

    response = requests.get(url, params=parametros)
    data = response.json()

    registros = []

    for resultado in data[0]["resultados"]:

        categoria_dict = resultado["classificacoes"][0]["categoria"]
        categoria_id   = list(categoria_dict.keys())[0]

        nomes = {"6794": "Total", "4": "Homens", "5": "Mulheres"}
        categoria_nome = nomes[categoria_id]

        serie = resultado["series"][0]["serie"]

        for periodo, valor in serie.items():
            if valor == "-" or valor == "":
                continue

            registros.append({
                "categoria": categoria_nome,
                "periodo":   periodo,
                "valor":     valor
            })

    print(f"[EXTRACT] {len(registros)} registros extraídos da API.")
    return registros