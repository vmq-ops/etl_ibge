from datetime import datetime

def transform(registros):
    documentos = []

    for reg in registros:
        if reg["valor"] in ["-", "...", ""]:
            continue

        periodo_raw = reg["periodo"]
        ano         = int(periodo_raw[:4])
        trimestre   = int(periodo_raw[4:])

        taxa = float(reg["valor"])

        documentos.append({
            "categoria":        reg["categoria"],
            "ano":              ano,
            "trimestre":        trimestre,
            "periodo":          f"{ano}T{trimestre}",
            "taxa_desocupacao": taxa,
            "fonte":            "IBGE",
            "data_coleta":      datetime.now()
        })

    print(f"[TRANSFORM] {len(documentos)} documentos transformados.")
    return documentos