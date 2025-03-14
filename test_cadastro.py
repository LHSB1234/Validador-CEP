import pytest
from validador_cep import ValidadorCEP

# Caminho completo para o arquivo Excel
CAMINHO_ARQUIVO = r"caminho do arquvio"

@pytest.fixture
def validador():
    return ValidadorCEP(CAMINHO_ARQUIVO)

def test_cep_valido_sorocaba(validador):
    assert validador.validar_cep("18.050-100", "Sorocaba") == True

def test_cep_valido_capela_do_alto(validador):
    assert validador.validar_cep("18.195-000", "Capela do Alto") == True

def test_cep_valido_sao_roque(validador):
    assert validador.validar_cep("18.130-020", "São Roque") == True

def test_cep_invalido_votorantim(validador):
    assert validador.validar_cep("19.000-000", "Votorantim") == False

def test_cep_invalido_para_cidade_errada(validador):
    assert validador.validar_cep("18.195-000", "Sorocaba") == False
