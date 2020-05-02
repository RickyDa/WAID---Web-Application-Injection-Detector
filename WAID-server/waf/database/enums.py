import enum


class Action(enum.Enum):
    ALLOW = 0
    BLOCK = 1


class RuleType(enum.Enum):
    INJECTION_ATTACK = 0
    BLOCKED_HOST = 1


class AnomalyStatus(enum.Enum):
    UNCHECKED = 0
    ATTACK = 1
    NORM = 2


class PayloadType(enum.Enum):
    RESPONSE = 0
    REQUEST_GET = 1
    REQUEST_POST = 2


class UserRole(enum.Enum):
    ADMIN = 0
    READ_ONLY = 1
