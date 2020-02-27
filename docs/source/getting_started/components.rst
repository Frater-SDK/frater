Components
==========

IOComponent
-----------

To start off, we'll show how to work with probably the most common type of Component: \
:py:class:`~frater.component.IOComponent`\. :py:class:`~frater.component.IOComponent`\s can be used for building \
components that require input and output streams.

Let's take a look with the following example where we build a simple summation component that adds up all the data that\
it receives over time.

.. literalinclude:: examples/io_component_example.py
    :language: python
    :lines: 1-22


Here we've defined the :py:class:`SummationComponent` with its corresponding state `SummationComponentState` that will\
hold the state info of