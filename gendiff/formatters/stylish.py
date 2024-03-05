SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '
DEFAULT_INDENT = 4


def to_str(value, spaces_count=2, depth=1):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = SEPARATOR * (spaces_count + DEFAULT_INDENT)
        # indent = SEPARATOR * (depth * DEFAULT_INDENT + 2)
        lines = []
        for key, inner_value in value.items():
            formatted_value = to_str(
                inner_value,
                spaces_count + DEFAULT_INDENT,
                depth
            )
            lines.append(f"{indent}{NONE}{key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
        end_indent = SEPARATOR * (spaces_count + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"


def make_stylish_result(diff, spaces_count=2, depth=1):
    indent = SEPARATOR * (depth * DEFAULT_INDENT - 2)
    lines = []
    for item in diff:
        key_name = item['name']
        old_value = to_str(item.get("old_value"), spaces_count)
        new_value = to_str(item.get("new_value"), spaces_count)
        action = item["action"]
        match action:
            case "unchanged":
                current_value = to_str(item.get("value"), spaces_count, depth)
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
                    item.get("children"),
                    spaces_count + DEFAULT_INDENT,
                    depth + 1
                )
                lines.append(f"{indent}{NONE}{key_name}: {children}")

    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (depth * DEFAULT_INDENT - 4)

    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_diff_stylish(data):
    return make_stylish_result(data)
