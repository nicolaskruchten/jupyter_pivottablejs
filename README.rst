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

Include any `option to PivotTable.js's pivotUI() function`_ as a keyword argument.

.. code:: python

    pivot_ui(df, rows=['row_name'], cols=['col_name'])

Independently control the output file path and the URL used to access it from Jupyter, in case the default relative-URL behaviour is incompatible with Jupyter's settings.

.. code:: python

    pivot_ui(df, outfile_path="/x/y.html", url="http://localhost/a/b/x.html")

.. _Jupyter/IPython Notebook: http://jupyter.org/
.. _PivotTable.js: https://github.com/nicolaskruchten/pivottable
.. _option to PivotTable.js's pivotUI() function: https://github.com/nicolaskruchten/pivottable/wiki/Parameters#options-object-for-pivotui
