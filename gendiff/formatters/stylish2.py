SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '


def to_str(value, depth=2):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = SEPARATOR * (depth + 4)
        lines = []
        for key, inner_value in value.items():
            formatted_value = to_str(inner_value, depth + 4)
            lines.append(f"{indent}{NONE}{key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
        end_indent = SEPARATOR * (depth + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"


def make_stylish_result(diff, depth=1):
    indent = SEPARATOR * depth
    lines = []
    for item in diff:
        key_name = item['name']
        old_value = to_str(item.get("old_value"), depth)
        new_value = to_str(item.get("new_value"), depth)
        action = item["action"]
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
                    item.get("children"), depth + 1)
                lines.append(f"{indent}{NONE}{key_name}: {children}")
    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (depth - 2)
    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_diff_stylish(data):
    return make_stylish_result(data)
