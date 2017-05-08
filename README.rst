``pivottablejs``: the Python module
===================================

Drag’n’drop Pivot Tables and Charts for `Jupyter/IPython Notebook`_,
care of `PivotTable.js`_

Installation
------------

``pip install pivottablejs``

Usage
-----

.. code:: python

    import pandas as pd
    df = pd.read_csv("some_input.csv")

    from pivottablejs import pivot_ui

    pivot_ui(df)

Advanced Usage
--------------

Include any `valid option`_ to PivotTable.js's `pivotUI()` function as a keyword argument.

.. code:: python

    pivot_ui(df, rows['row_name'], cols=['col_name'])

Independently control the output file path and the URL used to access it from Jupyter.

.. code:: python

    pivot_ui(df, outfile_path="x.html", url_prefix="http://localhost/path/")

.. _Jupyter/IPython Notebook: http://jupyter.org/
.. _PivotTable.js: https://github.com/nicolaskruchten/pivottable
.. _valid option: https://github.com/nicolaskruchten/pivottable/wiki/Parameters#options-object-for-pivotui
