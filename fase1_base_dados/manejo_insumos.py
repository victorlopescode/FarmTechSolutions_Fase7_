def calcular_insumos(area_m2: float, cultura: str) -> dict:
    """
    Retorna um dicionário com as quantidades de insumos baseadas na área em m².
    Pode ser ajustado de acordo com a cultura.
    """
    # Fatores básicos (podem ser refinados por cultura)
    fator_semente = 0.5   # kg por m²
    fator_fertilizante = 0.3  # kg por m²
    fator_agua = 2.0      # L por m²

    # Pequeno ajuste por cultura (ilustrativo)
    if cultura == "Soja":
        fator_agua *= 1.1
    elif cultura == "Milho":
        fator_fertilizante *= 1.2
    elif cultura == "Trigo":
        fator_semente *= 0.9

    return {
        "sementes_kg": area_m2 * fator_semente,
        "fertilizante_kg": area_m2 * fator_fertilizante,
        "agua_litros": area_m2 * fator_agua,
    }
