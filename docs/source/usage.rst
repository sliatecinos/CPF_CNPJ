Usage
=====

.. _installation:

Instalação
---------------

Para usar, primeiro efetue a instalação com o pip:

.. code-block:: console

   (.venv) $ pip install br-registrations

Validar um CPF
----------------

To retrieve a list of random ingredients,
you can use the ``validateCPF.CPF.valid_cpf`` function:

.. autofunction:: validateCPF.CPF.valid_cpf

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: br_registrations.InvalidKindError

Por exemplo:

>>> import br_registrations
>>> br_registrations.validateCPF.CPF.valid_cpf()
'True'

