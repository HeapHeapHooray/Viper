class EventHandler:
    def __init__(self):
        self._callbacks = {}
    def register_callback(self,handle,callback):
        if handle in self._callbacks.keys():
            self._callbacks[handle].add(callback)
        else:
            self._callbacks[handle] = set((callback,))
    def unregister_callback(self,handle,callback):
        if handle in self._callbacks.keys():
            self._callbacks[handle].remove(callback)
    def trigger(self,handle,*args):
        if not handle in self._callbacks.keys():
            return
        for callback in self._callbacks[handle]:
            callback(*args)
