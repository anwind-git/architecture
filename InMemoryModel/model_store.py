from ModelElements.poligonal_model import PoligonalModel
from ModelElements.Scene import Scene
from ModelElements.flash import Flash
from ModelElements.camera import Camera
from InMemoryModel.i_model_changed_observer import IModelChangedObserver
from InMemoryModel.i_model_changer import IModelChanger


class ModelStore(IModelChanger):
    def __init__(self,
                 model: PoligonalModel,
                 scene: Scene,
                 flash: Flash,
                 camera: Camera,
                 change_observer: IModelChangedObserver):
        self.models = model
        self.scenes = scene
        self.flashes = flash
        self.cameras = camera
        self.changeObservers = change_observer

    def get_scena(self: int):
        pass

    def notify_change(self: IModelChanger):
        pass

