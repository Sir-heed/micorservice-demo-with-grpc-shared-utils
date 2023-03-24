from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProductFromReceiverRequest(_message.Message):
    __slots__ = ["product_receiver"]
    PRODUCT_RECEIVER_FIELD_NUMBER: _ClassVar[int]
    product_receiver: ProductReceiver
    def __init__(self, product_receiver: _Optional[_Union[ProductReceiver, _Mapping]] = ...) -> None: ...

class CreateProductFromReceiverResponse(_message.Message):
    __slots__ = ["product_receiver"]
    PRODUCT_RECEIVER_FIELD_NUMBER: _ClassVar[int]
    product_receiver: ProductReceiver
    def __init__(self, product_receiver: _Optional[_Union[ProductReceiver, _Mapping]] = ...) -> None: ...

class DeleteByIdRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class ProductReceiver(_message.Message):
    __slots__ = ["image", "product_id", "title"]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    image: str
    product_id: str
    title: str
    def __init__(self, product_id: _Optional[str] = ..., title: _Optional[str] = ..., image: _Optional[str] = ...) -> None: ...

class UpdateByIdRequest(_message.Message):
    __slots__ = ["product_receiver"]
    PRODUCT_RECEIVER_FIELD_NUMBER: _ClassVar[int]
    product_receiver: ProductReceiver
    def __init__(self, product_receiver: _Optional[_Union[ProductReceiver, _Mapping]] = ...) -> None: ...

class UpdateByIdResponse(_message.Message):
    __slots__ = ["product_receiver"]
    PRODUCT_RECEIVER_FIELD_NUMBER: _ClassVar[int]
    product_receiver: ProductReceiver
    def __init__(self, product_receiver: _Optional[_Union[ProductReceiver, _Mapping]] = ...) -> None: ...
