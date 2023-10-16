from .i_model_changed_observer import IModelChangedObserver


class IModelChanger():
    def notify_change(self: IModelChangedObserver):
        pass