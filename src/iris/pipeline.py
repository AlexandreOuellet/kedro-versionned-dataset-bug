"""
This is a boilerplate pipeline
generated using Kedro 0.18.10
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import A, B


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=A,
                inputs=["parameters"],
                outputs="versionned_dataset",
                name="A",
            ),
            node(
                func=B,
                inputs=["versionned_dataset"],
                outputs=None,
                name="B",
            ),

        ]
    )
