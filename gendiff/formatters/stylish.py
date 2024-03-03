SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '
DEFAULT_INDENT = 4


def to_str(value, spaces_count=2):
    print('===to_str')
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
<<<<<<< Updated upstream
        indent = SEPARATOR * (depth + DEFAULT_INDENT)
=======
        indent = SEPARATOR * (spaces_count + 4)
>>>>>>> Stashed changes
        lines = []
        for key, inner_value in value.items():
            formatted_value = to_str(inner_value, spaces_count + 4)
            lines.append(f"{indent}{NONE}{key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
        end_indent = SEPARATOR * (spaces_count + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"

# def make_stylish_result(diff, spaces_count=2):
def make_stylish_result(diff, depth=1):
    spaces_count = depth*2
    indent = SEPARATOR * spaces_count
    lines = []
    for item in diff:
        key_name = item['name']
        old_value = to_str(item.get("old_value"), spaces_count)
        new_value = to_str(item.get("new_value"), spaces_count)
        action = item["action"]
<<<<<<< Updated upstream
        match action:
            case "unchanged":
                current_value = to_str(item.get("value"), depth)
                lines.append(f"{indent}{NONE}{key_name}: {current_value}")
            case "modified":
                lines.append(f"{indent}{DELETE}{key_name}: {old_value}")
                lines.append(f"{indent}{ADD}{key_name}: {new_value}")
            case "deleted":
                lines.append(f"{indent}{DELETE}{key_name}: {old_value}")
            case "added":
                lines.append(f"{indent}{ADD}{key_name}: {new_value}")
            case "nested":
                children = make_stylish_result(
                    item.get("children"), depth + DEFAULT_INDENT
                )
                lines.append(f"{indent}{NONE}{key_name}: {children}")
=======
        if action == "unchanged":
            current_value = to_str(item.get("value"), spaces_count)
            lines.append(f"{indent}{NONE}{key_name}: {current_value}")
        elif action == "modified":
            lines.append(f"{indent}{DELETE}{key_name}: {old_value}")
            lines.append(f"{indent}{ADD}{key_name}: {new_value}")
        elif action == "deleted":
            lines.append(f"{indent}{DELETE}{key_name}: {old_value}")
        elif action == "added":
            lines.append(f"{indent}{ADD}{key_name}: {new_value}")
        elif action == 'nested':
            children = make_stylish_result(
                item.get("children"), depth + 1
            )
            lines.append(f"{indent}{NONE}{key_name}: {children}")
>>>>>>> Stashed changes
    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (spaces_count - 2)

    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_diff_stylish(data):
    return make_stylish_result(data)
