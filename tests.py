# _*_ coding: utf-8_*_
from br_registrations import validateCPF, validateCNPJ

# Validation test of registration CPF number
# Instances the validation
cpf=validateCPF.CPF
# Passing a 11-digit number of CPF (in string format):
response_1=cpf.valid_cpf('11144477735')
response_2=cpf.valid_cpf('912.441.670-37', True)
# Outputs: 'CPF is valid is True .'
print('CPF is valid is', response_1, '.')
print('CPF is valid is', response_2, '.')

# Passing a registration number of CPF (in string format):
dv_1=cpf.get_cpf_dv('111444777')
dv_2=cpf.get_cpf_dv('912.441.670', True)
# Output (in list): 'Correct DV:  [3, 5]'
print('Correct DV: ', dv_1)
# Output (in list): 'Correct DV:  [3, 7]'
print('Correct DV: ', dv_2)

print('='*100)

# Validation test of registration CNPJ number
# Instances the validation:
cnpj=validateCNPJ.CNPJ
# Passing a 14-digit number of CNPJ (in string format):
response_1=cnpj.valid_cnpj('11222333000181')
response_2=cnpj.valid_cnpj('46.293.332/0001-02', True)
# Output #1: 'CNPJ is valid is True .'
print('CNPJ is valid is', response_1, '.')
# Output #2: 'CNPJ is valid is True .'
print('CNPJ is valid is', response_2, '.')

# Passing a registration number of CNPJ (in string format):
dv_1=cnpj.get_cnpj_dv('112223330001')
dv_2=cnpj.get_cnpj_dv('46.293.332/0001', True)
# Output #1 (in list): 'Correct DV:  [8, 1]'
print('Correct DV: ', dv_1)
# Output #2 (in list): 'Correct DV:  [0, 2]'
print('Correct DV: ', dv_2)
