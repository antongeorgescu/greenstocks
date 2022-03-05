define(['base/js/namespace'], function(IPython){
    console.log("Kernel event handler loaded")
    $([IPython.events]).on('kernel_ready.Kernel', function() {
        /**
        * The python code inside IPython.notebook.kernel.execute should be in the same line.
        * There should be no linebreaks or tabs. That makes this code fail silently while kernel load.
        */
        IPython.notebook.kernel.execute(`import os;os.environ['AZUREML_NB_PATH'] = '${IPython.notebook.notebook_path}';import azureml._jupyter_common;`)
    });
    return {onload:function() {console.log("Setting up kernel event handler: %o",IPython)}}
})