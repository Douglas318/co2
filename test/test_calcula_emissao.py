import pytest
from emissao import calcula_emissao

def test_calcula_emissao():

    emissao = calcula_emissao('diesel', 100)
    assert emissao['tipo_de_combustivel'] == 'diesel'
    assert emissao['distancia'] == 100
    assert emissao['eficiencia'] == 20
    assert emissao['co2_emissao'] == 70
    
    emissao = calcula_emissao('gasolina', 100)
    assert emissao['tipo_de_combustivel'] == 'gasolina'
    assert emissao['distancia'] == 100
    assert emissao['eficiencia'] == 20
    assert emissao['co2_emissao'] == 60
    
    with pytest.raises(ValueError):
        calcula_emissao('etanol', 100)
