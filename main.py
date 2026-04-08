from extract   import extract
from transform import transform
from load      import load

print("Iniciando ETL...")

dados = extract()
dados = transform(dados)
load(dados)

print("ETL finalizado!")