# _*_ coding: utf-8_*_


class CPF:
    """
    A simple Python library containing functions that check Brazilian documents values.
    It is intended to make it easy to verify CPF numbers.
    """
    def return_cpf_dv(inscricao: str) -> list:
        """Returns a list of last two numbers to registration number of CPF.
        Ex: return_cpf_dv('111444777') -> 35 """
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


    def valid_cpf(cnpj: str) -> bool:
        """Returns True (valid) or False (invalid) to a full-number of CPF.
        Ex: valid_cpf('11144477735') -> True
        """
        valida = False
        inscricao = cnpj[:-2]
        dv = list(map(int, cnpj[-2:]))
        dv_teste=CPF.return_cpf_dv(inscricao)
        
        if dv_teste == dv:
            valida = True

        return valida



