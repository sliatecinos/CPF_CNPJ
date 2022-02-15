Métodos disponíveis
=====================

.. _obter-digitos-inscricao:

Obter os dígitos da inscrição
=================================

Você pode usar os métodos ``validateCNPJ.CNPJ.get_cnpj_dv`` ou
 ``validateCPF.CPF.get_cpf_dv``, quando precisar obter os últimos
 dois dígitos da inscrição pesquisada.

Por exemplo, para o CNPJ o método será:

.. autofunction:: br_registrations.validateCNPJ.CNPJ.get_cnpj_dv

E para o CPF será:

.. autofunction:: br_registrations.validateCPF.CPF.get_cpf_dv

.. _validar-digitos-inscricao:

Validar a inscrição
======================

Você pode realizar a validação de um número de inscrição com os métodos
 ``validateCNPJ.CNPJ.valid_cnpj`` ou ``validateCPF.CPF.valid_cpf``
 disponíveis.

Por exemplo, para o CNPJ o método será:
.. autofunction:: br_registrations.validateCNPJ.CNPJ.valid_cnpj

E para o CPF será:
.. autofunction:: br_registrations.validateCPF.CPF.valid_cpf

.. .. autoexception:: br_registrations.InvalidKindError
.. Otherwise, :py:func:`lumache.get_random_ingredients`
.. will raise an exception.
