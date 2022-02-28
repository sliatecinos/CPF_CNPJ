Métodos disponíveis
**********************

.. _get-dv-docs:

Obter os dígitos da inscrição
=================================

Você pode usar os métodos ``validateCNPJ.CNPJ.get_cnpj_dv`` ou
``validateCPF.CPF.get_cpf_dv``, quando precisar obter os últimos
dois dígitos da inscrição pesquisada. Estes métodos possuem o parâmetro
opcional :ref:`parâmetro Regex`.

Por exemplo, para o CNPJ o método será:

.. autofunction:: br_registrations.validateCNPJ.CNPJ.get_cnpj_dv

E para o CPF será:

.. autofunction:: br_registrations.validateCPF.CPF.get_cpf_dv

.. _validating-docs:

Validar a inscrição
======================

Você pode realizar a validação de um número de inscrição com os métodos
``validateCNPJ.CNPJ.valid_cnpj`` ou ``validateCPF.CPF.valid_cpf``
disponíveis.Estes métodos possuem o parâmetro opcional :ref:`parâmetro Regex`.

Por exemplo, para o CNPJ o método será:

.. autofunction:: br_registrations.validateCNPJ.CNPJ.valid_cnpj

E para o CPF será:

.. autofunction:: br_registrations.validateCPF.CPF.valid_cpf

.. _parâmetro Regex:

Parâmetro regex
================

Em todos os métodos há a opção de parâmetro ``regex``, com valor *default*: **False**, 
que permite uma pesquisa que contemple pontuações no meio da inscrição.
Caso a pesquisa seja realizada com esse argumento diferente de ``True`` será retornada uma
``*Exception*`` pelo interpretador.

Exemplo:

>>> from br_registrations import validateCPF
>>> response_2=cpf.valid_cpf('912.441.670-37', regex=True)
>>> print('CPF "912.441.670-37" is valid is', response_2, '.')
'CPF "912.441.670-37" is valid is True .'

.. :py:func:`lumache.get_random_ingredients`
