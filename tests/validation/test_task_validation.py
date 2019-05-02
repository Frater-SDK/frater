from unittest import TestCase

from frater.stream import InputStream, OutputStream
from frater.task import Task, ComposedTask
from frater.validation.task import *
from .mocks import MockValidationType, OtherMockValidationType


class TestTaskValidation(TestCase):
    def test_is_valid_composition(self):
        tasks = list()
        type_0 = MockValidationType
        type_1 = OtherMockValidationType

        for _ in range(3):
            tasks.append(Task(type_0, type_1))
            type_1, type_0 = type_0, type_1

        assert is_valid_composition(tasks)

        tasks = [Task(int, int), Task(float, float)]
        assert not is_valid_composition(tasks)

    def test_is_valid_input_stream_for_task(self):
        task = Task(MockValidationType, MockValidationType)
        input_stream = InputStream(MockValidationType)

        assert is_valid_input_stream_for_task(task, input_stream)

    def test_is_valid_output_stream_for_task(self):
        task = Task(MockValidationType, MockValidationType)
        output_stream = OutputStream(MockValidationType)

        assert is_valid_output_stream_for_task(task, output_stream)

    def test_is_valid_input_stream_for_composed_task(self):
        tasks = [Task(MockValidationType, OtherMockValidationType),
                 Task(OtherMockValidationType, OtherMockValidationType)]

        input_stream = InputStream(MockValidationType)
        composed_task = ComposedTask(tasks)

        assert is_valid_input_stream_for_composed_task(composed_task, input_stream)

        input_stream = InputStream(OtherMockValidationType)
        composed_task = ComposedTask(tasks)

        assert not is_valid_input_stream_for_composed_task(composed_task, input_stream)

    def test_is_valid_output_stream_for_composed_task(self):
        tasks = [Task(MockValidationType, OtherMockValidationType),
                 Task(OtherMockValidationType, OtherMockValidationType)]

        output_stream = OutputStream(OtherMockValidationType)
        composed_task = ComposedTask(tasks)

        assert is_valid_output_stream_for_composed_task(composed_task, output_stream)

        output_stream = OutputStream(MockValidationType)
        composed_task = ComposedTask(tasks)

        assert not is_valid_output_stream_for_composed_task(composed_task, output_stream)
