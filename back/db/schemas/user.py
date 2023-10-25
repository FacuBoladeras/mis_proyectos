# Clase en vídeo (22/12/2022): https://www.twitch.tv/videos/1686104006

### User schema ###

def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "marca": user["marca"],
            "modelo": user["modelo"],
            "patente": user["patente"]}


def users_schema(users) -> list:
    return [user_schema(user) for user in users]
