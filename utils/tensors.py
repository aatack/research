from typing import List
import tensorflow as tf


def float_input(
    name: str, *shape: List[int], variable_dimension: bool = True
) -> tf.Tensor:
    """Create a float placeholder tensor, optionally with a variable dimension."""
    print(shape)
    return tf.placeholder(
        tf.float32, tuple(((None,) if variable_dimension else ()) + shape), name
    )
