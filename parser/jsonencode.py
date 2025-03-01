from sqlalchemy.ext.declarative import DeclarativeMeta
import json

# class AlchemyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj.__class__, DeclarativeMeta):
#             # Convert SQLAlchemy model to dictionary
#             fields = {}
#             for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
#                 data = obj.__getattribute__(field)
#                 try:
#                     json.dumps(data)
#                     fields[field] = data
#                 except TypeError:
#                     fields[field] = None
#             return fields
#         return json.JSONEncoder.default(self, obj)

def serialize_complex(result):
    if isinstance(result, list):
        return [serialize_complex_single(item) for item in result]
    else:
        return serialize_complex_single(result)

def serialize_complex_single(result):
    data = {c.name: getattr(result, c.name) for c in result.__table__.columns}
    # Add relationships
    if hasattr(result, 'addresses'):
        data['addresses'] = [serialize_complex_single(addr) for addr in result.addresses]
    return data