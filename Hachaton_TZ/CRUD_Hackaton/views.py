from dec import dec_object


class CreateMixin:
    def _get_or_set_objects_and_id(self):
        try:

            if (self.objects or not self.objects) and (self.id or not self.id):
                pass
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

    def __init__(self) -> None:
        self._get_or_set_objects_and_id()

    def post(self, **kwargs):
        self.id += 1
        object_ = dict(id=self.id, **kwargs)
        self.objects.append(object_)
        return {'status': 201, 'msg': object_}


class ListingMixin:
    def list(self):
        res = []
        for obj in self.objects:
            res.append({'id': obj['id'], 'marka': obj['marka'], 'model': obj['model'],
                        'god_vypuska': obj['god_vypuska'], 'obyem_dvigatelya': obj['obyem_dvigatelya'],
                        'svet': obj['svet'], 'tip_kuzova': obj['tip_kuzova'], 'probeg': obj['probeg'],
                        'sena': obj['sena']})
        return {'status': 200, 'msg': res}


class DetailMixin:
    @dec_object
    def detail(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            return {'status': 200, 'msg': obj}
        return {'status': 404, 'msg': 'Not Found!'}


class UpdateMixin:
    @dec_object
    def update(self, id, **kwargs):
        obj = kwargs.pop('object_')
        if obj:
            obj.update(**kwargs)
            return {'status': 206, 'msg': obj}
        return {'status': 404, 'msg': 'Not Found!'}


class DeleteMixin:
    @dec_object
    def delete(self, id, **kwargs):
        obj = kwargs.get('object_')
        if obj:
            self.objects.remove(obj)
            return {'status': 204, 'msg': 'Deleted!'}
        return {'status': 404, 'msg': 'Not Found!'}
