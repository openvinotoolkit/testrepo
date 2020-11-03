#!groovy
properties([
    parameters([
        booleanParam(defaultValue: true,
                     description: 'Cancel the rest of parallel stages if one of them fails and return status immediately',
                     name: 'failFast'),
        string(
            trim: true,
            defaultValue: 'akladiev/github_get_changed_files',
            name: 'library_version')
    ])
])
env.getEnvironment().each { name, value -> println "Name: $name -> Value $value" }
loadOpenVinoLibrary { thelib ->
    client = thelib.com.intel.openvino.client.ClientFactory.buildClient(this, false)
    changeset = client.getChangedFiles()
    println "[INFO] Files changed :\n${changeset.join('\n')}"
}
