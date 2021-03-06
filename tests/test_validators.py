import pytest
import config


@pytest.fixture()
def user_agent_validator():
    config.DENY_USER_AGENTS = [
        r'curl',
        r'^Wget/1.20.3$'
    ]
    from core.validators import user_agent
    return user_agent


@pytest.mark.parametrize(
    'user_agent, allow',
    [
        ('curl/7.66.0', False),
        ('curl/7.0.0', False),
        ('curl/', False),
        ('curl', False),
        ('Wget/1', True),
        ('Wget', True),
        ('Wget/1.20.3', False),
        ('Curl', True),
        ('CURL', True),
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)', True),
        ('', True)
    ]
)
def test_user_agent(user_agent_validator, user_agent, allow):
    assert user_agent_validator(user_agent) is allow
