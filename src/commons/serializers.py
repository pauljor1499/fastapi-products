# Helper function to convert MongoDB document (which uses ObjectId) to a Python dict
def item_serializer(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "name": item["name"],
        "description": item["description"],
        "price": item["price"]
    }