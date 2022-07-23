# _*_ coding: utf-8_*_
import re
"""
@Author       : sliatecinos
@Created Time : 2021-01-19 20:57:00
@Updated Time : 2021-02-28 00:00:00
@BR Registrations
    environments:
"""


class CNPJ:
    """
    Uma classe Python simples de validação dos números de inscrição CNPJ.
    """
    @staticmethod
    def get_cnpj_dv(inscricao: str, regex: bool=False) -> list:
        """
        Retorna uma lista dos dois últimos números de uma inscrição CNPJ.

        |  Exemplos:
        |  :return cnpj_dv: ('112223330001') -> [8, 1]
        |  :return cnpj_dv: ('46.293.332/0001') -> [0, 2]
        """
        if regex:
            inscricao=re.findall(r"\d+", inscricao)
            inscricao=''.join(inscricao)

        DV = []
        ALINHAMENTO=[6,5,4,3,2,9,8,7,6,5,4,3,2]
        inscricao = list(inscricao.zfill(12))
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
    def valid_cnpj(cnpj: str, regex: bool=False) -> bool:
        """
        Retorna True (válido) ou False (inválido) para um documento CNPJ.

        |  Exemplos:
        |  :return valid_cnpj: ('11222333000181') -> True
        |  :return valid_cnpj: ('46.293.332/0001-02') -> True
        """
        if regex:
            cnpj=re.findall(r"\d+", cnpj)
            cnpj=''.join(cnpj)

        valida = False
        if cnpj == cnpj[::-1]:
            return valida

        inscricao = cnpj[:-2]
        dv = list(map(int, cnpj[-2:]))
        dv_teste=CNPJ.get_cnpj_dv(inscricao)

        if dv_teste == dv:
            valida = True

        return valida
