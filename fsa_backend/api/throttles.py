from rest_framework.throttling import UserRateThrottle, ScopedRateThrottle


class DefaultRateThrottle(UserRateThrottle):
    scope = "default_throttle"


class DefaultScopedRateThrottle(ScopedRateThrottle):
    scope = "default_scoped_throttle"
