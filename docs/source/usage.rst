Usage
=====

.. _installation:

Instalação
---------------

Para usar, primeiro efetue a instalação com o pip:

.. code-block:: console

   (.venv) $ pip install br-registrations

Obter a versão atual
---------------------

Você pode usar ``.version`` function:

.. autofunction:: version

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. .. autoexception:: br_registrations.InvalidKindError

Por exemplo:

>>> import br_registrations
>>> br_registrations.validateCPF.CPF.valid_cpf('11111111111')
'False'

