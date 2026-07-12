class Mitigation:

    def __init__(
        self,
        zone_type,
        zone,
        time,
        index,
    ):
        self.zone_type = zone_type
        self.zone = zone
        self.time = time
        self.index = index

    def __str__(self):
        return (
            f"{self.zone_type} MITIGATION | "
            f"{self.time} | "
            f"index={self.index}"
        )