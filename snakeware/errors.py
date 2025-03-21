class CommandError(Exception):
    """
    Thrown for a negative rval.
    """

    pass


class AppNotReadyError(CommandError):
    """
    Thrown for the response status: APP_NOT_READY
    """

    pass


# NOTE: Needs a better name. I dunno exactly what this error means.
class ConfigNotExistError(CommandError):
    """
    CONFIG_NOT_EXIST
    """

    pass


# NOTE: Idk if this is an error.
class HDMIInserted(Exception):
    """
    Thrown for the response status: HDMI_INSERTED
    """

    pass


class InvalidOperationError(CommandError):
    """
    Thrown for the response status INVALID_OPERATION
    """

    pass


class InvalidOptionValueError(CommandError, ValueError):
    """
    Thrown for the response status INVALID_OPTION_VALUE
    """


class InvalidParameterError(CommandError):
    """
    Thrown for a INVALID_PARAM response status.
    """

    pass


class InvalidPathError(CommandError):
    """
    Thrown for a INVALID_PATH response status.
    """

    pass


class InvalidTokenError(CommandError):
    """
    Thrown for a INVALID_TOKEN response status.
    """

    pass


class InvalidTypeError(CommandError):
    """
    Thrown for a INVALID_TYPE response status.
    """

    pass


# NOTE: Idk what this should inherit from.
class JSONPackageError(Exception):
    """
    JSON_PACKAGE_ERROR
    """

    pass


# NOTE: Idk what this should inherit from.
class JSONPackageTimeout(Exception):
    """
    JSON_PACKAGE_TIMEOUT
    """

    pass


class JSONSyntaxError(CommandError, SyntaxError):
    """
    MQ_SENDING_ERROR
    """

    pass


# NOTE: Idk what MQ is for these two:
class MQReceivingError(CommandError):
    """
    MQ_RECEIVING_ERROR
    """

    pass


class MQSendingError(CommandError):
    """
    MQ_SENDING_ERROR
    """

    pass


# NOTE: Idk what this should inherit from.
class NoMatchingClientError(Exception):
    """
    FOUND_NO_MATCH_CLNT
    """

    pass


class OperationMismatchError(CommandError):
    """
    Thrown for the response status OPERATION_MISMATCH
    """

    pass


class OutOfMemmoryError(CommandError):
    """
    Thrown for the response status: NO_MORE_MEMORY
    """

    pass


class PIVNotAllowedError(CommandError):
    """
    Thrown for the response status: PIV_NOT_ALLOWED
    """

    pass


# NOTE: could use a better name
class ReachedMaximumClientsError(Exception):
    """
    REACH_MAX_CLNT
    """

    pass


class SessionStartFailError(CommandError):
    """
    SESSION_START_FAIL
    """

    pass


class SystemBusyError(CommandError):
    """
    Thrown for the response status: SYSTEM_BUSY
    """

    pass


class TokenLockedError(CommandError):
    """
    Thrown for a TOKEN_LOCKED response status.
    """

    pass


class UnknownError(CommandError):
    """
    Thrown for a UNKNOWN_ERROR response status, or all RESERVED response statuses.
    """

    pass


class UnsupportedOperationError(CommandError):
    """
    Thrown for the response status: OPERATION_UNSUPPORTED
    """

    pass
