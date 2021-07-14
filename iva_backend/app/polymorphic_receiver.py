def polymorphic_receiver(signal, sender, **kwargs):
    """
    A decorator for creating a receiver for signals for parent and all sub-classes of the sender
    """

    def _get_subclasses():
        result = [sender]
        classes_to_inspect = [sender]
        while classes_to_inspect:
            class_to_inspect = classes_to_inspect.pop()
            for subclass in class_to_inspect.__subclasses__():
                if subclass not in result:
                    result.append(subclass)
                    classes_to_inspect.append(subclass)
        return result

    def _decorator(func):
        sender_classes = _get_subclasses()
        for sender_class in sender_classes:
            if isinstance(signal, (list, tuple)):
                for s in signal:
                    s.connect(func, sender_class, **kwargs)
            else:
                signal.connect(func, sender_class, **kwargs)
        return func
    return _decorator
