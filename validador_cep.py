import pandas as pd
import re

class ValidadorCEP:
    def __init__(self, caminho_arquivo):
        """
        Inicializa o validador de CEP carregando os dados do Excel.
        
        :param caminho_arquivo: Caminho para o arquivo Excel contendo os intervalos de CEPs.
        """
        try:
            self.df = pd.read_excel(caminho_arquivo)
            self.df['CEP_INICIAL'] = self.df['CEP_INICIAL'].apply(self._formatar_cep)
            self.df['CEP_FINAL'] = self.df['CEP_FINAL'].apply(self._formatar_cep)
        except Exception as e:
            raise ValueError(f"Erro ao carregar o arquivo Excel: {e}")

    def _formatar_cep(self, cep):
        """
        Remove caracteres não numéricos do CEP.
        
        :param cep: CEP no formato string.
        :return: CEP formatado como inteiro.
        """
        try:
            return int(re.sub(r'\D', '', str(cep)))
        except ValueError:
            raise ValueError(f"CEP inválido: {cep}")

    def validar_cep(self, cep, cidade):
        """
        Valida se o CEP informado pertence à cidade especificada.
        
        :param cep: CEP no formato string.
        :param cidade: Nome da cidade.
        :return: True se o CEP pertence à cidade, False caso contrário.
        """
        try:
            cep_numerico = self._formatar_cep(cep)
            cidade = cidade.lower()

            for _, row in self.df.iterrows():
                if row['LOCALIDADE'].lower() == cidade:  # Corrigido para 'LOCALIDADE'
                    if row['CEP_INICIAL'] <= cep_numerico <= row['CEP_FINAL']:
                        return True
            return False
        except Exception as e:
            raise ValueError(f"Erro ao validar CEP: {e}")

# Exemplo de uso:
if __name__ == "__main__":
    try:
        caminho_arquivo = r"caminho do arquvio"
        validador = ValidadorCEP(caminho_arquivo)
        print(validador.validar_cep("18.050-100", "Sorocaba"))  # Deve retornar True
    except Exception as e:
        print(e)
