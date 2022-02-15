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

Você pode usar ``br_registrations.version`` function:

.. .. autofunction:: br_registrations.version

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. .. autoexception:: br_registrations.InvalidKindError

Por exemplo:

>>> import br_registrations as brr
>>> brr.version
'0.0.0.9'

