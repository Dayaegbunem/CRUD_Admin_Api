def item_serializer(item) -> dict:
    return {
        'id': str(item['_id']),
        'name': item['name'],
        'description': item['description'],
        'completed': item['completed']
    }

def items_serializer(items) -> list:
    return [item_serializer(item) for item in items]