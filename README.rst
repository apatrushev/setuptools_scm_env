setuptools_scm_env
==================
``setuptools_scm_env`` helper package for
`setuptools_scm <https://github.com/pypa/setuptools_scm>`_ to provide
package version via environment variable.

Usage
-----
Install ``setuptools_scm_env`` as usual or add it to your package
``setupt_requires``. Provide version during build/install via environment
variable ``SETUPTOOLS_SCM_VERSION``:

.. code-block:: shell

    $ SETUPTOOLS_SCM_VERSION=1.2.3 pip install package.tar.gz


Motivation
----------
Sometimes you are not able to change anything inside package and/or
distribution format, but want to install package that depends on setuptools_scm.
In that case you can provide version through environment variable
and use your usual tools for packaging/installation.
