
from flask_talisman import Talisman

# Configure Content Security Policy
csp = {
    'default-src': ["'self'"],
    'script-src': ["'self'"],
    'style-src': ["'self'"],
}

Talisman(
    app,
    content_security_policy=csp,
    force_https=False
)
