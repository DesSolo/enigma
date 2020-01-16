from core import settings


def user_agent(agent):
    for pattern in settings.DENY_USER_AGENTS:
        if pattern.match(agent):
            return False
    return True
