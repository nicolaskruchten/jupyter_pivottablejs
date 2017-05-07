``pivottablejs``: the Python module
===================================

Drag’n’drop Pivot Tables and Charts for `Jupyter/IPython Notebook`_,
care of `PivotTable.js`_

Installation
------------

``pip install pivottablejs``

Usage
-----

::

    import pandas as pd
    df = pd.read_csv("some_input.csv")

    from pivottablejs import pivot_ui

    pivot_ui(df)

.. _Jupyter/IPython Notebook: http://jupyter.org/
.. _PivotTable.js: https://github.com/nicolaskruchten/pivottable
