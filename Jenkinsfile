#!groovy
properties([
    parameters([
        booleanParam(defaultValue: true,
                     description: 'Cancel the rest of parallel stages if one of them fails and return status immediately',
                     name: 'failFast'),
        string(
            trim: true,
            defaultValue: 'akladiev/changesets_to_entrypoint',
            name: 'library_version')
    ])
])
loadOpenVinoLibrary {
    entrypoint(this)
}
