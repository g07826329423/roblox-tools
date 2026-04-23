class RobloxError(Exception):
    """Base class for Roblox exceptions."""
    pass

class AssetNotFoundError(RobloxError):
    """Raised when an asset cannot be found."""
    def __init__(self, asset_id):
        self.asset_id = asset_id
        super().__init__(f"Asset not found: {asset_id}")

class InvalidUserError(RobloxError):
    """Raised when a user is invalid."""
    def __init__(self, username):
        self.username = username
        super().__init__(f"Invalid user: {username}")

class PermissionDeniedError(RobloxError):
    """Raised when a user lacks permissions."""
    def __init__(self, action):
        self.action = action
        super().__init__(f"Permission denied for action: {action}")

class RateLimitExceededError(RobloxError):
    """Raised when API rate limit is exceeded."""
    def __init__(self, limit):
        self.limit = limit
        super().__init__(f"Rate limit exceeded: {limit}")