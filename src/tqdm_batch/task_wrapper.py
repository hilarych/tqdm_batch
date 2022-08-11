def task_wrapper(pid, function, batch, queue, *args, **kwargs):
    """
    Wrapper to add progress bar update
    """
    result = []
    for example in batch:
        result.append(function(example, *args, **kwargs))
        queue.put(f'update{pid}')
    return result

def task_wrapper_no_q(pid, function, batch,*args, **kwargs):
    """
    Wrapper to add progress bar update
    """
    result = []
    for example in batch:
        result.append(function(example, *args, **kwargs))
    return result
