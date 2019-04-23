def is_valid_composition(tasks):
    for i in range(len(tasks) - 1):
        if not tasks[i].output_type == tasks[i + 1].input_type:
            return False
    return True


def is_valid_input_stream_for_task(task, input_stream):
    return task.input_type == input_stream.stream_type


def is_valid_output_stream_for_task(task, output_stream):
    return task.output_type == output_stream.stream_type


def is_valid_input_stream_for_composed_task(task, input_stream):
    return is_valid_input_stream_for_task(task.tasks[0], input_stream)


def is_valid_output_stream_for_composed_task(task, output_stream):
    return is_valid_output_stream_for_task(task.tasks[-1], output_stream)
