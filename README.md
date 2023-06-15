# Kedro versionned dataset bug

This repo is to reproduce a dataset versionning bug when executing multiple time the same pipeline with different parameters (running multiple exepriments in parallel)

## To repro

* Clone this reprository
* Open in vscode with Devcontaineres (reopen/rebuild the devcontainers)
* `pip install -r src/requirements.txt`
* _Quickly_, you need to :
  * `kedro run` (this will run for ~100 seconds)
  * modify `parameters.yml` to decrease the sleep time to 1 second
  * open a new terminal and execute `kedro run`
  * Let both run finish

Observe how the outputs are the same, even though it is random data for both runs.

## Explanation

The issue is with the timing.

Here is how it looks in a timeline
```
Exec 1: |[A-----(sleep for 100 seconds)]->versionned_dataset->[B]
Exec 2: |  [A]->versionned_dataset->[B]
```

In this scenario, when `Exec 1 node B` is executed, it will fetch the latest version of the dataset.  That latest version will be `Exec 2 node A`'s versionned_dataset.

When `Exec 1` writes its dataset's versions, it will have a timestamp prior to `Exec 2`, as it started earlier.

The real issue is that the version ID (the timestamp) is generated when `node A` starts its execution.  The fix would be to have the version ID generated when the pipeline starts executing and pass that version to all of the nodes


