setuptools_scm_env
==================
This is a `setuptools_scm <https://github.com/pypa/setuptools_scm>`_ plugin
that adds support for providing package version via environment variable.

Usage
-----
Install ``setuptools_scm_env`` as usual or add it to your package
``setup_requires``. Provide version during build/install via environment
variable ``SETUPTOOLS_SCM_VERSION``:

.. code-block:: shell

    $ SETUPTOOLS_SCM_VERSION=1.2.3 pip install your-package.tar.gz


Motivation
----------
Sometimes you should install package that depends on
`setuptools_scm <https://github.com/pypa/setuptools_scm>`_, but you
are not able to change anything inside package and/or distribution format.
In that case you can provide version through environment variable
and use your usual tools for packaging/installation.
