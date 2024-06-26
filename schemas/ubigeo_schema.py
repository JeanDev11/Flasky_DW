from utils.ma import ma
from marshmallow import fields

class UbigeoSchema(ma.Schema):
    idubigeo = fields.Integer()
    departamento = fields.String()

ubigeo_schema = UbigeoSchema()
ubigeos_schema = UbigeoSchema(many=True)