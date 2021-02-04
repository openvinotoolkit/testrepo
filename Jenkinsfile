#!groovy


properties([
    parameters([
        booleanParam(defaultValue: true,
                     description: 'Cancel the rest of parallel stages if one of them fails and return status immediately',
                     name: 'failFast'),
        booleanParam(defaultValue: true,
                     description: 'Propagate status to GitHub',
                     name: 'propagateStatus'),
        string(defaultValue: '',
               description: 'Pipeline shared library version (branch/tag/commit). Determined automatically if empty',
               name: 'library_version'),
        string(defaultValue: 'master',
               description: 'aaa',
               name: 'sourceBranch'),
        string(defaultValue: 'master',
               description: 'aaa',
               name: 'targetBranch')
        string(defaultValue: 'master',
               description: 'aaa',
               name: 'commitSha'),
        string(defaultValue: '2022-02-04T16:37:05.152657Z',
               description: 'aaa',
               name: 'commitDate'),
        string(defaultValue: 'github',
               description: 'aaa',
               name: 'eventSource'),
        string(defaultValue: 'testrepo',
               description: 'aaa',
               name: 'repoName'),
        string(defaultValue: 'private',
               description: 'aaa',
               name: 'repoType'),
    ])
])




loadOpenVinoLibrary {
    entrypoint(this)
}
