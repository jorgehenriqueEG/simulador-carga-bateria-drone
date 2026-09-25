def calcular_voo(tensao, mah):
    energia_wh = (tensao * mah) / 1000
    consumo_w = 45
    tempo_min = (energia_wh / consumo_w) * 60
    massa_carga = (mah / 1000) * 3.2
    print(f"Carga Máx: {massa_carga:.2f} kg | Voo: {int(tempo_min)} min")

tensao = 14.8
mah = 11100
calcular_voo(tensao, mah)