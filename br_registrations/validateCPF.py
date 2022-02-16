# _*_ coding: utf-8_*_
import re
"""
@Author       : sliatecinos
@Created Time : 2021-01-19 20:57:00
@Updated Time : 2021-02-15 00:00:00
@BR Registrations
    environments:
"""


class CPF:
    """
    Uma classe Python simples de validação dos números de inscrição CPF.
    """
    @staticmethod
    def get_cpf_dv(inscricao: str, regex: bool=False) -> list:
        """Retorna uma lista dos dois últimos números de uma inscrição CPF.
        | Exemplos:
        | :return cpf_dv: ('111444777') -> 35
        | :return cpf_dv: ('912.441.670') -> 37
        """
        if regex:
            inscricao=re.findall("\d+", inscricao)
            inscricao=''.join(inscricao)

        DV = []
        ALINHAMENTO=[11,10,9,8,7,6,5,4,3,2]
        inscricao = list(inscricao.zfill(9))
        # retorna DV_1
        inscricao_1 = list(map(int, inscricao))
        somatorio=list(zip(inscricao_1, ALINHAMENTO[1:]))   # usa parte do alinhamento
        DV_1=sum(map(lambda x: x[0]*x[1], somatorio)) % 11
        DV_1 = 0 if DV_1 < 2 else 11 - DV_1
        DV.append(DV_1)

        # retorna DV_2
        inscricao_2 = list(map(int, inscricao))
        inscricao_2.extend(DV)
        somatorio=list(zip(inscricao_2, ALINHAMENTO[:]))   # usa todo alinhamento
        DV_2=sum(map(lambda x: x[0]*x[1], somatorio)) % 11
        DV_2 = 0 if DV_2 < 2 else 11 - DV_2
        DV.append(DV_2)

        return DV


    @staticmethod
    def valid_cpf(cpf: str, regex: bool=False) -> bool:
        """Retorna True (válido) ou False (inválido) para um documento CPF.
        | Exemplos:
        | :return valid_cpf: ('11144477735') -> True
        | :return valid_cpf: ('912.441.670-37') -> True
        """
        if regex:
            cpf=re.findall("\d+", cpf)
            cpf=''.join(cpf)

        valida = False
        if cpf == cpf[::-1]:
            return valida

        inscricao = cpf[:-2]
        dv = list(map(int, cpf[-2:]))
        dv_teste=CPF.get_cpf_dv(inscricao)

        if dv_teste == dv:
            valida = True

        return valida
