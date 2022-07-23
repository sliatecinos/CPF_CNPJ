.. _BR-registrations:

BR registrations
===================

|LICENSE|

.. |LICENSE| image:: https://img.shields.io/github/license/sliatecinos/br_registrations?style=plastic
    :alt: GitHub license   
    :target: https://github.com/sliatecinos/br_registrations/blob/master/LICENSE.txt


**Project description**
-----------------------
.. begin-docs

A simple Python library containing functions that check Brazilian documents values. It is intended to make it easy to verify CNPJ and CPF document numbers.
Originally developed and open-sourced at `Sliatecinos (GitHub) <https://github.com/sliatecinos>`_.


**Installation**
----------------
.. begin-installation

``pip install br-registrations``

.. end-installation

**Basic Usage**
---------------
.. begin-usage

.. code:: python

    from br_registrations import validateCPF, validateCNPJ

    # Validation test of registration CPF number
    # Instances the validation
    cpf=validateCPF.CPF
    # Passing a 11-digit number of CPF (in string format):
    response_1=cpf.valid_cpf('11144477735')
    response_2=cpf.valid_cpf('912.441.670-37', True)   # using Regex feature
    response_3=cpf.valid_cpf('11111111111', True)   # using Regex feature
    # Outputs #1, #2: 'CPF ___ is valid is True .'
    print('CPF "11144477735" is valid is', response_1, '.')
    print('CPF "912.441.670-37" is valid is', response_2, '.')
    # Outputs #3: 'CPF ___ is valid is False .'
    print('CPF "11111111111" is valid is', response_3, '.')

    # Passing a registration number of CPF (in string format):
    dv_1=cpf.get_cpf_dv('111444777')
    dv_2=cpf.get_cpf_dv('912.441.670', True)   # using Regex feature
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
    response_2=cnpj.valid_cnpj('46.293.332/0001-02', True)   # using Regex feature
    response_3=cnpj.valid_cnpj('11111111111111')
    # Outputs #1, #2: 'CNPJ ___ is valid is True .'
    print('CNPJ "11222333000181" is valid is', response_1, '.')
    print('CNPJ "46.293.332/0001-02" is valid is', response_2, '.')
    # Outputs #3: 'CNPJ ___ is valid is False .'
    print('CNPJ "11111111111111" is valid is', response_3, '.')

    # Passing a registration number of CNPJ (in string format):
    dv_1=cnpj.get_cnpj_dv('112223330001')
    dv_2=cnpj.get_cnpj_dv('46.293.332/0001', True)   # using Regex feature
    # Output #1 (in list): 'Correct DV:  [8, 1]'
    print('Correct DV: ', dv_1)
    # Output #2 (in list): 'Correct DV:  [0, 2]'
    print('Correct DV: ', dv_2)

    # View lib version:
    import br_registrations as brr
    print(brr.__version__)

.. end-usage

Links
-----
* PyPi.org: `https://pypi.org/project/br-registrations <https://pypi.org/project/br-registrations/>`_

* Source code: `https://github.com/sliatecinos/br_registrations <https://github.com/sliatecinos/br_registrations>`_

License
-------

The project is made available under the terms of the MIT license.  See `LICENSE <./LICENSE>`_ for details.

.. end-docs
