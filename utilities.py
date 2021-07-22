def paginate_items(request, selection):
    ITEMS_PER_PAGE = 10 # default
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    items = [type.format() for type in selection]
    current_items = items[start: end]
    return current_items
