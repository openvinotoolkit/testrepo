#!groovy


properties([
    parameters([
        booleanParam(defaultValue: true,
                     description: 'Cancel the rest of parallel stages if one of them fails and return status immediately',
                     name: 'failFast'),
        booleanParam(defaultValue: true,
                     description: 'Propagate status to GitHub',
                     name: 'propagateStatus'),
        string(defaultValue: 'akladiev/max_survivability',
               trim: true,
               description: 'library version',
               name: 'library_version'),
    ])
])





loadOpenVinoLibrary {
    entrypoint(this)
}
