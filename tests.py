# _*_ coding: utf-8_*_
from br_registrations import validateCNPJ, validateCPF

# Validation test of registration CNPJ number
# Instances the validation:
ret_CNPJ=validateCNPJ.CNPJ
# Passing a full-number of CNPJ (in string format):
response=ret_CNPJ.valid_cnpj('11222333000181')
# Output: 'CNPJ is valid is True .'
print('CNPJ is valid is', response, '.')

# Passing a registration number of CNPJ (in string format):
dv=ret_CNPJ.get_cnpj_dv('112223330001')
print('Correct DV: ', dv)
# Output (in list): 'Correct DV:  [8, 1]'

print('='*100)

# Validation test of registration CPF number
# Instances the validation
ret_CPF=validateCPF.CPF
# Passing a full-number of CPF (in string format):
response=ret_CPF.valid_cpf('11144477735')
# Output: 'CPF is valid is True .'
print('CPF is valid is', response, '.')

# Passing a registration number of CPF (in string format):
dv=ret_CPF.get_cpf_dv('111444777')
print('Correct DV: ', dv)
# Output (in list): 'Correct DV:  [3, 5]'
