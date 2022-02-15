Métodos disponíveis
=====================

.. _obter-digitos-inscricao:

Obter os dígitos da inscrição
=================================

Você pode usar os métodos ``validateCNPJ.CNPJ.get_cnpj_dv`` ou
 ``validateCPF.CPF.get_cpf_dv``, quando precisar obter os últimos
 dois dígitos da inscrição pesquisada. Estes métodos possuem o parâmetro
 opcional :ref:`Regex`.

Por exemplo, para o CNPJ o método será:

.. autofunction:: br_registrations.validateCNPJ.CNPJ.get_cnpj_dv

E para o CPF será:

.. autofunction:: br_registrations.validateCPF.CPF.get_cpf_dv

.. _validar-digitos-inscricao:

Validar a inscrição
======================

Você pode realizar a validação de um número de inscrição com os métodos
 ``validateCNPJ.CNPJ.valid_cnpj`` ou ``validateCPF.CPF.valid_cpf``
 disponíveis.Estes métodos possuem o parâmetro opcional :ref:`Regex`.

Por exemplo, para o CNPJ o método será:
.. autofunction:: br_registrations.validateCNPJ.CNPJ.valid_cnpj

E para o CPF será:
.. autofunction:: br_registrations.validateCPF.CPF.valid_cpf

.. _Regex:

Parâmetro regex
================

Em todos os métodos você tem a opção de parâmetro ``regex``, com valor-padrão **False**, 
que permite uma pesquisa que contemple pontuações no meio da inscrição.
Caso a pesquisa seja realizada sem esse valor será retornada uma __Exception__ pelo interpretador.

.. .. autoexception:: br_registrations.InvalidKindError
.. :py:func:`lumache.get_random_ingredients`
