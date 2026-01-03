from .models import UserProfile

def get_service_area_limit(user) -> int:
    profile = getattr(user, "profile", None)
    if not profile:
        return 5

    limits = {
        UserProfile.TIER_FREE: 5,
        UserProfile.TIER_PRO: 50,
        UserProfile.TIER_PREMIUM: 50000,
    }
    return limits.get(profile.tier, 5)
