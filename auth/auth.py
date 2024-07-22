from fastapi_users.authentication import CookieTransport, JWTStrategy

SECRET = "SECRET"

cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)