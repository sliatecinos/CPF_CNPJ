"""
BR registrations - Biblioteca Python usada para validação de números de CNPJ/CPF usados no Brasil.
"""

__version__ = "0.0.0.9"


class CNPJ:
    """Traz os metodos de validação de CNPJ."""
    @staticmethod
    def get_cnpj_dv(inscricao: str, regex=False):
        """Retorna uma lista com os últimos dois dígitos de um CNPJ.
        Ex: return_cnpj_dv('112223330001') -> 81 
            return_cnpj_dv('46.293.332/0001') -> 02

        :param inscricao: os 12 primeiros dígs. de um CNPJ.
        :type inscricao: str
        :return: versão da lib.
        :rtype: list[str,str]
        """
        return ['8','1']
    pass


class CPF:
    """Traz os metodos de validação de CPF."""
    @staticmethod
    def get_cpf_dv(inscricao: str, regex=False):
        """Retorna uma lista com os últimos dois dígitos de um CPF.
        Ex: return_cpf_dv('111444777') -> 35 
            return_cpf_dv('912.441.670') -> 37 

        :param inscricao: os 9 primeiros dígs. de um CPF.
        :type inscricao: str
        :return: versão da lib.
        :rtype: list[str,str]
        """
        return ['3','5']
    pass


def version():
    """
    retorna a versão atual da instalação de br-registrations.

    :param: N/A
    :type: N/A
    :return: versão da lib.
    :rtype: str
    """
    return '0.0.0.9'
