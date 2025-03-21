import dataclasses
import json
import pathlib

from snakeware.message_identifiers import MessageIdentifier
from snakeware.response_statuses import ResponseStatus
from snakeware.message_parameters import MessageParameter

# TODO Need to detect errors in ranges. make sure that the msg_id exists and watnot.
# NOTE: The session_token might not infinitely increase — ie it might wrap around — but I'm not sure exactly when that happens. If it does wrap around, I need to detect session_tokens outside of the range. (this might be accounted for in the Command, Response, or Notification classes)


class Message(dict):
    def __setattr__(self, name, value):
        self[name] = value

    def __getattribute__(self, name):
        try:
            return self[name]
        except KeyError:
            return object.__getattribute__(self, name)


class Command(Message):
    def __init__(
        self,
        message_identifier: MessageIdentifier,
        session_token: int = None,
        message_parameter: int | str = None,
        **kwargs,
    ):
        self.msg_id = message_identifier
        self.token = session_token
        self.param = message_parameter
        for key, value in kwargs.items():
            self[key] = value


class AliveTick(Command):
    def __init__(self, session_token: int):
        super().__init__(
            message_identifier=MessageIdentifier.ALIVE_TICK, session_token=session_token
        )


class AppConnect(Command):
    def __init__(self, session_token: int):
        super().__init__(
            message_identifier=MessageIdentifier.APP_CONNECT, session_token=session_token
        )


class AppDisconnect(Command):
    def __init__(self, session_token: int):
        super().__init__(
            message_identifier=MessageIdentifier.APP_DISCONNECT, session_token=session_token
        )


# NOTE: I'm not sure if this name is accurate enough.
class CancelDataTransfer(Command):
    def __init__(self, session_token: int):
        super().__init__(
            message_identifier=MessageIdentifier.CANCEL_FILE_XFER, session_token=session_token
        )


class ChangeDirectory(Command):
    def __init__(self, session_token: int, directory_path: str):
        super().__init__(
            message_identifier=MessageIdentifier.CD,
            session_token=session_token,
            param=directory_path,
        )


class GetFileFragment(Command):
    def __init__(self, session_token: int, filepath: str, fragment_size: int, fragment_offset: int):
        super().__init__(
            message_identifier=MessageIdentifier.GET_FILE,
            session_token=session_token,
            param=filepath,
            fetch_size=fragment_size,
            offset=fragment_offset,
        )


class GetMediaInfo(Command):
    def __init__(self, session_token: int, filepath: str):
        super().__init__(
            message_identifier=MessageIdentifier.MEDIA_INFO,
            session_token=session_token,
            param=filepath,
        )


class ListDirectory(Command):
    def __init__(self, session_token: int):
        super().__init__(message_identifier=MessageIdentifier.LS, session_token=session_token)


class SetClientInformation(Command):
    def __init__(self, session_token: int, local_address: str, connection_type: str):
        super().__init__(
            message_identifier=MessageIdentifier.SET_CLNT_INFO,
            session_token=session_token,
            message_parameter=local_address,
            type=connection_type,
        )


class StartSession(Command):
    def __init__(self):
        super().__init__(message_identifier=MessageIdentifier.START_SESSION)


class StopSession(Command):
    def __init__(self, session_token: int):
        super().__init__(
            message_identifier=MessageIdentifier.STOP_SESSION, session_token=session_token
        )


# TODO: Maybe split this up into the different notification types?
class Notification(Message):
    def __init__(self, session_token: int, type: str):
        self.msg_id = MessageIdentifier.NOTIFICATION
        self.token = session_token
        self.type = type


class Response(Message):
    def __init__(
        self, message_identifier: int, response_status: int, parameter: int | str = None, **kwargs
    ):
        self.msg_id = message_identifier
        self.rval = response_status
        self.param = parameter
        for key, value in kwargs.item():
            self[key] = value
