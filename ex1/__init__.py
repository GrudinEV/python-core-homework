def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    tree = {}
    arrCategories = []
    for category in mapping['categoryIdsSorted']:
        arrItems = []
        for role in mapping['categories'][category]['roleIds']:
            arrItems += [{'id': role, 'text': mapping['roles'][role]['name']}]
        arrCategories += [{'id': 'category-' + category, 'text': mapping['categories'][category]['name'], 'items': arrItems}]
    tree.update({'categories': arrCategories})
    return tree
