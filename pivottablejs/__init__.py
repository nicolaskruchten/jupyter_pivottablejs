# coding: utf8

# %install_ext http://nicolas.kruchten.com/pivottable/jupyter/pivottablejs.py
# %load_ext pivottablejs
# %pivottablejs data_frame


template = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        
        <title>PivotTable.js</title>

        <!-- external libs from cdnjs -->
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.10/c3.min.css">
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery-csv/0.71/jquery.csv-0.71.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.10/c3.min.js"></script>

        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/pivottable/1.6.3/pivot.min.css">
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pivottable/1.6.3/pivot.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pivottable/1.6.3/d3_renderers.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pivottable/1.6.3/c3_renderers.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pivottable/1.6.3/export_renderers.min.js"></script>

        <style>
            body {font-family: Verdana;}
            .node {
              border: solid 1px white;
              font: 10px sans-serif;
              line-height: 12px;
              overflow: hidden;
              position: absolute;
              text-indent: 2px;
            }
            .c3-line, .c3-focused {stroke-width: 3px !important;}
            .c3-bar {stroke: white !important; stroke-width: 1;}
            .c3 text { font-size: 12px; color: grey;}
            .tick line {stroke: white;}
            .c3-axis path {stroke: grey;}
            .c3-circle { opacity: 1 !important; }
        </style>
    </head>
    <body>
        <script type="text/javascript">
            $(function(){
                if(window.location != window.parent.location)
                    $("<a>", {target:"_blank", href:""})
                        .text("[pop out]").prependTo($("body"));
                    
                $("#output").pivotUI( 
                    $.csv.toArrays($("#output").text()), 
                    $.extend({ 
                            renderers: $.extend(
                                $.pivotUtilities.renderers, 
                                $.pivotUtilities.c3_renderers, 
                                $.pivotUtilities.d3_renderers,
                                $.pivotUtilities.export_renderers
                                ),
                            hiddenAttributes: [""]
                        }
                        ,
                        %(pivot_extras)s
                    )
                ).show();
             });
        </script>
        <div id="output" style="display: none;">%(df)s</div>
    </body>
</html>
"""

from IPython.display import IFrame
import json

def pivot_ui(df, outfile_path = "pivottablejs.html", width="100%", height="500", **kargs):
    pivot_extras = {}
    for key in ["rows","cols","aggregatorName","vals","rendererName"]:
        if key in kargs.keys():
            pivot_extras[key] = kargs[key]
        
    with open(outfile_path, 'w') as outfile:
        outfile.write(template % { "df":df.to_csv() , "pivot_extras":json.dumps(pivot_extras) } )
        
    return IFrame(src=outfile_path, width=width, height=height)
        

# EXAMPLE:
# import pandas as pd
# from pivottablejs import pivot_ui
# df = pd.DataFrame({"a":["col","alto","ancho","bla"],"b":[2,3,4,5],"c":[6,2,6,8]});
# pivot_ui(df,rows=["a"],cols=["b"],vals=["c"],aggregatorName="Sum",rendererName = "Heatmap")
